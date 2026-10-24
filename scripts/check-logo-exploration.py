#!/usr/bin/env python3
"""Validate deliverables, measure accent coverage, and package the unselected studies."""
from pathlib import Path
from PIL import Image, ImageChops
import json, xml.etree.ElementTree as ET, zipfile
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'logo/exploration'
manifest=json.loads((BASE/'manifest.json').read_text())
assert len(manifest['concepts'])==10
sizes=[16,24,32,64,512];palettes=['dark','light','white','navy'];count=0
measurements={'method':'Alpha-weighted 512px raster estimate; red-channel interpolation from silver to aqua; exact 1x browser exports','sizes':sizes,'concepts':{}}
for concept in manifest['concepts']:
    ident=concept['id'];directory=BASE/ident
    assert len(concept['scores'])==10 and all(1<=v<=10 for v in concept['scores'].values())
    page=(directory/'index.html').read_text()
    assert '<details class="meaning" id="meaning">' in page and '<details open' not in page
    for palette in palettes:
        for prefix in ['mark','lockup']:
            root=ET.parse(directory/f'{prefix}-{palette}.svg').getroot()
            assert root.tag.endswith('svg')
            assert not root.findall('.//{http://www.w3.org/2000/svg}text'), 'Logo wordmarks must be outlines'
        for size in sizes:
            png=directory/f'mark-{palette}-{size}.png';im=Image.open(png)
            assert im.mode=='RGBA' and im.size==(size,size),(png,im.mode,im.size)
            alpha=im.getchannel('A');assert alpha.getextrema()==(0,255),(png,'transparent/opaque pixels missing')
            box=alpha.getbbox();assert box and box[0]>0 and box[1]>0 and box[2]<size and box[3]<size,(png,'clipped mark')
            if palette in ('white','navy'):
                target=(255,255,255) if palette=='white' else (8,17,31)
                opaque=[rgb[:3] for rgb in im.get_flattened_data() if rgb[3]==255]
                assert all(color==target for color in opaque),(png,'non-monochrome')
            count+=1
    diffs={}
    for size in sizes:
        ref=Image.open(directory/f'mark-white-{size}.png').getchannel('A')
        for palette in ('dark','light','navy'):
            actual=Image.open(directory/f'mark-{palette}-{size}.png').getchannel('A')
            diff=ImageChops.difference(ref,actual)
            maximum=diff.getextrema()[1]
            assert maximum<=2,(ident,palette,size,'silhouette differs',maximum)
            diffs[f'{palette}-{size}']=maximum
    pixels=list(Image.open(directory/'mark-dark-512.png').get_flattened_data())
    area=sum(px[3]/255 for px in pixels)
    accent=sum((px[3]/255)*max(0,min(1,(244-px[0])/187)) for px in pixels)
    percentage=100*accent/area
    assert 10<=percentage<=20,(ident,percentage,'aqua outside latest target')
    measurements['concepts'][ident]={'name':concept['name'],'aqua_area_percent':round(percentage,2),'filled_pixel_area_at_512':round(area,2),'max_alpha_difference_from_white':max(diffs.values()),'sizes_verified':sizes,'four_colorways_verified':True}
measurements['transparent_png_count']=count
(BASE/'measurements.json').write_text(json.dumps(measurements,indent=2)+'\n')
# Package assets and the complete rationale; the website review remains available at its local path.
with zipfile.ZipFile(BASE/'covan-logo-exploration.zip','w',zipfile.ZIP_DEFLATED) as archive:
    for p in sorted(BASE.rglob('*')):
        if p.is_file() and p.suffix in ('.svg','.png','.json'):
            archive.write(p,Path('covan-logo-exploration')/p.relative_to(BASE))
    archive.write(ROOT/'docs/logo-exploration.md','covan-logo-exploration/BRIEF.md')
    archive.writestr('covan-logo-exploration/README.txt','Covan Labs: ten unselected concepts. Start with contact-sheet-dark.png before reading manifest.json. Each numbered folder has marks, outlined wordmarks, actual-contour diagrams and 16/24/32/64/512px transparent PNGs in four colorways. manifest.json contains each story, rationale and subjective assessment. measurements.json records the export checks. No concept is selected. No trademark clearance is claimed.\n')
print(json.dumps({'concepts':10,'transparent_pngs':count,'aqua_percent':{k:v['aqua_area_percent'] for k,v in measurements['concepts'].items()},'archive':str(BASE/'covan-logo-exploration.zip')},indent=2))
