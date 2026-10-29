#!/usr/bin/env python3
"""Check monochrome proofs, exact A extraction and package the four studies."""
from pathlib import Path
import json, xml.etree.ElementTree as ET, zipfile
from PIL import Image, ImageChops
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'logo/identity';NS={'s':'http://www.w3.org/2000/svg'}
manifest=json.loads((BASE/'manifest.json').read_text());assert manifest['directions']==2 and len(manifest['variants'])==4
checked=0
for v in manifest['variants']:
    folder=BASE/v['id']
    for color,rgb in [('white',(255,255,255)),('navy',(8,17,31))]:
        for kind in ('mark','wordmark','identity'):
            svg=ET.parse(folder/f'{kind}-{color}.svg').getroot()
            assert not svg.findall('.//s:text',NS), 'Identity lettering must be outlined'
            fills={e.get('fill') for e in svg.iter() if e.get('fill')}
            assert fills=={'#FFFFFF' if color=='white' else '#08111F'},fills
        if v['direction']=='A':
            mark=ET.parse(folder/f'mark-{color}.svg').getroot().find('.//s:path',NS).get('d')
            word=ET.parse(folder/f'wordmark-{color}.svg').getroot().find('.//s:path[@data-letter="C"]',NS).get('d')
            assert mark==word==v['c'], 'A mark is not the exact first wordmark glyph'
        for size in (16,24,32,64,512):
            path=folder/f'mark-{color}-{size}.png';im=Image.open(path)
            assert im.mode=='RGBA' and im.size==(size,size),(path,im.size)
            alpha=im.getchannel('A');assert alpha.getextrema()==(0,255)
            x0,y0,x1,y1=alpha.getbbox();assert 0<x0<x1<size and 0<y0<y1<size,(path,'clipped mark')
            assert all(p[:3]==rgb for p in im.get_flattened_data() if p[3]==255),(path,'not monochrome')
            checked+=1
        for scale in (1,2):
            im=Image.open(folder/f'identity-{color}-{scale}x.png');alpha=im.getchannel('A');box=alpha.getbbox()
            assert im.height==v['navbar_height']*scale
            assert box and box[0]>0 and box[1]>0 and box[2]<im.width and box[3]<im.height,(v['id'],scale,'clipped identity')
            assert all(p[:3]==rgb for p in im.get_flattened_data() if p[3]==255)
            checked+=1
    for size in (16,24,32,64,512):
        a=Image.open(folder/f'mark-white-{size}.png').getchannel('A');b=Image.open(folder/f'mark-navy-{size}.png').getchannel('A')
        assert ImageChops.difference(a,b).getextrema()[1]<=1
result={'status':'passed','directions':2,'refinements':4,'pngs_checked':checked,'a_mark_matches_wordmark_C_exactly':True,'monochrome_only':True,'sizes':[16,24,32,64,512],'identities_unclipped':True}
(BASE/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
with zipfile.ZipFile(BASE/'covan-monochrome-identities.zip','w',zipfile.ZIP_DEFLATED) as archive:
    for p in sorted(BASE.rglob('*')):
        if p.is_file() and p.suffix in ('.svg','.png','.json'):
            archive.write(p,Path('covan-monochrome-identities')/p.relative_to(BASE))
    archive.write(ROOT/'docs/logo-identity.md','covan-monochrome-identities/BRIEF.md')
    archive.write(ROOT/'assets/fonts/Inter-LICENSE.txt','covan-monochrome-identities/Inter-LICENSE.txt')
    archive.writestr('covan-monochrome-identities/README.txt','Covan Labs: two directions, two monochrome refinements each. Start with comparison-white.png or comparison-navy.png. A1/A2: customized wordmarks; standalone C is the exact first glyph. B1/B2: continuous C marks with consistent supporting type. SVG files are outlined; PNGs are transparent. Geometry is unapproved. No aqua has been introduced.\n')
print(json.dumps(result,indent=2))
