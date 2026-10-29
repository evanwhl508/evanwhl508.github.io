#!/usr/bin/env python3
"""Primary-scale output QA. No favicon-readability acceptance gate."""
from pathlib import Path
import json,xml.etree.ElementTree as ET,zipfile
from PIL import Image,ImageChops
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'logo/confluence-hybrid';NS={'s':'http://www.w3.org/2000/svg'}
m=json.loads((OUT/'manifest.json').read_text());assert len(m['variants'])==3 and m['micro_created'] is False
assert len({v['merged'] for v in m['variants']})==3
COLORS=('white','navy','black','primary','light');SIZES=(16,24,64,128,256)
def component(pixels,start):
 pending=[start];seen={start}
 while pending:
  x,y=pending.pop()
  for q in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
   if q in pixels and q not in seen:seen.add(q);pending.append(q)
 return seen
results=[];count=0
for v in m['variants']:
 folder=OUT/v['id'];edge_differences={}
 for color in COLORS:
  assert ET.parse(folder/f'mark-{color}.svg').getroot().find('s:path',NS).get('d')==v['merged']
  for size in SIZES:
   im=Image.open(folder/f'mark-{color}-{size}.png');assert im.size==(size,size) and im.mode=='RGBA'
   a=im.getchannel('A');x0,y0,x1,y1=a.getbbox();assert 0<x0<x1<size and 0<y0<y1<size
   if color in ('white','navy','black'):
    rgb={'white':(255,255,255),'navy':(8,17,31),'black':(0,0,0)}[color];assert all(p[:3]==rgb for p in im.get_flattened_data() if p[3]==255)
   if size in m['primary_sizes']:
    ink={(x,y) for y in range(size) for x in range(size) if a.getpixel((x,y))>=128};assert component(ink,next(iter(ink)))==ink
    clear={(x,y) for y in range(size) for x in range(size) if a.getpixel((x,y))<128};seed=(round(size*.58),size//2);assert seed in clear and any(x==size-1 for x,y in component(clear,seed))
    white=Image.open(folder/f'mark-white-{size}.png').getchannel('A');diff=ImageChops.difference(a,white)
    changed=[(x,y) for y in range(size) for x in range(size) if diff.getpixel((x,y))]
    if changed:
     assert len(changed)<=2 and diff.getextrema()[1]<=64
     for x,y in changed:assert any(white.getpixel((xx,yy))<255 for xx in range(max(0,x-1),min(size,x+2)) for yy in range(max(0,y-1),min(size,y+2)))
     edge_differences[f'{color}-{size}']={'pixels':len(changed),'max_alpha_delta':diff.getextrema()[1]}
   count+=1
 px=list(Image.open(folder/'mark-primary-256.png').get_flattened_data());area=sum(p[3] for p in px);pct=100*sum(p[3]*max(0,min(1,(244-p[0])/187)) for p in px)/area
 assert 6<=pct<=10,(v['id'],pct)
 results.append({'id':v['id'],'aqua_filled_area_percent':round(pct,3),'primary_counter_open_and_ink_connected':True,'colorway_svg_contour_identical':True,'raster_edge_differences':edge_differences})
report={'status':'passed','directions':3,'pngs_checked':count,'primary_sizes':[64,128,256],'secondary_sizes':[16,24],'secondary_legibility_not_an_acceptance_gate':True,'micro_created':False,'variants':results,'note':'Primary raster checks do not determine beauty or trademark distinctiveness. A separate micro design follows selection.'}
(OUT/'checks.json').write_text(json.dumps(report,indent=2)+'\n')
with zipfile.ZipFile(OUT/'covan-hybrid-studies.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(OUT.rglob('*')):
  if p.is_file() and p.suffix in ('.svg','.png','.json'):z.write(p,Path('covan-hybrid-studies')/p.relative_to(OUT))
 for name in ('confluence-hybrid-geometry.py','confluence-primary-geometry.py','confluence-flow-geometry.py','build-confluence-hybrid.py','build-confluence-flow.py','export-confluence-hybrid.js','check-confluence-hybrid.py'):z.write(ROOT/'scripts'/name,Path('covan-hybrid-studies/source')/name)
 z.write(ROOT/'docs/logo-confluence-hybrid.md','covan-hybrid-studies/BRIEF.md');z.write(ROOT/'assets/fonts/Inter-LICENSE.txt','covan-hybrid-studies/Inter-LICENSE.txt')
 z.writestr('covan-hybrid-studies/README.txt','Three hybrid Confluence C studies: H1 Elegant Hybrid, H2 Signature Hybrid, H3 Structured Hybrid. Based on 01 Elegant Flow with restrained 03 personality and limited 02 structure. Evaluate 256/128/64px and navbar lockups. 16/24px files are direct master reductions for secondary reference, NOT Micro C designs or approved favicons. A separate Micro C follows primary selection. Source scripts require the repository paths described in BRIEF.md.\n')
print(json.dumps({'status':'passed','primary_sizes':[64,128,256],'micro_created':False,'pngs_checked':count,'aqua_percent':{v['id']:v['aqua_filled_area_percent'] for v in results}},indent=2))
