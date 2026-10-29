#!/usr/bin/env python3
"""Validate Confluence C construction, native raster proofs and accent area."""
from pathlib import Path
import json,math,xml.etree.ElementTree as ET,zipfile,hashlib
from PIL import Image,ImageChops
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'logo/confluence';NS={'s':'http://www.w3.org/2000/svg'}
m=json.loads((BASE/'manifest.json').read_text());assert len(m['variants'])==4
COLORS=('white','navy','black','primary','light','origin');SIZES=(16,24,32,64,512)
def component(pixels,start):
    pending=[start];seen={start}
    while pending:
        x,y=pending.pop()
        for q in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if q in pixels and q not in seen:seen.add(q);pending.append(q)
    return seen
def edge_difference(a,b):
    difference=ImageChops.difference(a,b);points=[(x,y) for y in range(a.height) for x in range(a.width) if difference.getpixel((x,y))]
    # Chromium coverage can differ on isolated boundary pixels at 512px.
    # Native proofs must match exactly. Interior shape changes never pass.
    if points:
        assert a.width==512 and len(points)<=2 and difference.getextrema()[1]<=64,(a.size,len(points),difference.getextrema())
        for x,y in points:
            assert any(a.getpixel((xx,yy))<255 for xx in range(max(0,x-1),min(a.width,x+2)) for yy in range(max(0,y-1),min(a.height,y+2)))
    return {'changed_edge_pixels':len(points),'max_alpha_difference':difference.getextrema()[1]}
results=[];count=0
for v in m['variants']:
    folder=BASE/v['id'];raster={};areas={}
    assert v['reference']['id'] in ('01','04')
    assert v['merged'].count('A')==4 and v['merged'].count('C')==2
    for name,key in [('origin-a','origin_a'),('origin-b','origin_b')]:
        assert ET.parse(folder/f'{name}.svg').getroot().find('s:path',NS).get('d')==v[key]
    for c in (v['circles'][0],v['circles'][2]):assert abs(c['cx']-c['r']-v['outer_join'][0])<1e-8
    for c in (v['circles'][1],v['circles'][3]):assert abs(math.hypot(v['inner_join'][0]-c['cx'],v['inner_join'][1]-c['cy'])-c['r'])<1e-8
    for color in COLORS:
        root=ET.parse(folder/f'mark-{color}.svg').getroot();assert root.find('s:path',NS).get('d')==v['merged']
        for size in SIZES:
            im=Image.open(folder/f'mark-{color}-{size}.png');assert im.mode=='RGBA' and im.size==(size,size)
            a=im.getchannel('A');assert a.getextrema()==(0,255)
            x0,y0,x1,y1=a.getbbox();assert 0<x0<x1<size and 0<y0<y1<size
            if color in ('white','navy','black'):
                rgb={'white':(255,255,255),'navy':(8,17,31),'black':(0,0,0)}[color]
                assert all(p[:3]==rgb for p in im.get_flattened_data() if p[3]==255)
            if size<=64:
                ink={(x,y) for y in range(size) for x in range(size) if a.getpixel((x,y))>=128};assert component(ink,next(iter(ink)))==ink
                clear={(x,y) for y in range(size) for x in range(size) if a.getpixel((x,y))<128};seed=(round(size*.6),size//2)
                assert seed in clear and any(x==size-1 for x,y in component(clear,seed))
            if color!='white':
                white=Image.open(folder/f'mark-white-{size}.png').getchannel('A');raster[f'{color}-{size}']=edge_difference(white,a)
            count+=1
        if color in ('primary','origin'):
            im=Image.open(folder/f'mark-{color}-512.png')
            pixels=list(im.get_flattened_data());area=sum(p[3] for p in pixels)
            accent=sum(p[3]*max(0,min(1,(244-p[0])/187)) for p in pixels)/area*100
            assert 12<=accent<=18,(v['id'],color,accent)
            areas[color]=round(accent,2)
    union=Image.open(ROOT/f'output/playwright/confluence-union-{v["id"]}.png').getchannel('A')
    white=Image.open(folder/'mark-white-512.png').getchannel('A');union_result=edge_difference(white,union)
    results.append({'id':v['id'],'aqua_filled_area_percent':areas,'identical_svg_contour_all_colorways':True,'native_single_component_and_open_counter':True,'union_raster':union_result,'colorway_edge_differences':{k:v for k,v in raster.items() if v['changed_edge_pixels']}})
report={'status':'passed','refinements':4,'pngs_checked':count,'native_sizes':[16,24,32,64],'large_proof':512,'variants':results,'note':'Native alpha masks match exactly. Any 512px edge-coverage differences are listed. These checks do not establish beauty, memorability or trademark distinctiveness.'}
(BASE/'checks.json').write_text(json.dumps(report,indent=2)+'\n')
with zipfile.ZipFile(BASE/'covan-confluence-c.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(BASE.rglob('*')):
        if p.is_file() and p.suffix in ('.svg','.png','.json'):z.write(p,Path('covan-confluence-c')/p.relative_to(BASE))
    for file in ('confluence-geometry.py','two-origin-geometry.py','build-confluence.py','export-confluence.js','check-confluence.py'):
        z.write(ROOT/'scripts'/file,Path('covan-confluence-c/source')/file)
    z.write(ROOT/'docs/logo-confluence.md','covan-confluence-c/BRIEF.md')
    z.write(ROOT/'assets/fonts/Inter-LICENSE.txt','covan-confluence-c/Inter-LICENSE.txt')
    z.writestr('covan-confluence-c/README.txt','Four Confluence C refinements; none selected. Start with comparison-white.png, comparison-primary.png and comparison-light.png. Each numbered folder has pure white/navy/black, two-color dark/light, one alternate origin-color treatment, construction geometry, separate source ribbons, outlined wordmark lockups and transparent 16/24/32/64/512px PNGs. Source scripts use the original repository paths; run them from the project, as described in BRIEF.md.\n')
print(json.dumps({'status':'passed','refinements':4,'pngs_checked':count,'aqua_area_percent':[{v['id']:v['aqua_filled_area_percent']} for v in results]},indent=2))
