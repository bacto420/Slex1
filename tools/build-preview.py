#!/usr/bin/env python3
"""Derive the pre-drop preview theme from the main one.

The preview is the same theme with the shop closed: no products, no
collections, no cart, no blog. Everything that would sell something answers
with the Coming soon section instead — a store with no products still serves
/products/... and /cart, and a bare Shopify error there reads as broken
rather than as not yet open.

Deriving it rather than keeping a second copy means the two never drift: fix
the footer once and both themes get it.

    python3 tools/build-preview.py [output.zip]
"""

import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
PREVIEW = ROOT / 'preview'

THEME_DIRS = ('assets', 'config', 'layout', 'locales', 'sections', 'snippets', 'templates')

# Sections that only exist to sell. Their templates point at coming-soon, so
# nothing references them any more.
DROP_SECTIONS = (
    'home-split.liquid',
    'main-product.liquid',
    'main-collection.liquid',
    'main-list-collections.liquid',
    'main-cart.liquid',
    'main-search.liquid',
    'main-blog-posts.liquid',
    'main-article.liquid',
    'product-bundle.liquid',
)


def build(out_zip: pathlib.Path) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        stage = pathlib.Path(tmp) / 'theme'
        stage.mkdir()

        for name in THEME_DIRS:
            shutil.copytree(ROOT / name, stage / name)

        for name in DROP_SECTIONS:
            (stage / 'sections' / name).unlink(missing_ok=True)

        shutil.copy(PREVIEW / 'sections' / 'coming-soon.liquid', stage / 'sections')

        for tpl in sorted((PREVIEW / 'templates').glob('*.json')):
            shutil.copy(tpl, stage / 'templates')

        shutil.copy(PREVIEW / 'config' / 'settings_data.json', stage / 'config')

        css = stage / 'assets' / 'base.css'
        css.write_text(css.read_text() + (PREVIEW / 'preview.css').read_text())

        # The bundle lives on the home and product templates, both replaced.
        # Nothing should still point at a section that is no longer shipped.
        shipped = {p.stem for p in (stage / 'sections').glob('*.liquid')}
        for tpl in sorted((stage / 'templates').glob('*.json')):
            data = json.loads(tpl.read_text())
            for key, section in data.get('sections', {}).items():
                if section.get('type') not in shipped:
                    raise SystemExit(
                        '%s references missing section "%s"' % (tpl.name, section.get('type'))
                    )

        if out_zip.exists():
            out_zip.unlink()
        subprocess.run(
            ['zip', '-q', '-r', str(out_zip), *THEME_DIRS, '-x', '*.DS_Store'],
            cwd=stage, check=True,
        )
        print('wrote %s' % out_zip)


if __name__ == '__main__':
    target = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'bacto-preview-theme.zip'
    build(target.resolve())
