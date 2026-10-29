#!/usr/bin/env python3
"""Primary-scale output QA. No favicon-readability acceptance gate."""
from pathlib import Path
import json,xml.etree.ElementTree as ET,zipfile
from PIL import Image,ImageChops
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'logo/h1-polish';NS={'s':'http://www.w3.org/2000/svg'}
m=json.loads((OUT/'manifest.json').read_text());assert len(m['variants'])==3 and m['micro_created'] is False
benchmark,a,b=m['variants']
assert [v['id'] for v in m['variants']]==['benchmark','polish-a','polish-b']
master=json.loads((ROOT/'logo/confluence-hybrid/manifest.json').read_text())['variants'][0]
for key in ('merged','confluence','origin_a','origin_b'):assert benchmark[key]==master[key]
assert a['merged']==benchmark['merged']
for i in [0,1,2,3,6,7,8,9]:assert b['segments'][i]==benchmark['segments'][i]
assert b['segments'][4][:2]==benchmark['segments'][4][:2]
assert b['segments'][5][2:]==benchmark['segments'][5][2:]
for v in (a,b):assert abs(v['aqua_exact_area']-benchmark['aqua_exact_area'])<1e-7
terminal=b['polish']['terminal_measurement'];assert abs((1-terminal['after']/terminal['before'])*100-2.5)<1e-8
def seam_center(v):return sum(v[k][j][1] for k in ('upper_seam','lower_seam') for j in (0,3))/4
assert abs(seam_center(a)-seam_center(b)-.5)<1e-8
assert m['wordmark']['roomier_origin']-m['wordmark']['current_origin']==2
COLORS=('white','navy','black','primary','light');SIZES=(64,128,256)
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
   if v['id']=='benchmark':
    old=Image.open(ROOT/f'logo/confluence-hybrid/h1/mark-{color}-{size}.png');assert all(hi==0 for lo,hi in ImageChops.difference(im,old).getextrema())
   count+=1
 px=list(Image.open(folder/'mark-primary-256.png').get_flattened_data());area=sum(p[3] for p in px);pct=100*sum(p[3]*max(0,min(1,(244-p[0])/187)) for p in px)/area
 assert 6<=pct<=10,(v['id'],pct)
 results.append({'id':v['id'],'aqua_filled_area_percent':round(pct,3),'primary_counter_open_and_ink_connected':True,'colorway_svg_contour_identical':True,'raster_edge_differences':edge_differences})
report={'status':'passed','directions':3,'pngs_checked':count,'primary_sizes':[64,128,256],'benchmark_exact':True,'polish_a_silhouette_unchanged':True,'aqua_geometric_area_retained':True,'polish_b_lower_tip_reduction_percent':2.5,'polish_b_upward_shift_units':.5,'spacing_test_extra_px':2,'micro_created':False,'variants':results,'note':'Primary raster checks do not determine beauty or trademark distinctiveness. A separate micro design follows selection.'}
(OUT/'checks.json').write_text(json.dumps(report,indent=2)+'\n')
with zipfile.ZipFile(OUT/'covan-h1-final-polish.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(OUT.rglob('*')):
  if p.is_file() and p.suffix in ('.svg','.png','.json'):z.write(p,Path('covan-h1-final-polish')/p.relative_to(OUT))
 for name in ('h1-polish-geometry.py','confluence-hybrid-geometry.py','confluence-primary-geometry.py','confluence-flow-geometry.py','build-h1-polish.py','build-confluence-flow.py','export-h1-polish.js','check-h1-polish.py'):z.write(ROOT/'scripts'/name,Path('covan-h1-final-polish/source')/name)
 z.write(ROOT/'docs/logo-h1-polish.md','covan-h1-final-polish/BRIEF.md');z.write(ROOT/'assets/fonts/Inter-LICENSE.txt','covan-h1-final-polish/Inter-LICENSE.txt')
 z.writestr('covan-h1-final-polish/README.txt','H1 Elegant Hybrid is the selected master. Compare the unchanged benchmark with only Polish A and Polish B. Proofs: 256/128/64px, current navbar spacing and +2px spacing. No favicon optimization or new concepts. Source scripts require the repository paths described in BRIEF.md.\n')
print(json.dumps({'status':'passed','primary_sizes':[64,128,256],'micro_created':False,'pngs_checked':count,'aqua_percent':{v['id']:v['aqua_filled_area_percent'] for v in results}},indent=2))
