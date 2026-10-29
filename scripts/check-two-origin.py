#!/usr/bin/env python3
"""Check exact two-ribbon union, monochrome native proofs and package the review."""
from pathlib import Path
import json,math,xml.etree.ElementTree as ET,zipfile
from PIL import Image,ImageChops
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'logo/two-origin';NS={'s':'http://www.w3.org/2000/svg'}
m=json.loads((BASE/'manifest.json').read_text());assert len(m['variants'])==5
checked=0;results=[]
def connected(pixels,start):
    pending=[start];seen={start}
    while pending:
        x,y=pending.pop()
        for q in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if q in pixels and q not in seen:seen.add(q);pending.append(q)
    return seen
for v in m['variants']:
    ident=v['id'];folder=BASE/ident
    outer,inner=v['outer_join'],v['inner_join']
    # The two outer circles share their leftmost point and vertical tangent.
    for c in (v['circles'][0],v['circles'][2]):assert abs((c['cx']-c['r'])-outer[0])<1e-8 and c['cy']==outer[1]
    for c in (v['circles'][1],v['circles'][3]):assert abs(math.hypot(inner[0]-c['cx'],inner[1]-c['cy'])-c['r'])<1e-8
    for color,rgb in [('white',(255,255,255)),('navy',(8,17,31))]:
        mark=ET.parse(folder/f'mark-{color}.svg').getroot()
        paths=mark.findall('.//s:path',NS);assert len(paths)==1 and paths[0].get('d')==v['merged']
        assert v['merged'].count('A')==4 and not any(command in v['merged'] for command in ('C','Q')), 'Unexpected non-circular mark geometry'
        for name,key in [('origin-a','origin_a'),('origin-b','origin_b')]:
            source=ET.parse(folder/f'{name}-{color}.svg').getroot();assert source.find('.//s:path',NS).get('d')==v[key]
        for size in (16,24,32,64,512):
            im=Image.open(folder/f'mark-{color}-{size}.png');assert im.mode=='RGBA' and im.size==(size,size)
            alpha=im.getchannel('A');assert alpha.getextrema()==(0,255)
            x0,y0,x1,y1=alpha.getbbox();assert 0<x0<x1<size and 0<y0<y1<size
            assert all(p[:3]==rgb for p in im.get_flattened_data() if p[3]==255), 'Accent color in monochrome proof'
            if size<=64:
                ink={(x,y) for y in range(size) for x in range(size) if alpha.getpixel((x,y))>=128}
                assert connected(ink,next(iter(ink)))==ink, 'Broken raster silhouette'
                clear={(x,y) for y in range(size) for x in range(size) if alpha.getpixel((x,y))<128}
                seed=(round(size*.6),size//2);assert seed in clear
                assert any(x==size-1 for x,y in connected(clear,seed)), 'Counter is closed'
            checked+=1
    edge_differences={}
    for size in (16,24,32,64,512):
        white=Image.open(folder/f'mark-white-{size}.png').getchannel('A');navy=Image.open(folder/f'mark-navy-{size}.png').getchannel('A')
        difference=ImageChops.difference(white,navy);maximum=difference.getextrema()[1]
        changed=[(x,y) for y in range(size) for x in range(size) if difference.getpixel((x,y))]
        # Chromium uses different coverage at one terminal-edge pixel at 512px.
        # Native-size silhouettes must match exactly; no interior differences pass.
        if changed:
            assert size==512 and len(changed)<=1 and maximum<=64,(ident,size,len(changed),maximum)
            for x,y in changed:
                assert any(white.getpixel((xx,yy))<255 for xx in range(max(0,x-1),min(size,x+2)) for yy in range(max(0,y-1),min(size,y+2)))
        edge_differences[str(size)]={'pixels':len(changed),'max_alpha_delta':maximum}
    union=Image.open(ROOT/f'output/playwright/two-origin-union-{ident}.png').getchannel('A');merged=Image.open(folder/'mark-white-512.png').getchannel('A')
    assert ImageChops.difference(union,merged).getextrema()[1]==0,'Merged mark differs from the two actual origins'
    results.append({'id':ident,'two_origin_union_matches_exactly':True,'single_connected_ink_component_at_native_sizes':True,'open_counter_at_native_sizes':True,'monochrome_svg_geometry_identical':True,'raster_edge_differences':edge_differences})
report={'status':'passed','concepts':1,'variants':5,'pngs_checked':checked,'sizes':[16,24,32,64,512],'variants_checked':results,'limitation':'Geometric/raster checks verify construction and legibility conditions, not subjective beauty or trademark distinctiveness.'}
(BASE/'checks.json').write_text(json.dumps(report,indent=2)+'\n')
with zipfile.ZipFile(BASE/'covan-two-origin-c.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(BASE.rglob('*')):
        if p.is_file() and p.suffix in ('.svg','.png','.json'):z.write(p,Path('covan-two-origin-c')/p.relative_to(BASE))
    z.write(ROOT/'docs/logo-two-origin.md','covan-two-origin-c/BRIEF.md')
    z.write(ROOT/'scripts/two-origin-geometry.py','covan-two-origin-c/geometry.py')
    z.write(ROOT/'assets/fonts/Inter-LICENSE.txt','covan-two-origin-c/Inter-LICENSE.txt')
    z.writestr('covan-two-origin-c/README.txt','Five variations of one Two-Origin C. Start with comparison-white.png or comparison-navy.png. Each numbered folder contains two independent origin ribbons, their exact merged silhouette, actual circular construction grid, supporting wordmark lockups and native transparent monochrome PNGs. Geometry is independent of fonts; the wordmark uses outlined Inter. No variant or color stage is approved.\n')
print(json.dumps({'status':'passed','concepts':1,'variants':5,'pngs_checked':checked,'exact_union_checks':5,'native_ink_connected':True,'native_counter_open':True},indent=2))
