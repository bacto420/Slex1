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
