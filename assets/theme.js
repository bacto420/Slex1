/* BACTO theme — minimal JS */
(function () {
  'use strict';

  document.documentElement.classList.remove('no-js');

  /* Mobile menu toggle */
  var toggle = document.querySelector('[data-menu-toggle]');
  var nav = document.querySelector('[data-menu]');

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.getAttribute('data-open') === 'true';
      nav.setAttribute('data-open', open ? 'false' : 'true');
      toggle.setAttribute('aria-expanded', open ? 'false' : 'true');
      toggle.textContent = open ? 'Menu' : 'Close';
    });
  }




  /* ------------------------------------------------------------------
     Bundle deal — choosing between products, picking a size, and keeping
     the totals honest while the customer switches.

     Liquid has already printed a correct, complete bundle for the default
     selection, hidden inputs included. This only takes over once a choice
     is made, so the section works with the script blocked: one product and
     one size per slot, exactly what was rendered.
     ------------------------------------------------------------------ */
  var formatMoney = function (cents, format) {
    var value = (cents || 0) / 100;

    /* Shopify's money format may carry markup — merchants wrap the amount
       in a span often enough. This lands in textContent, so any tags would
       show up as literal angle brackets in the totals. */
    format = String(format).replace(/<[^>]*>/g, '');

    var withSeparators = function (decimals, thousands, decimalMark) {
      var fixed = value.toFixed(decimals);
      var parts = fixed.split('.');
      var whole = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, thousands);
      return decimals ? whole + decimalMark + parts[1] : whole;
    };

    return format.replace(/\{\{\s*(\w+)\s*\}\}/g, function (_, token) {
      switch (token) {
        case 'amount_no_decimals':                      return withSeparators(0, ',', '.');
        case 'amount_with_comma_separator':             return withSeparators(2, '.', ',');
        case 'amount_no_decimals_with_comma_separator': return withSeparators(0, '.', ',');
        case 'amount_with_apostrophe_separator':        return withSeparators(2, "'", '.');
        default:                                        return withSeparators(2, ',', '.');
      }
    });
  };

  var setupBundle = function (root) {
    var pct    = parseInt(root.getAttribute('data-bundle-pct'), 10) || 0;
    var scope  = root.getAttribute('data-bundle-scope') || 'total';
    var format = root.getAttribute('data-money-format') || '{{amount}}';

    var money = function (cents) { return formatMoney(cents, format); };

    var totalRegular = root.querySelector('[data-total-regular]');
    var totalBundle  = root.querySelector('[data-total-bundle]');
    var totalSaving  = root.querySelector('[data-total-saving]');
    var form         = root.querySelector('[data-bundle-form]');
    var submit       = form ? form.querySelector('button[type="submit"]') : null;

    var slots = [];

    Array.prototype.forEach.call(root.querySelectorAll('[data-slot]'), function (el) {
      var json = el.querySelector('[data-slot-json]');
      if (!json) return;

      var data;
      try { data = JSON.parse(json.textContent); } catch (e) { return; }
      if (!data.products || !data.products.length) return;

      var slot = {
        el: el,
        products: data.products,
        chosen: data.products[0],
        variant: null,
        priceEl: el.querySelector('[data-slot-price]'),
        select: el.querySelector('[data-slot-variant]'),
        sizeBox: el.querySelector('.bundle__size'),
        sizeLabel: el.querySelector('.bundle__size-label')
      };
      slot.variant = pickVariant(slot.chosen, null);
      slots.push(slot);

      Array.prototype.forEach.call(el.querySelectorAll('[data-switch]'), function (button) {
        button.addEventListener('click', function () {
          choose(slot, button.getAttribute('data-switch'));
        });
      });

      if (slot.select) {
        slot.select.addEventListener('change', function () {
          slot.variant = byId(slot.chosen, slot.select.value) || slot.variant;
          render();
        });
      }
    });

    if (!slots.length) return;

    function byId(product, id) {
      var found = null;
      product.variants.forEach(function (v) {
        if (String(v.id) === String(id)) found = v;
      });
      return found;
    }

    /* Keep the size across a product switch where it exists — someone who
       picked L for one jacket means L for the other. Otherwise fall to the
       first size actually in stock. */
    function pickVariant(product, keepTitle) {
      var match = null;
      if (keepTitle) {
        product.variants.forEach(function (v) {
          if (!match && v.title === keepTitle && v.available) match = v;
        });
      }
      if (!match) {
        product.variants.forEach(function (v) {
          if (!match && v.available) match = v;
        });
      }
      return match || product.variants[0] || null;
    }

    function choose(slot, productId) {
      var next = null;
      slot.products.forEach(function (p) {
        if (String(p.id) === String(productId)) next = p;
      });
      if (!next || next === slot.chosen) return;

      var keep = slot.variant ? slot.variant.title : null;
      slot.chosen = next;
      slot.variant = pickVariant(next, keep);
      render();
    }

    function renderSlot(slot) {
      Array.prototype.forEach.call(slot.el.querySelectorAll('[data-option]'), function (tile) {
        var on = String(tile.getAttribute('data-option')) === String(slot.chosen.id);
        tile.classList.toggle('is-hidden', !on);
        tile.setAttribute('aria-pressed', on ? 'true' : 'false');
      });

      Array.prototype.forEach.call(slot.el.querySelectorAll('[data-switch]'), function (button) {
        var on = String(button.getAttribute('data-switch')) === String(slot.chosen.id);
        button.setAttribute('aria-pressed', on ? 'true' : 'false');
      });

      if (slot.select) {
        var single = slot.chosen.hasOneVariant || slot.chosen.variants.length < 2;
        if (slot.sizeBox) slot.sizeBox.hidden = single;
        if (slot.sizeLabel) slot.sizeLabel.textContent = slot.chosen.optionName || '';

        slot.select.innerHTML = '';
        slot.chosen.variants.forEach(function (v) {
          var option = document.createElement('option');
          option.value = v.id;
          option.textContent = v.title;
          option.disabled = !v.available;
          if (slot.variant && v.id === slot.variant.id) option.selected = true;
          slot.select.appendChild(option);
        });
      }

      if (slot.priceEl && slot.variant) {
        slot.priceEl.textContent = money(slot.variant.price);
      }
    }

    function render() {
      var regular = 0;
      var cheapest = 0;
      var sellable = true;

      slots.forEach(function (slot) {
        renderSlot(slot);
        if (!slot.variant) { sellable = false; return; }
        if (!slot.variant.available) sellable = false;
        regular += slot.variant.price;
        if (!cheapest || slot.variant.price < cheapest) cheapest = slot.variant.price;
      });

      var base = scope === 'cheapest' ? cheapest : regular;
      var saving = Math.round(base * pct / 100);

      if (totalRegular) totalRegular.textContent = money(regular);
      if (totalBundle)  totalBundle.textContent  = money(regular - saving);
      if (totalSaving)  totalSaving.textContent  = money(saving);

      if (form) {
        slots.forEach(function (slot, i) {
          var input = form.querySelector('[data-line="' + i + '"]');
          if (input && slot.variant) input.value = slot.variant.id;
        });
      }

      if (submit) submit.disabled = !sellable;
    }

    render();
  };

  Array.prototype.forEach.call(document.querySelectorAll('[data-bundle]'), setupBundle);

  /* ------------------------------------------------------------------
     The footer carries a "Cookie-Einstellungen" link that reopens our own
     banner. With that banner switched off — Shopify's native one used
     instead — the link would sit there doing nothing, so it is taken out.
     Shopify's banner brings its own way back to the choice.
     ------------------------------------------------------------------ */
  if (!document.getElementById('CookieBanner')) {
    Array.prototype.forEach.call(
      document.querySelectorAll('[data-cookie-settings]'),
      function (link) {
        var row = link.closest ? link.closest('li') : null;
        (row || link).hidden = true;
      }
    );
  }

  /* ------------------------------------------------------------------
     Footer columns as an accordion.

     Built as an enhancement rather than as markup: the page ships with
     every column open, and only a browser running this script folds them
     away. Without JavaScript the legal links stay visible, which is what
     § 5 ECG asks for — a fold that never opens would hide the Impressum.
     ------------------------------------------------------------------ */
  var cols = document.querySelector('[data-footer-accordion]');

  if (cols) {
    var mode = cols.getAttribute('data-footer-accordion') || 'always';
    var phone = window.matchMedia('(max-width: 749px)');
    var panels = [];

    Array.prototype.forEach.call(
      cols.querySelectorAll('[data-footer-heading]'),
      function (heading, i) {
        var panel = heading.parentNode.querySelector('[data-footer-panel]');
        if (!panel) return;

        /* The heading keeps its level; the button lives inside it, so the
           outline stays intact for screen readers. */
        var button = document.createElement('button');
        button.type = 'button';
        button.className = 'footer__toggle';
        button.innerHTML = heading.innerHTML;
        heading.innerHTML = '';
        heading.appendChild(button);

        panel.id = panel.id || 'FooterPanel' + i;
        button.setAttribute('aria-controls', panel.id);

        var setOpen = function (open) {
          panel.hidden = !open;
          button.setAttribute('aria-expanded', open ? 'true' : 'false');
        };

        button.addEventListener('click', function () {
          setOpen(button.getAttribute('aria-expanded') !== 'true');
        });

        panels.push(setOpen);
      }
    );

    /* "Only on phones" has to react to a window being resized across the
       breakpoint, otherwise a column folded on a narrow window stays folded
       when it widens again. */
    var apply = function () {
      var folded = mode === 'always' || (mode === 'mobile' && phone.matches);
      cols.setAttribute('data-folded', folded ? 'true' : 'false');
      panels.forEach(function (setOpen) { setOpen(!folded); });
    };

    apply();
    if (mode === 'mobile') {
      if (phone.addEventListener) phone.addEventListener('change', apply);
      else if (phone.addListener) phone.addListener(apply);
    }
  }

  /* ------------------------------------------------------------------
     Withdrawal form — two steps, as § 13a FAGG requires: fill in, then a
     separate screen whose only primary action is "Widerruf bestätigen".
     Runs for every .widerruf__form on the page (the footer dialog and, if
     present, the standalone page). Without JS the noscript button submits.
     ------------------------------------------------------------------ */
  var setupWiderruf = function (form) {
    var step1 = form.querySelector('[data-step="1"]');
    var step2 = form.querySelector('[data-step="2"]');
    var review = form.querySelector('[data-widerruf-review]');
    var next = form.querySelector('[data-widerruf-next]');
    var back = form.querySelector('[data-widerruf-back]');
    if (!step1 || !step2 || !next) return;

    var labelFor = function (field) {
      var l = form.querySelector('label[for="' + field.id + '"]');
      return l ? l.textContent.replace('*', '').trim() : field.name;
    };

    next.addEventListener('click', function () {
      var missing = null;
      Array.prototype.forEach.call(step1.querySelectorAll('[data-required]'), function (f) {
        var bad = !f.value.trim() || (f.type === 'email' && !f.checkValidity());
        if (bad && !missing) missing = f;
        if (bad) f.setAttribute('aria-invalid', 'true');
        else f.removeAttribute('aria-invalid');
      });
      if (missing) {
        if (missing.reportValidity) missing.reportValidity();
        missing.focus();
        return;
      }

      review.innerHTML = '';
      var fields = step1.querySelectorAll('input[name^="contact["], textarea[name^="contact["]');
      Array.prototype.forEach.call(fields, function (f) {
        if (f.type === 'hidden' || !f.value.trim()) return;
        var row = document.createElement('div');
        var dt = document.createElement('dt');
        var dd = document.createElement('dd');
        dt.textContent = labelFor(f);
        dd.textContent = f.value.trim();
        row.appendChild(dt); row.appendChild(dd);
        review.appendChild(row);
      });

      /* Stamp the moment of submission for the acknowledgement email. */
      var stamp = form.querySelector('[data-widerruf-stamp]') || document.getElementById('WiderrufStamp');
      var body = form.querySelector('[data-widerruf-body]') || document.getElementById('WiderrufBody');
      var now = new Date();
      if (stamp) stamp.value = now.toLocaleString('de-AT') + ' (' + now.toISOString() + ')';
      if (body) {
        var lines = ['Widerruf über die Rücktrittsfunktion der Website.'];
        Array.prototype.forEach.call(review.querySelectorAll('div'), function (row) {
          lines.push(row.querySelector('dt').textContent + ': ' + row.querySelector('dd').textContent);
        });
        lines.push('Abgesendet am: ' + (stamp ? stamp.value : ''));
        body.value = lines.join('\n');
      }

      step1.hidden = true;
      step2.hidden = false;
      step2.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    });

    if (back) {
      back.addEventListener('click', function () {
        step2.hidden = true;
        step1.hidden = false;
        step1.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      });
    }
  };

  Array.prototype.forEach.call(document.querySelectorAll('.widerruf__form'), setupWiderruf);

  /* ------------------------------------------------------------------
     Dialog wiring, with a fallback for browsers without <dialog>.
     ------------------------------------------------------------------ */
  var dlg = document.getElementById('WiderrufDialog');
  if (dlg) {
    var supportsDialog = typeof dlg.showModal === 'function';

    var openDialog = function () {
      if (supportsDialog) dlg.showModal();
      else { dlg.setAttribute('open', ''); dlg.classList.add('wdialog--fallback'); }
      var first = dlg.querySelector('input, button');
      if (first) first.focus();
    };
    var closeDialog = function () {
      if (supportsDialog) dlg.close();
      else { dlg.removeAttribute('open'); dlg.classList.remove('wdialog--fallback'); }
    };

    Array.prototype.forEach.call(document.querySelectorAll('[data-widerruf-open]'), function (btn) {
      btn.addEventListener('click', openDialog);
    });
    Array.prototype.forEach.call(dlg.querySelectorAll('[data-widerruf-close]'), function (btn) {
      btn.addEventListener('click', closeDialog);
    });

    /* Click on the backdrop closes it. */
    dlg.addEventListener('click', function (e) {
      if (e.target === dlg) closeDialog();
    });

    /* Shopify bounces back to the page after submitting — reopen so the
       customer actually sees the confirmation. */
    if (dlg.querySelector('[data-widerruf-success]') ||
        /[?&]contact_posted=true/.test(window.location.search)) {
      openDialog();
    }
  }
})();
