#!/usr/bin/env python3
"""Production assets. Run with fontTools[woff]; master paths are frozen, never re-designed."""
from pathlib import Path
import json, re, hashlib, xml.etree.ElementTree as ET
from functools import lru_cache
from fontTools.svgLib.path import parse_path
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/brand'
NAVY='#08111F'; WHITE='#F4F7FA'; AQUA='#39C6C8'; TEAL='#15999C'; SILVER='#9EADBD'
m=json.loads((OUT/'source/master.json').read_text())
assert hashlib.sha256((ROOT/m['source']).read_bytes()).hexdigest()==m['sha256'], 'Approved source changed; stop production.'

def transform(d,scale=1,x=0,y=0):
    pen=SVGPathPen(None);parse_path(d,TransformPen(pen,(scale,0,0,scale,x,y)));return pen.getCommands()

def svg(w,h,body,label='Covan Labs'):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{label}">\n<title>{label}</title>\n{body}\n</svg>\n'

def save(path,text):
    p=OUT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)

# One derived Micro C: a slightly thicker counter and simpler, wider terminal clearance.
# These control points are deliberately isolated from the approved master.
micro='M80 22C73 11 63 7 50 7C28.5 7 14 25.5 14 49C14 73 28 91 48.5 91C62 91 74 86 80 80C82.5 75.5 76 71 69.5 74C64 78.5 57 79 49.8 79C35 79 29.5 64 29.5 49.5C29.5 33 39 21 51.4 21C60 21 67 25 71.5 31C74 34 76.5 24 80 22Z'
micro_accent='M14 47C14 53 14.6 59 15.8 63C20 65 26 61 30.1 57C29.6 54 29.5 51 29.5 47.5C25 46 19 49 14 47Z'
save('source/micro.json',json.dumps({'derived_from':m['sha256'],'silhouette':micro,'confluence':micro_accent,'adjustments':'Counter slightly thickened; terminal clearance widened; confluence simplified. Master unchanged.'},indent=2)+'\n')

def mark(body=WHITE,accent=AQUA,size=512,x=0,y=0,tier='master',uid='ink'):
    scale=size/100;d=transform(micro if tier=='micro' else m['silhouette'],scale,x,y)
    a=transform(micro_accent if tier=='micro' else m['confluence'],scale,x,y)
    if not accent:return f'<path fill="{body}" d="{d}"/>'
    return f'<defs><pattern id="{uid}" x="0" y="0" width="{size+x}" height="{size+y}" patternUnits="userSpaceOnUse"><rect x="0" y="0" width="{size+x}" height="{size+y}" fill="{body}"/><path fill="{accent}" d="{a}"/></pattern></defs>\n<path fill="url(#{uid})" d="{d}"/>'

@lru_cache(None)
def font(family,weight):
    paths={'Inter':ROOT/'assets/fonts/InterVariable.woff2','Manrope':OUT/'source/fonts/Manrope.ttf','Noto':OUT/'source/fonts/NotoSansTC.ttf'}
    f=TTFont(paths[family]);axes={a.axisTag:weight if a.axisTag=='wght' else 24 if a.axisTag=='opsz' else a.defaultValue for a in f['fvar'].axes};return instantiateVariableFont(f,axes,inplace=True)

def text_paths(text,family,weight,size,x,baseline):
    f=font(family,weight);gs=f.getGlyphSet();cmap=f.getBestCmap();scale=size/f['head'].unitsPerEm;paths=[]
    for char in text:
        name=cmap[ord(char)];pen=SVGPathPen(gs, ntos=lambda n: format(n,".4f").rstrip("0").rstrip(".") if n else "0");gs[name].draw(TransformPen(pen,(scale,0,0,-scale,x,baseline)))
        paths.append(f'<path d="{pen.getCommands()}"/>');x+=f['hmtx'][name][0]*scale-.28*(size/24)
    return ''.join(paths),x

def word(family='Inter',x=0,baseline=28.5,size=24,color=WHITE):
    a,end=text_paths('Covan',family,600,size,x,baseline);b,end=text_paths('Labs',family,425,size,end+5.8*size/24,baseline)
    return f'<g fill="{color}">{a}{b}</g>',end

# Physical ink gap ~17px: 0.56 of the 30.24px visible mark height.
# Path coordinates, rather than transforms, make exported assets portable.
def lockup(layout='horizontal',body=WHITE,accent=AQUA,family='Inter'):
    if layout in ('horizontal','localized'):
        w,end=word(family,x=47,baseline=28.5)
        w=w.replace(WHITE,body)
        height=40 if layout=='horizontal' else 60
        content=mark(body,accent,36,0,2)+w
        if layout=='localized':
            c,_=text_paths('高凡','Noto',400,12,48,48);content+=f'<g fill="{body}">{c}</g>'
        return svg(round(end+9,3),height,content),round(end+9,3),height
    w,end=word(family,x=0,baseline=0)
    width=200;content=mark(body,accent,128,36,0)
    w,_=word(family,x=(width-end)/2,baseline=155,color=body)
    return svg(width,180,content+w),width,180

variants={'primary':(WHITE,AQUA),'light':(NAVY,TEAL),'white':(WHITE,None),'navy':(NAVY,None),'black':('#000000',None)}
exports=[]
for name,(body,accent) in variants.items():
    path=f'logo/covan-mark-{name}.svg';save(path,svg(512,512,mark(body,accent)));exports.append({'svg':path,'kind':'transparent','width':512,'height':512})
for tier in ['primary','monochrome']:
    save(f'micro/covan-mark-micro-{tier}.svg',svg(512,512,mark(WHITE,AQUA if tier=='primary' else None,tier='micro')))
save('micro/covan-mark-micro-light.svg',svg(512,512,mark(NAVY,TEAL,tier='micro')))
save('micro/covan-mark-micro-navy.svg',svg(512,512,mark(NAVY,None,tier='micro')))
for layout in ['horizontal','stacked','localized']:
    for name,(body,accent) in {'dark':(WHITE,AQUA),'light':(NAVY,TEAL),'white':(WHITE,None),'monochrome':(NAVY,None),'black':('#000000',None)}.items():
        s,w,h=lockup(layout,body,accent);path=f'logo/covan-logo-{layout}-{name}.svg';save(path,s);exports.append({'svg':path,'kind':'transparent','width':w,'height':h})
# Editable source: deliberately live text; production counterparts above contain outlines only.
save('source/wordmark-editable.svg',svg(180,40,mark(WHITE,AQUA,36,0,2)+'<text x="47" y="28.5" font-family="Inter" font-size="24" letter-spacing="-.28" fill="#F4F7FA"><tspan font-weight="600">Covan</tspan><tspan dx="5.8" font-weight="425">Labs</tspan></text>'))
for family in ['Inter','Manrope']:
    s,w,h=lockup(family=family);save(f'proofs/wordmark-{family.lower()}.svg',s)
# Avatar has safe padding even under circular crops.
for size in [512,1024]:
    save(f'social/covan-avatar-{size}.svg',svg(size,size,f'<rect width="{size}" height="{size}" fill="{NAVY}"/>'+mark(size=size*.72,x=size*.14,y=size*.14)))
og_word,og_width=word(x=0,baseline=409,size=72)
og_word,_=word(x=(1200-og_width)/2,baseline=409,size=72)
caption,caption_width=text_paths('Independent software studio · Hong Kong','Inter',400,24,0,474)
caption,_=text_paths('Independent software studio · Hong Kong','Inter',400,24,(1200-caption_width)/2,474)
save('social/covan-og-brand.svg',svg(1200,630,f'<rect width="1200" height="630" fill="{NAVY}"/>'+mark(size=240,x=480,y=85)+og_word+f'<g fill="{SILVER}">{caption}</g>'))
# Exact clear-space diagram: 1x measured from visible ink bounds.
from fontTools.pens.boundsPen import BoundsPen
bounds=BoundsPen(None);parse_path(transform(m['silhouette'],5.12,64,64),bounds)
x0,y0,x1,y1=bounds.bounds;space=70.656
save('proofs/clear-space.svg',svg(640,640,mark(size=512,x=64,y=64)+f'<rect x="{x0-space}" y="{y0-space}" width="{x1-x0+2*space}" height="{y1-y0+2*space}" fill="none" stroke="{AQUA}" stroke-width="2" stroke-dasharray="6 6"/><rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" fill="none" stroke="{SILVER}" stroke-dasharray="4 5"/><path d="M{x0} {y0-35}H{x0-space}" stroke="{AQUA}" stroke-width="2"/><text x="{x0-space/2}" y="{y0-44}" text-anchor="middle" fill="{WHITE}" font-family="sans-serif" font-size="18">1x</text>'))
# Favicon candidates use a stable navy tile so either browser chrome stays legible.
for name,accent in [('a',AQUA),('b',None)]:
    save(f'favicon/candidate-{name}.svg',svg(512,512,f'<rect width="512" height="512" rx="80" fill="{NAVY}"/>'+mark(WHITE,accent,tier='micro')))
# Native-size review selected B: continuous luminance improves the 16px spine.
save('favicon/favicon.svg',(OUT/'favicon/candidate-b.svg').read_text())
manifest={'master':m,'colors':variants,'wordmark':{'family':'Inter','Covan':600,'Labs':425,'ink_gap_to_mark_height':.56},'exports':exports,'favicon':'B — monochrome','minimums':{'master_standalone':64,'master_navbar_artboard':36,'horizontal_width':160,'micro':16},'clear_space':{'x_in_512_units':70.656,'definition':'Left middle thickness: (27.8 − 14) × 5.12'}}
save('manifest.json',json.dumps(manifest,indent=2)+'\n')
print('Built frozen master, Micro C, 15 outlined lockups, font proofs and export manifest.')
