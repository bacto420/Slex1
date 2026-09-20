#!/usr/bin/env python3
"""Generate the size chart layouts.

One garment, one entry in GARMENTS: its drawing, its measurements. Both the
portrait and the wide layout come out of the same entry, so the numbers
cannot drift apart between the two files the way they did when each was
edited by hand.

The Michroma woff2 is inlined as base64, so a rendered file carries the
shop's typeface with no font install and no network at render time.
"""

import base64
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
THEME = HERE.parent.parent

FONT = base64.b64encode((THEME / 'assets' / 'michroma-latin.woff2').read_bytes()).decode()

# Long-sleeve top: curved hem, wide ribbed cuffs, dropped shoulders.
FIGURE_LONGSLEEVE = """
<svg viewBox="0 0 400 330" class="figure">
  <g fill="none" stroke="#fff" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round">
    <path d="M132 72 L176 72 Q200 90 224 72 L268 72
             L358 200 L318 228 L266 130 L272 232
             Q200 274 128 232 L134 130 L82 228 L42 200 Z"/>
  </g>
  <g fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" opacity="0.9">
    <path d="M178 80 Q200 98 222 80"/>
    <path d="M342 177 L302 205"/>
    <path d="M58 177 L98 205"/>
  </g>
  <g fill="none" stroke="#fff" stroke-width="1" opacity="0.45">
    <path d="M347 185 L307 213 M353 192 L313 220"/>
    <path d="M53 185 L93 213 M47 192 L87 220"/>
  </g>
  <g fill="none" stroke="#fff" stroke-width="1.2" opacity="0.55">
    <path d="M132 46 L268 46 M132 40 L132 52 M268 40 L268 52"/>
    <path d="M128 294 L272 294 M128 288 L128 300 M272 288 L272 300"/>
    <path d="M240 134 L240 246 M234 134 L246 134 M234 246 L246 246"/>
    <path d="M279 64 L369 192 M274 66 L284 61 M364 194 L374 189"/>
  </g>
  <g fill="#fff" class="figure__letters">
    <text x="200" y="32"  text-anchor="middle">A</text>
    <text x="200" y="318" text-anchor="middle">D</text>
    <text x="226" y="196" text-anchor="end">B</text>
    <text x="352" y="104" text-anchor="start">C</text>
  </g>
</svg>
"""

# Hooded zip jacket: hood, centre-front zip, two welt pockets, gathered hem,
# tabbed cuffs. A is taken from the shoulder, so it runs beside the body
# rather than through it.
FIGURE_JACKET = """
<svg viewBox="0 0 400 330" class="figure">
  <g fill="none" stroke="#fff" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round">
    <path d="M122 110 L160 104 L240 104 L278 110
             L334 236 L302 250 L264 162 L262 272
             Q232 276 200 272 Q168 268 138 272
             L136 162 L98 250 L66 236 Z"/>
    <path d="M150 104 C 148 70 168 52 200 52 C 232 52 252 70 250 104"/>
  </g>
  <g fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" opacity="0.85">
    <path d="M158 102 C 156 76 172 62 200 62 C 228 62 244 76 242 102"/>
    <path d="M200 104 L200 270"/>
    <path d="M137 252 L263 252"/>
    <path d="M160 190 L170 232"/>
    <path d="M240 190 L230 232"/>
    <path d="M72 223 L104 237"/>
    <path d="M328 223 L296 237"/>
  </g>
  <g fill="none" stroke="#fff" stroke-width="1.2" opacity="0.55">
    <path d="M36 104 L36 272 M30 104 L42 104 M30 272 L42 272"/>
    <path d="M137 186 L263 186 M137 180 L137 192 M263 180 L263 192"/>
    <path d="M294 103 L350 229 M289 105 L299 100 M345 231 L355 226"/>
  </g>
  <g fill="#fff" class="figure__letters">
    <text x="26"  y="196" text-anchor="end">A</text>
    <text x="168" y="176" text-anchor="middle">B</text>
    <text x="364" y="160" text-anchor="start">C</text>
  </g>
</svg>
"""

GARMENTS = {
    'longsleeve': {
        'figure': FIGURE_LONGSLEEVE,
        'sizes': ['S', 'M', 'L', 'XL'],
        'rows': [
            ('A', 'Shoulder width',            ['53', '55', '57', '59']),
            ('B', 'Length from armpit',        ['39', '40', '41', '43']),
            ('C', 'Sleeve length from shoulder',['67', '68', '69', '70']),
            ('D', 'Hem width',                 ['55', '57', '60', '63']),
        ],
        'note': 'Measured with a tolerance of ±2 cm. If in doubt, take the larger size.',
    },
    'jacket': {
        'figure': FIGURE_JACKET,
        'sizes': ['XS', 'S', 'M', 'L', 'XL'],
        'rows': [
            ('A', 'Length',         ['70', '73', '76', '79', '82']),
            ('B', 'Half chest',     ['55', '57', '59', '61', '63']),
            ('C', 'Sleeve length',  ['76', '78', '80', '82', '84']),
        ],
        'note': ('Half chest is measured flat from seam to seam — double it for the full '
                 'circumference. Tolerance ±2 cm. If in doubt, take the larger size.'),
    },
}

INTRO = ('All measurements are taken from the garment laid flat, not from the body. '
         'Values in centimetres.')

PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<style>
  @font-face {
    font-family: 'Michroma';
    src: url(data:font/woff2;base64,__FONT__) format('woff2');
    font-weight: 400;
    font-display: block;
  }

  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; background: #000; }

  body {
    width: __W__px;
    height: __H__px;
    color: #fff;
    /* Michroma carries the brand voice; the numbers sit in a plain grotesk,
       where a 5 cannot be mistaken for an S. */
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    display: flex;
    flex-direction: column;
    padding: __PAD__;
  }

  .brand {
    font-family: 'Michroma', sans-serif;
    font-size: __BRAND__px;
    letter-spacing: 0.22em;
    color: #8a8a8a;
    margin-bottom: __BRANDGAP__px;
  }

  h1 {
    font-family: 'Michroma', sans-serif;
    font-size: __H1__px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin: 0 0 __H1GAP__px;
  }

  .intro {
    font-size: __INTRO__px;
    line-height: 1.6;
    color: #cfcfcf;
    margin: 0 0 __INTROGAP__px;
    max-width: 46ch;
  }

  .main { flex: 1 1 auto; }

  .figure { width: 100%; height: auto; display: block; }
  .figure__letters text { font-family: 'Michroma', sans-serif; font-size: 19px; }

  table { width: 100%; border-collapse: collapse; }

  th, td {
    padding: __CELLY__px __CELLX__px;
    text-align: left;
    border-bottom: 1px solid #1f1f1f;
    font-size: __CELL__px;
  }

  thead th {
    font-family: 'Michroma', sans-serif;
    font-weight: 400;
    font-size: __HEAD__px;
    letter-spacing: 0.08em;
    color: #8a8a8a;
    text-transform: uppercase;
  }

  tbody th { font-weight: 400; color: #fff; }
  tbody td { font-variant-numeric: tabular-nums; }

  .letter {
    display: inline-block;
    min-width: 2em;
    color: #8a8a8a;
    font-family: 'Michroma', sans-serif;
    font-size: 0.85em;
  }

  .measure { width: __MEASURE__%; }

  .note {
    font-size: __NOTE__px;
    line-height: 1.6;
    color: #a0a0a0;
    margin: __NOTEGAP__px 0 0;
  }
</style></head>
<body>
  <div class="brand">BACTO</div>
  <h1>Size chart</h1>
  <p class="intro">__INTROTEXT__</p>
  <div class="main">__MAIN__</div>
  <p class="note">__NOTETEXT__</p>
</body></html>"""


def table(garment):
    head = "".join('<th>%s</th>' % s for s in garment['sizes'])
    body = "".join(
        '<tr><th><span class="letter">%s</span>%s</th>%s</tr>'
        % (letter, label, "".join('<td>%s</td>' % v for v in values))
        for letter, label, values in garment['rows'])
    return ('<table><thead><tr><th class="measure">Measurement</th>' + head
            + '</tr></thead><tbody>' + body + '</tbody></table>')


def write(path, w, h, pad, measure, sizes, main, note):
    s = (PAGE.replace('__FONT__', FONT).replace('__W__', str(w)).replace('__H__', str(h))
             .replace('__PAD__', pad).replace('__MAIN__', main)
             .replace('__MEASURE__', str(measure))
             .replace('__INTROTEXT__', INTRO).replace('__NOTETEXT__', note))
    for key, val in sizes.items():
        s = s.replace('__%s__' % key, str(val))
    pathlib.Path(path).write_text(s)
    print('geschrieben:', pathlib.Path(path).name)


for name, garment in GARMENTS.items():
    # More size columns leave the label column less room.
    measure = 44 if len(garment['sizes']) < 5 else 36
    fig, tbl = garment['figure'].strip(), table(garment)

    # Portrait 1200x1500 — the shape of the product photographs, so it slots
    # into the gallery without breaking the grid.
    write(HERE / ('%s-portrait.html' % name), 1200, 1500, '80px 84px', measure,
          dict(BRAND=18, BRANDGAP=44, H1=48, H1GAP=26, INTRO=20, INTROGAP=40,
               CELLY=22, CELLX=14, CELL=25, HEAD=17, NOTE=19, NOTEGAP=28),
          '<div style="width:68%;margin:0 auto 24px">' + fig + '</div>' + tbl,
          garment['note'])

    # Wide 1600x900 — for a description or a banner.
    write(HERE / ('%s-wide.html' % name), 1600, 900, '60px 76px', measure,
          dict(BRAND=15, BRANDGAP=30, H1=38, H1GAP=20, INTRO=17, INTROGAP=38,
               CELLY=26, CELLX=14, CELL=22, HEAD=15, NOTE=18, NOTEGAP=34),
          '<div style="display:grid;grid-template-columns:34% 1fr;gap:80px;align-items:center">'
          '<div>' + fig + '</div>' + tbl + '</div>',
          garment['note'])
