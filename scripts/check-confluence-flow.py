#!/usr/bin/env python3
"""Check curved source union/intersection, optical stations and native-size proofs."""
from pathlib import Path
import json,math,xml.etree.ElementTree as ET,zipfile
from PIL import Image,ImageChops
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'logo/confluence-flow';NS={'s':'http://www.w3.org/2000/svg'}
m=json.loads((BASE/'manifest.json').read_text());assert [v['id'] for v in m['variants']]==['a','b','c']
COLORS=('white','navy','black','primary','light');SIZES=(16,24,32,64,512)
def connected(pixels,start):
 pending=[start];seen={start}
 while pending:
  x,y=pending.pop()
  for q in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
   if q in pixels and q not in seen:seen.add(q);pending.append(q)
 return seen
def source_comparison(expected,actual):
 diff=ImageChops.difference(expected,actual);points=[(x,y) for y in range(512) for x in range(512) if diff.getpixel((x,y))]
 # Independent subdivision rasterization may differ at one contour-edge pixel.
 assert len(points)<=1 and diff.getextrema()[1]<=64,(len(points),diff.getextrema())
 for x,y in points:
  assert any(actual.getpixel((xx,yy))<255 for xx in range(max(0,x-1),min(512,x+2)) for yy in range(max(0,y-1),min(512,y+2)))
 return {'different_boundary_pixels':len(points),'maximum_alpha_difference':diff.getextrema()[1]}
def aligned(a,b):
 assert abs(a[0]*b[1]-a[1]*b[0])<1e-8 and a[0]*b[0]+a[1]*b[1]>0
results=[];count=0
for v in m['variants']:
 folder=BASE/v['id'];q=v['segments']
 assert v['merged'].count('C')==10 and 'A' not in v['merged']
 for before,after in [(q[1],q[2]),(q[6],q[7])]:
  assert before[-1]==after[0]
  aligned([before[3][i]-before[2][i] for i in (0,1)],[after[1][i]-after[0][i] for i in (0,1)])
 changes={}
 for station,old in [('spine',20),('crown',21),('lower_sweep',18)]:
  pct=(v['optical_stations'][station]/old-1)*100;assert 5-1e-8<=abs(pct)<=8;changes[station]=round(pct,2)
 for name,key in [('origin-a','origin_a'),('origin-b','origin_b'),('overlap','confluence')]:assert ET.parse(folder/f'{name}.svg').getroot().find('s:path',NS).get('d')==v[key]
 for color in COLORS:
  assert ET.parse(folder/f'mark-{color}.svg').getroot().find('s:path',NS).get('d')==v['merged']
  for size in SIZES:
   im=Image.open(folder/f'mark-{color}-{size}.png');assert im.mode=='RGBA' and im.size==(size,size)
   a=im.getchannel('A');assert a.getextrema()==(0,255);x0,y0,x1,y1=a.getbbox();assert 0<x0<x1<size and 0<y0<y1<size
   if color in ('white','navy','black'):
    rgb={'white':(255,255,255),'navy':(8,17,31),'black':(0,0,0)}[color];assert all(p[:3]==rgb for p in im.get_flattened_data() if p[3]==255)
   white=Image.open(folder/f'mark-white-{size}.png').getchannel('A');assert ImageChops.difference(a,white).getextrema()[1]==0
   if size<=64:
    ink={(x,y) for y in range(size) for x in range(size) if a.getpixel((x,y))>=128};assert connected(ink,next(iter(ink)))==ink
    clear={(x,y) for y in range(size) for x in range(size) if a.getpixel((x,y))<128};seed=(round(size*.6),size//2);assert seed in clear and any(x==size-1 for x,y in connected(clear,seed))
   count+=1
 px=list(Image.open(folder/'mark-primary-512.png').get_flattened_data());area=sum(p[3] for p in px);aqua=100*sum(p[3]*max(0,min(1,(244-p[0])/187)) for p in px)/area;assert 6<=aqua<=10
 a=Image.open(ROOT/f'output/playwright/confluence-flow-{v["id"]}-origin-a.png').getchannel('A');b=Image.open(ROOT/f'output/playwright/confluence-flow-{v["id"]}-origin-b.png').getchannel('A')
 merged=Image.open(folder/'mark-white-512.png').getchannel('A');overlap=Image.open(ROOT/f'output/playwright/confluence-flow-{v["id"]}-overlap.png').getchannel('A')
 results.append({'id':v['id'],'aqua_filled_area_percent':round(aqua,3),'optical_station_change_percent':changes,'spine_tangents_aligned':True,'union_check':source_comparison(ImageChops.lighter(a,b),merged),'intersection_check':source_comparison(ImageChops.darker(a,b),overlap),'all_colorway_alpha_masks_identical':True,'native_counter_open_and_ink_connected':True})
report={'status':'passed','refinements':3,'pngs_checked':count,'sizes':list(SIZES),'variants':results,'limitation':'Independent source rasterization differs on at most one boundary pixel at 512px, recorded above. All final colorway masks match exactly. Checks establish construction and raster legibility, not subjective beauty or legal distinctiveness.'}
(BASE/'checks.json').write_text(json.dumps(report,indent=2)+'\n')
with zipfile.ZipFile(BASE/'covan-curved-confluence.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(BASE.rglob('*')):
  if p.is_file() and p.suffix in ('.svg','.png','.json'):z.write(p,Path('covan-curved-confluence')/p.relative_to(BASE))
 for name in ('confluence-flow-geometry.py','build-confluence-flow.py','export-confluence-flow.js','check-confluence-flow.py'):z.write(ROOT/'scripts'/name,Path('covan-curved-confluence/source')/name)
 z.write(ROOT/'docs/logo-confluence-flow.md','covan-curved-confluence/BRIEF.md');z.write(ROOT/'assets/fonts/Inter-LICENSE.txt','covan-curved-confluence/Inter-LICENSE.txt')
 z.writestr('covan-curved-confluence/README.txt','Exactly three refinements: A Balanced, B Flowing, C Minimal. None is selected. Start with comparison-white.png, comparison-primary.png or comparison-light.png. Each folder includes construction curves, actual overlap, the merged mark, navbar lockups and transparent 16/24/32/64/512px PNGs. Source scripts use the original project paths; see BRIEF.md.\n')
print(json.dumps({'status':'passed','refinements':3,'pngs_checked':count,'aqua_area_percent':{v['id']:v['aqua_filled_area_percent'] for v in results}},indent=2))
