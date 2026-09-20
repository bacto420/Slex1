#!/bin/sh
# Build the layouts, then render each to PNG.
#
# Chromium ships with the session; --force-device-scale-factor=2 gives a 2x
# file, which is what Shopify wants for a product image.
#
# Numbers and drawings live in build.py — edit there, never in the generated
# HTML, which is overwritten on every run. Check the bottom line of each
# picture afterwards: content that overflows the canvas is cropped silently.
set -e

HERE=$(cd "$(dirname "$0")" && pwd)
OUT=${1:-"$HERE/out"}
CHROME=${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}

python3 "$HERE/build.py"
mkdir -p "$OUT"

for garment in longsleeve jacket; do
  "$CHROME" --headless --no-sandbox --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=2 --window-size=1200,1500 \
    --screenshot="$OUT/bacto-size-chart-$garment-portrait.png" \
    "file://$HERE/$garment-portrait.html"

  "$CHROME" --headless --no-sandbox --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=2 --window-size=1600,900 \
    --screenshot="$OUT/bacto-size-chart-$garment-wide.png" \
    "file://$HERE/$garment-wide.html"
done

echo "geschrieben nach $OUT"
