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

# Long-sleeve top: boxy body, straight hem, dropped shoulders, the sleeve
# drawn as a second tube under the shoulder. Traced off the reference sketch
# the same way as the jacket, so the form is the sketch's; only the stroke is
# imposed — one weight, square ends.
FIGURE_LONGSLEEVE = """
<svg viewBox="0 0 400 330" class="figure">
  <g fill="none" stroke="#fff" stroke-width="2.4"
     stroke-linecap="square" stroke-linejoin="miter" stroke-miterlimit="4">
    <path d="M265.8 264.4 C247.9 264.3 182.1 263.8 158.8 263.8 C135.5 263.9 131.6 267.6 126.1 264.5 C120.7 261.5 125.5 262.5 126.1 245.5 C126.8 228.5 129.6 176.6 130.2 162.3 C130.7 148.0 129.7 160.3 129.6 159.9"/>
    <path d="M279.3 181.3 C283.1 188.4 296.3 213.0 302.0 224.1 C307.6 235.2 310.7 242.3 313.2 248.0 C315.7 253.7 316.1 256.5 317.1 258.3 C318.1 260.0 314.5 260.2 319.2 258.4 C323.8 256.6 340.8 250.0 345.0 247.6 C349.2 245.2 346.1 247.8 344.5 244.1 C342.9 240.4 342.7 239.3 335.3 225.4 C327.9 211.4 305.9 171.2 300.0 160.3"/>
    <path d="M112.5 182.4 C108.7 189.6 95.5 213.9 89.8 225.4 C84.0 236.8 80.3 245.2 77.8 250.9 C75.3 256.6 75.5 258.1 74.6 259.5 C73.8 261.0 77.3 261.3 72.7 259.5 C68.0 257.7 51.1 251.1 46.8 248.7 C42.6 246.3 45.5 249.4 47.2 245.4 C49.0 241.3 50.1 238.5 57.5 224.5 C65.0 210.5 86.1 172.0 91.8 161.4"/>
    <path d="M175.5 79.3 C171.3 80.6 156.9 84.7 150.0 87.0 C143.1 89.4 138.4 91.3 134.1 93.3 C129.8 95.3 127.6 96.5 124.2 99.1 C120.8 101.7 120.1 102.5 113.8 108.7 C107.5 114.9 92.4 130.3 86.6 136.5 C80.7 142.7 80.0 143.9 78.6 145.8 C77.3 147.6 77.1 145.9 78.6 147.6 C80.1 149.3 85.5 153.7 87.7 156.1 C89.9 158.4 91.1 160.5 91.8 161.4"/>
    <path d="M219.5 79.1 C223.6 80.4 237.1 84.2 244.2 86.8 C251.3 89.3 257.8 92.1 262.2 94.4 C266.7 96.7 266.8 97.0 270.9 100.6 C275.0 104.3 281.0 110.4 286.8 116.3 C292.7 122.2 301.6 131.3 306.0 136.1 C310.4 140.8 312.0 142.9 313.2 144.7 C314.4 146.4 314.6 144.9 313.1 146.6 C311.6 148.3 306.2 152.8 304.1 155.1 C301.9 157.4 300.7 159.4 300.0 160.3"/>
    <path d="M262.2 158.8 C262.1 159.5 261.2 150.9 261.7 162.9 C262.2 174.9 264.5 213.9 265.2 230.8 C265.8 247.7 265.7 258.8 265.8 264.4"/>
    <path d="M175.5 79.3 C175.9 80.7 176.7 85.2 177.9 87.6 C179.2 90.0 181.5 92.1 183.2 93.6 C184.9 95.0 186.4 95.6 188.1 96.3 C189.8 97.1 191.1 97.7 193.4 98.0 C195.6 98.3 199.1 98.7 201.7 98.4 C204.3 98.1 207.0 97.4 209.2 96.2 C211.4 95.0 213.5 93.2 215.0 91.5 C216.6 89.7 217.6 87.7 218.4 85.6 C219.1 83.6 219.3 80.2 219.5 79.1"/>
    <path d="M279.3 181.3 C278.7 181.6 276.5 183.2 275.6 183.4 C274.7 183.7 276.0 186.8 273.9 182.9 C271.9 178.9 265.2 163.7 263.2 159.7 C261.3 155.7 262.3 158.9 262.2 158.8"/>
    <path d="M129.6 159.9 C129.4 160.1 130.6 156.6 128.6 160.6 C126.7 164.7 119.9 180.1 117.8 184.1 C115.7 188.1 117.2 184.8 116.3 184.5 C115.4 184.2 113.2 182.8 112.5 182.4"/>
    <path d="M300.0 160.3 L279.3 181.3"/>
    <path d="M91.8 161.4 L112.5 182.4"/>
    <path d="M129.6 159.9 L130.2 156.1"/>
    <path d="M261.6 154.9 L262.2 158.8"/>
  </g>
  <g fill="none" stroke="#fff" stroke-width="1.2" stroke-linecap="square" opacity="0.55">
    <path d="M129 56 L262 56 M129 50 L129 62 M262 50 L262 62"/>
    <path d="M125 292 L266 292 M125 286 L125 298 M266 286 L266 298"/>
    <path d="M236 159 L236 265 M230 159 L242 159 M230 265 L242 265"/>
    <path d="M290.3 79.7 L367.3 237.8 M285.8 81.9 L294.8 77.5 M362.8 240.0 L371.8 235.6"/>
  </g>
  <g fill="#fff" class="figure__letters">
    <text x="196" y="42"  text-anchor="middle">A</text>
    <text x="196" y="314" text-anchor="middle">D</text>
    <text x="226" y="216" text-anchor="end">B</text>
    <text x="340" y="153" text-anchor="middle">C</text>
  </g>
</svg>
"""

# Hooded zip jacket. The silhouette is traced off the reference sketch, down
# to the hand-drawn wobble in the hem, so the shape is the sketch's and not a
# redrawing of it. Only the stroke was changed: one weight throughout and
# square line ends, so no line tapers or rounds off against its neighbour.
# A is taken from the shoulder, so it runs beside the body rather than
# through it.
FIGURE_JACKET = """
<svg viewBox="0 0 400 330" class="figure">
  <g fill="none" stroke="#fff" stroke-width="2.4"
     stroke-linecap="square" stroke-linejoin="miter" stroke-miterlimit="4">
    <path d="M169.1 69.5 C169.5 71.6 171.5 77.1 171.5 81.9 C171.5 86.7 169.7 94.2 169.3 98.3 C168.9 102.5 173.0 103.1 169.3 107.0 C165.6 110.8 153.1 117.5 147.2 121.7 C141.3 125.9 138.4 128.0 133.9 132.2 C129.5 136.3 125.5 140.6 120.6 146.7 C115.7 152.8 110.1 160.3 104.5 168.6 C98.9 176.9 92.6 186.6 87.0 196.5 C81.3 206.4 75.0 218.1 70.5 227.8 C66.1 237.5 62.1 249.1 60.2 254.7 C58.3 260.4 59.0 260.3 59.1 262.0 C59.2 263.6 60.4 264.4 60.7 264.9"/>
    <path d="M228.5 74.5 C228.6 74.6 229.3 73.5 229.1 75.0 C229.0 76.6 227.4 80.3 227.6 83.8 C227.7 87.3 229.6 92.0 230.1 96.0 C230.6 100.0 227.1 103.4 230.5 107.6 C233.9 111.7 244.7 116.7 250.6 120.9 C256.4 125.0 261.0 128.3 265.6 132.5 C270.2 136.6 273.4 140.2 278.0 145.8 C282.6 151.4 287.3 157.6 293.2 166.1 C299.0 174.7 306.7 186.7 312.9 197.3 C319.0 207.9 325.6 220.5 329.9 229.9 C334.3 239.2 337.3 248.3 339.0 253.3 C340.8 258.4 340.4 258.5 340.6 260.2 C340.8 262.0 340.7 263.1 340.4 264.0 C340.2 264.9 339.4 265.3 339.1 265.6"/>
    <path d="M195.8 278.0 C195.8 273.8 195.1 273.0 195.9 252.7 C196.7 232.4 199.5 182.3 200.5 156.1 C201.5 130.0 201.8 105.8 202.0 95.7"/>
    <path d="M195.8 278.0 C206.9 278.3 250.9 280.6 262.3 279.8 C273.7 279.0 263.4 278.0 264.3 273.2 C265.3 268.5 266.8 261.8 267.8 251.3 C268.8 240.8 270.1 216.9 270.6 210.0"/>
    <path d="M195.8 278.0 C186.0 278.2 147.2 280.4 137.1 279.0 C126.9 277.6 135.8 275.4 134.9 269.8 C133.9 264.2 132.4 255.6 131.4 245.5 C130.5 235.4 129.6 215.3 129.2 209.3"/>
    <path d="M228.5 74.5 C228.9 73.8 230.5 71.9 231.2 69.9 C231.8 67.8 232.3 65.0 232.4 62.5 C232.5 60.0 232.2 57.1 231.6 54.7 C231.1 52.2 230.0 49.5 229.1 47.6 C228.2 45.7 227.6 44.8 226.3 43.4 C225.0 42.0 223.3 40.3 221.4 39.2 C219.6 38.0 217.4 37.0 215.2 36.3 C213.0 35.7 211.1 35.2 208.5 35.1 C205.8 35.0 202.4 35.1 199.5 35.6 C196.6 36.0 193.7 36.9 191.1 37.9 C188.4 38.9 186.3 39.8 183.7 41.4 C181.1 42.9 177.7 45.2 175.6 47.0 C173.5 48.8 172.3 50.2 171.0 52.0 C169.8 53.8 168.8 55.7 168.2 57.8 C167.6 59.9 167.5 62.7 167.6 64.7 C167.7 66.6 168.8 68.7 169.1 69.5"/>
    <path d="M129.2 209.3 C128.9 209.4 133.2 199.4 127.7 210.1 C122.2 220.8 101.6 262.8 96.2 273.5 C90.8 284.3 95.9 274.4 95.4 274.6 C94.9 274.9 93.7 274.9 93.4 274.9"/>
    <path d="M306.6 275.6 C306.1 275.5 309.7 285.6 304.0 274.8 C298.2 264.0 277.7 221.6 272.2 210.8 C266.6 200.0 270.8 210.1 270.6 210.0"/>
    <path d="M138.5 252.9 L149.3 187.1"/>
    <path d="M261.2 253.0 L250.4 187.7"/>
    <path d="M256.5 160.8 C258.4 165.4 265.6 181.8 267.8 188.2 C270.0 194.6 269.4 195.5 269.8 199.2 C270.3 202.8 270.5 208.2 270.6 210.0"/>
    <path d="M129.2 209.3 C129.4 207.0 129.8 199.4 130.3 195.6 C130.9 191.7 130.2 192.2 132.4 186.3 C134.5 180.4 141.5 164.5 143.3 160.2"/>
    <path d="M60.7 264.9 C60.6 265.7 59.8 268.5 60.0 269.8 C60.2 271.1 59.1 271.1 61.9 272.6 C64.7 274.1 72.5 277.2 76.8 278.5 C81.0 279.9 84.7 281.2 87.4 280.6 C90.2 280.0 92.4 275.9 93.4 274.9"/>
    <path d="M220.3 80.5 C218.7 80.9 214.0 82.6 210.8 83.2 C207.7 83.7 204.3 83.8 201.4 83.8 C198.5 83.7 196.9 83.7 193.4 82.8 C190.0 82.0 182.8 79.5 180.6 78.8"/>
    <path d="M339.1 265.6 C339.2 266.4 339.9 269.6 339.7 270.9 C339.4 272.2 340.7 271.8 337.9 273.2 C335.2 274.6 327.3 277.8 323.1 279.2 C318.8 280.5 315.2 281.8 312.4 281.2 C309.7 280.6 307.5 276.6 306.6 275.6"/>
    <path d="M93.4 274.9 L60.7 264.9"/>
    <path d="M306.6 275.6 C308.8 274.8 314.8 272.4 320.2 270.7 C325.7 269.0 336.0 266.4 339.1 265.6"/>
    <path d="M220.3 80.5 C220.0 81.8 219.2 86.6 218.6 88.5 C218.1 90.3 218.2 90.6 216.9 91.6 C215.6 92.6 213.4 93.9 211.0 94.6 C208.5 95.3 203.5 95.5 202.0 95.7"/>
    <path d="M202.0 95.7 C201.1 95.6 198.3 95.7 196.2 95.1 C194.2 94.4 192.1 93.6 190.0 91.9 C187.9 90.2 185.3 87.1 183.7 84.9 C182.2 82.7 181.1 79.8 180.6 78.8"/>
    <path d="M180.6 78.8 L169.1 69.5"/>
    <path d="M220.3 80.5 C221.5 79.5 226.0 75.5 227.4 74.5 C228.8 73.6 228.3 74.5 228.5 74.5"/>
  </g>
  <g fill="none" stroke="#fff" stroke-width="1.2" stroke-linecap="square" opacity="0.55">
    <path d="M36 108 L36 280 M30 108 L42 108 M30 280 L42 280"/>
    <path d="M129 209 L254 209 M129 203 L129 215 M254 203 L254 215"/>
    <path d="M258.5 90.8 L364.7 252.4 M254.4 93.6 L262.7 88.1 M360.6 255.2 L368.9 249.7"/>
  </g>
  <g fill="#fff" class="figure__letters">
    <text x="26"  y="200" text-anchor="end">A</text>
    <text x="168" y="201" text-anchor="middle">B</text>
    <text x="323" y="164" text-anchor="middle">C</text>
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
                 'circumference. Tolerance ±2 cm. If in doubt, take the smaller size.'),
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


# Headless Chromium paints 87 CSS pixels less than --window-size asks for, and
# says so itself: window.innerHeight is 813 for a window of 900. The screenshot
# is still the full window, the strip below is simply never painted — black on
# black, invisible, until a line of text lands in it and disappears. So the page
# is laid out against the height that actually paints.
VIEWPORT_LOSS = 87


def write(path, w, h, pad, measure, sizes, main, note):
    s = (PAGE.replace('__FONT__', FONT).replace('__W__', str(w))
             .replace('__H__', str(h - VIEWPORT_LOSS))
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
