#!/bin/sh
# Render the size charts to PNG.
#
# The layouts are plain HTML with the Michroma woff2 inlined as base64, so
# the rendered file carries the shop's own typeface with no font install and
# no network. Chromium ships with the session; --force-device-scale-factor=2
# gives a 2x file, which is what Shopify wants for a product image.
#
# After changing a number, re-run this and re-upload. Both layouts must keep
# their content inside the canvas — a row that overflows is simply cut off,
# so check the bottom line of the picture before uploading.
set -e

HERE=$(cd "$(dirname "$0")" && pwd)
OUT=${1:-"$HERE/out"}
CHROME=${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}

mkdir -p "$OUT"

"$CHROME" --headless --no-sandbox --disable-gpu --hide-scrollbars \
  --force-device-scale-factor=2 --window-size=1200,1500 \
  --screenshot="$OUT/bacto-sizechart-portrait.png" "file://$HERE/portrait.html"

"$CHROME" --headless --no-sandbox --disable-gpu --hide-scrollbars \
  --force-device-scale-factor=2 --window-size=1600,900 \
  --screenshot="$OUT/bacto-sizechart-wide.png" "file://$HERE/wide.html"

echo "geschrieben nach $OUT"
