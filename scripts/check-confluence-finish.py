#!/usr/bin/env python3
"""Validate only the requested finishing deltas and their native proofs."""
from pathlib import Path
import json,runpy,xml.etree.ElementTree as ET,zipfile
from PIL import Image,ImageChops
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'logo/confluence-finish';NS={'s':'http://www.w3.org/2000/svg'}
m=json.loads((OUT/'manifest.json').read_text());vs=m['variants'];assert [v['id'] for v in vs]==['a1','a2','a3']
old=json.loads((ROOT/'logo/confluence-flow/manifest.json').read_text())['variants'][0]
for k in ('merged','origin_a','origin_b','confluence'):assert vs[0][k]==old[k]
assert vs[1]['merged']==vs[0]['merged']
# Exact 2.5% x-scaling preserves every lower-return control point; only upper cap changes.
for j in range(1,8):
 for a,b in zip(vs[1]['segments'][j],vs[2]['segments'][j]):assert abs(b[0]-(47.5+(a[0]-47.5)*.975))<1e-8 and b[1]==a[1]
for seam in ('upper_seam','lower_seam'):
 for a,b in zip(vs[1][seam],vs[2][seam]):assert abs(b[0]-(47.5+(a[0]-47.5)*.975))<1e-8 and b[1]==a[1]
assert vs[2]['horizontal_scale']==.975
assert vs[2]['segments'][9][1][1]<vs[1]['segments'][9][1][1]
def connected(pixels,start):
 pending=[start];seen={start}
 while pending:
  x,y=pending.pop()
  for q in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
   if q in pixels and q not in seen:seen.add(q);pending.append(q)
 return seen
results=[];count=0
for v in vs:
 folder=OUT/v['id'];edges={}
 for color in ('white','navy','black','primary','light'):
  assert ET.parse(folder/f'mark-{color}.svg').getroot().find('s:path',NS).get('d')==v['merged']
  for size in (16,24,32,64,256):
   im=Image.open(folder/f'mark-{color}-{size}.png');assert im.mode=='RGBA' and im.size==(size,size)
   a=im.getchannel('A');x0,y0,x1,y1=a.getbbox();assert 0<x0<x1<size and 0<y0<y1<size
   white=Image.open(folder/f'mark-white-{size}.png').getchannel('A');diff=ImageChops.difference(a,white)
   assert diff.getextrema()[1]==0,(v['id'],color,size,diff.getextrema())
   if color in ('white','navy','black'):
    rgb={'white':(255,255,255),'navy':(8,17,31),'black':(0,0,0)}[color];assert all(p[:3]==rgb for p in im.get_flattened_data() if p[3]==255)
   if size<=64:
    ink={(x,y) for y in range(size) for x in range(size) if a.getpixel((x,y))>=128};assert connected(ink,next(iter(ink)))==ink
    clear={(x,y) for y in range(size) for x in range(size) if a.getpixel((x,y))<128};seed=(round(size*.6),size//2);assert seed in clear and any(x==size-1 for x,y in connected(clear,seed))
   if v['id']=='a1' and size<=64:
    benchmark=Image.open(ROOT/f'logo/confluence-flow/a/mark-{color}-{size}.png');assert ImageChops.difference(im,benchmark).getbbox() is None
   count+=1
 px=list(Image.open(folder/'mark-primary-256.png').get_flattened_data());area=sum(p[3] for p in px);pct=100*sum(p[3]*max(0,min(1,(244-p[0])/187)) for p in px)/area;assert 6<=pct<=8
 results.append({'id':v['id'],'aqua_area_percent':round(pct,3),'identical_colorway_masks':True,'native_counter_open_and_ink_connected':True})
assert results[1]['aqua_area_percent']<results[0]['aqua_area_percent'] and abs(results[2]['aqua_area_percent']-results[1]['aqua_area_percent'])<.05
report={'status':'passed','selected_base':'A / Balanced','refinements':3,'pngs_checked':count,'sizes':[16,24,32,64,256],'a1_exact_geometry_and_native_benchmark':True,'a2_silhouette_unchanged':True,'a3_width_reduction_percent':2.5,'a3_lower_return_preserved_under_scaling':True,'variants':results}
(OUT/'checks.json').write_text(json.dumps(report,indent=2)+'\n')
with zipfile.ZipFile(OUT/'covan-a-optical-refinements.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(OUT.rglob('*')):
  if p.is_file() and p.suffix in ('.svg','.png','.json'):z.write(p,Path('covan-a-optical-refinements')/p.relative_to(OUT))
 for file in ('confluence-finish-geometry.py','confluence-flow-geometry.py','build-confluence-finish.py','build-confluence-flow.py','export-confluence-finish.js','check-confluence-finish.py'):z.write(ROOT/'scripts'/file,Path('covan-a-optical-refinements/source')/file)
 z.write(ROOT/'docs/logo-confluence-finish.md','covan-a-optical-refinements/BRIEF.md');z.write(ROOT/'assets/fonts/Inter-LICENSE.txt','covan-a-optical-refinements/Inter-LICENSE.txt')
 z.writestr('covan-a-optical-refinements/README.txt','Option A is the selected base. Compare A1 Current benchmark, A2 Refined confluence and A3 Refined silhouette. The final optical variant remains pending review. PNG sizes: 16/24/32/64/256, with monochrome and aqua versions, outlined wordmark lockups and construction sources. Source scripts use the project paths; see BRIEF.md.\n')
print(json.dumps({'status':'passed','pngs':count,'aqua_area_percent':{v['id']:v['aqua_area_percent'] for v in results},'a1_exact':True,'a2_outline_unchanged':True,'a3_narrower_percent':2.5},indent=2))
