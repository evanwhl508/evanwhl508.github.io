#!/usr/bin/env python3
"""Asset QA: frozen paths, SVG portability, alpha/dimensions and metadata references."""
from pathlib import Path
import json,hashlib,re,xml.etree.ElementTree as ET
from PIL import Image,ImageChops
from fontTools.svgLib.path import parse_path
from fontTools.pens.recordingPen import RecordingPen
ROOT=Path(__file__).resolve().parents[1];B=ROOT/'public/brand';m=json.loads((B/'manifest.json').read_text());ns={'s':'http://www.w3.org/2000/svg'}
assert hashlib.sha256((ROOT/m['master']['source']).read_bytes()).hexdigest()==m['master']['sha256']
def commands(d):
    p=RecordingPen();parse_path(d,p);return p.value
master=ET.parse(B/'logo/covan-mark-primary.svg').getroot()
for source,target in [(m['master']['silhouette'],master.find('s:path',ns).get('d')),(m['master']['confluence'],master.find('.//s:pattern/s:path',ns).get('d'))]:
    a,b=commands(source),commands(target);assert len(a)==len(b)
    for (op,p),(op2,q) in zip(a,b):
        assert op==op2
        for pt,qt in zip(p,q):assert all(abs(v*5.12-w)<1e-9 for v,w in zip(pt,qt))
svgs=list((B/'logo').glob('*.svg'))+list((B/'micro').glob('*.svg'))
for path in svgs:
    r=ET.parse(path).getroot();assert r.get('viewBox') and r.find('s:title',ns) is not None
    ids={e.get('id') for e in r.iter() if e.get('id')}
    for e in r.iter():
        assert e.tag.split('}')[-1] not in ('image','text','script','mask','foreignObject','filter','linearGradient','radialGradient'),path
        for k,v in e.attrib.items():
            assert 'href' not in k and 'data:' not in v,path
            for ref in re.findall(r'url\(#([^)]*)\)',v):assert ref in ids,path
    assert not any(e.get('transform') for e in r.iter()),path
pngs=0
for asset in m['exports']:
    for size in [512,256,128,64,32]:
        p=B/'png'/Path(asset['svg']).name.replace('.svg',f'-{size}.png');im=Image.open(p)
        assert im.size==(size,max(1,round(size*asset['height']/asset['width']))),p
        assert im.mode=='RGBA' and im.getchannel('A').getextrema()[0]==0 and im.getchannel('A').getextrema()[1]>0,p;pngs+=1
for size in [16,24,32,48]:
    for name in ['favicon','candidate-a','candidate-b']:
        p=B/f'favicon/{name}-{size}.png';assert Image.open(p).size==(size,size);pngs+=1
for path,size in [('favicon/apple-touch-icon.png',180),('favicon/android-chrome-192.png',192),('favicon/android-chrome-512.png',512),('social/covan-avatar-512.png',512),('social/covan-avatar-1024.png',1024)]:
    im=Image.open(B/path);assert im.size==(size,size) and (im.mode=='RGB' or im.getchannel('A').getextrema()==(255,255));pngs+=1
og=Image.open(B/'social/covan-og-brand.png');assert og.size==(1200,630)
# Catch lost/translated pattern fills, which dimensions alone cannot detect.
for path,box,minimum in [('social/covan-avatar-512.png',(0,0,512,512),20000),('social/covan-og-brand.png',(480,85,720,325),8000)]:
    im=Image.open(B/path).convert('RGB').crop(box)
    visible=sum(1 for r,g,b in im.get_flattened_data() if r>200 and g>200 and b>200)
    assert visible>minimum,(path,visible,'Missing or clipped mark')
# Stacked mark must retain the same occupied area as the master at its scale.
stack=Image.open(B/'png/covan-logo-stacked-dark-512.png').convert('RGBA')
ink=sum(1 for r,g,b,a in stack.crop((0,0,512,328)).get_flattened_data() if a>127)
assert ink>20000,('Stacked mark clipped',ink)
for type in ['primary','monochrome','light','navy']:
    for size in [16,20,24,32,48,64]:
        im=Image.open(B/f'micro/covan-mark-micro-{type}-{size}.png');assert im.size==(size,size) and im.getchannel('A').getextrema()==(0,255);pngs+=1
# Compare complete RGBA bytes, not only difference alpha.
a=Image.open(ROOT/'output/playwright/master-approved.png');b=Image.open(ROOT/'output/playwright/master-production.png');assert a.tobytes()==b.tobytes(),'Master raster changed'
def luminance(h):
    cs=[int(h[i:i+2],16)/255 for i in (1,3,5)];cs=[c/12.92 if c<=.04045 else ((c+.055)/1.055)**2.4 for c in cs];return sum(a*b for a,b in zip(cs,[.2126,.7152,.0722]))
def contrast(a,b):
    a,b=sorted([luminance(a),luminance(b)]);return (b+.05)/(a+.05)
contrasts={f'{a}/{b}':round(contrast(a,b),2) for a,b in [('#15999C','#F6F8FB'),('#39C6C8','#08111F'),('#F4F7FA','#08111F'),('#9EADBD','#101C2C')]}
assert contrasts['#15999C/#F6F8FB']>=3
assert contrasts['#9EADBD/#101C2C']>=4.5
for p in list(ROOT.glob('index.html'))+list((ROOT/'theme2').rglob('*.html'))+list((ROOT/'brand').rglob('*.html')):
    html=p.read_text();assert '/public/brand/favicon/favicon.svg' in html and '/public/brand/social/covan-og-brand.png' in html,p
    assert 'src="/logo/covan-' not in html,p
for ico in json.loads((B/'site.webmanifest').read_text())['icons']:assert (ROOT/ico['src'].lstrip('/')).exists()
report={'master':'Exact path scaling and pixel identity PASS','portable_svgs':len(svgs),'pngs_checked':pngs+1,'contrast':contrasts,'favicon':m['favicon'],'status':'PASS'}
(B/'checks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
