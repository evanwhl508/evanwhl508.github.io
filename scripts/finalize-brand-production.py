#!/usr/bin/env python3
"""Package exported assets and maintain old temporary URLs without touching theme 1."""
from pathlib import Path
import shutil,zipfile,json
ROOT=Path(__file__).resolve().parents[1];B=ROOT/'public/brand';L=ROOT/'logo'
for name in ['InterVariable.woff2','Inter-LICENSE.txt']:shutil.copyfile(ROOT/'assets/fonts'/name,B/'source/fonts'/name)
# Archive the former temporary production set once; retain all exploration folders.
archive=L/'archive-provisional'
if not archive.exists():
    archive.mkdir()
    for p in L.iterdir():
        if p.is_file() and (p.name.startswith('covan-') or p.name.startswith('favicon') or p.name.startswith('apple-') or p.name.startswith('social-card')):shutil.copyfile(p,archive/p.name)
for old,new in [('dark','primary'),('light','light'),('white','white'),('navy','navy')]:
    shutil.copyfile(B/f'logo/covan-mark-{new}.svg',L/f'covan-mark-{old}.svg')
    for layout in ['horizontal','stacked']:
        color='monochrome' if old=='navy' else old
        shutil.copyfile(B/f'logo/covan-logo-{layout}-{color}.svg',L/f'covan-logo-{layout}-{old}.svg')
for size in [64,128,256,512]:
    for name,suffix in [('primary',''),('light','-light')]:shutil.copyfile(B/f'png/covan-mark-{name}-{size}.png',L/f'covan-mark-{size}{suffix}.png')
for size in [16,32]:shutil.copyfile(B/f'favicon/favicon-{size}.png',L/f'favicon-{size}.png')
shutil.copyfile(B/'favicon/apple-touch-icon.png',L/'apple-touch-icon.png')
for ext in ['svg','png']:shutil.copyfile(B/f'social/covan-og-brand.{ext}',L/f'social-card.{ext}')
shutil.copyfile(ROOT/'docs/brand-production.md',B/'README.md')
with zipfile.ZipFile(B/'covan-brand-assets.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(B.rglob('*')):
        if p.is_file() and p.suffix!='.zip':z.write(p,'covan-brand/'+str(p.relative_to(B)))
print('Packaged identity kit; legacy URLs updated, theme 1 assets untouched.')
