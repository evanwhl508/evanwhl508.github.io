#!/usr/bin/env python3
"""Two restrained identity directions, two refinements each. Monochrome only."""
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
import math, json
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'logo/identity';OUT.mkdir(exist_ok=True)
FONT=instantiateVariableFont(TTFont(ROOT/'assets/fonts/InterVariable.woff2'),{'wght':520,'opsz':32})
GS=FONT.getGlyphSet();CMAP=FONT.getBestCmap();CAP=FONT['OS/2'].sCapHeight
COLORS={'white':'#FFFFFF','navy':'#08111F'}
A1C='M86 18C77 6 65 -1 49 -1C21 -1 3 20 3 50C3 80 21 101 49 101C65 101 78 94 87 82L77 74C70 84 61 89 49 89C29 89 16 73 16 50C16 27 29 11 49 11C61 11 71 17 77 27Z'
A2C='M81 19C73 6 61 -1 46 -1C20 -1 3 19 3 50C3 81 20 101 46 101C62 101 74 94 82 81L71 75C65 85 57 89 46 89C28 89 16 74 16 50C16 26 28 11 46 11C57 11 65 16 71 26Z'
# These C paths are the actual first glyphs in A, not marks drawn afterward.
V='M0 29.128H12.9L32.1 84.9Q33.9 90.2 35.7 84.9L55.1 29.128H68L41.5 100H26.5Z'
B1C='M82 23C74 14 63 10 51 10C28 10 11 27 11 50C11 73 28 90 51 90C63 90 74 85 82 76L72.8 67.6C67.1 74.1 60.5 77.5 51 77.5C35.3 77.5 23.5 65.7 23.5 50C23.5 34.3 35.3 22.5 51 22.5C60.5 22.5 67.1 25.9 72.8 32.4Z'
B2C='M78.16 24C72 14 62.32 9 50.88 9C29.76 9 16.56 27 16.56 50C16.56 74 30.64 91 50.88 91C63.2 91 72.88 85 79.92 75L71.12 67C65.84 74 58.8 79 50.88 79C36.8 79 27.12 67 27.12 50C27.12 33 36.8 21 50.88 21C58.8 21 65.84 25 70.24 32Z'
VARIANTS={
 'a1':dict(direction='A',label='Open proportions',c=A1C,cwidth=87,owidth=68,vscale=1,xscale=1,gaps=[9,8,8,10],wordgap=40,labscale=.91,summary='A broader C, open counters and measured spacing.',changes=['C redrawn with a broad bowl, controlled overshoot and inclined terminals.','o redrawn to echo the C’s counter proportions. v has a shallow curved inner join.','C–o, o–v, v–a and a–n spaced individually; Labs uses 91% cap height.']),
 'a2':dict(direction='A',label='Closer proportions',c=A2C,cwidth=82,owidth=65,vscale=.96,xscale=.97,gaps=[8,7,8,9],wordgap=38,labscale=.91,summary='A slightly narrower C and a closer word rhythm.',changes=['C redrawn with a narrower bowl and more upright terminal cuts.','o and v narrowed with it; a/n adjusted in width to retain an even rhythm.','Pair spacing tightened selectively; the same restrained Labs proportions.']),
 'b1':dict(direction='B',label='Circular balance',c=B1C,summary='A continuous C with an almost circular counter.',changes=['One uninterrupted contour; no module seams.','Concentric-feeling curves and matched oblique terminal cuts.','The mark sits at 28px beside a restrained 20px Inter wordmark.']),
 'b2':dict(direction='B',label='Optical balance',c=B2C,summary='A quieter upper bowl and a slightly fuller lower return.',changes=['One uninterrupted contour; no hidden letters.','A slightly more upright bowl and a modestly extended lower terminal.','The same typography, scale and spacing as B1, so only the C changes.']),
}

def glyph(char,x,baseline,cap=100,xscale=1):
    g=GS[CMAP[ord(char)]];bounds=BoundsPen(GS);g.draw(bounds);left,_,right,_=bounds.bounds
    sy=cap/CAP;sx=sy*xscale;pen=SVGPathPen(GS,ntos=lambda n:f'{n:.4f}'.rstrip('0').rstrip('.'))
    g.draw(TransformPen(pen,(sx,0,0,-sy,x-left*sx,baseline)))
    return f'<path d="{pen.getCommands()}"/>',(right-left)*sx

def oval(width):
    rx=width/2;ry=37.05;cy=64.5;ix=rx-11.7;iy=ry-11.4
    return f'M{width} {cy}A{rx} {ry} 0 1 0 0 {cy}A{rx} {ry} 0 1 0 {width} {cy}ZM{rx+ix} {cy}A{ix} {iy} 0 1 1 {rx-ix} {cy}A{ix} {iy} 0 1 1 {rx+ix} {cy}Z'

def a_wordmark(v):
    # y=0..100 is the capital-letter design space. All paths share baseline 100.
    content=[f'<path data-letter="C" d="{v["c"]}"/>'];x=v['cwidth']+v['gaps'][0]
    content.append(f'<path data-letter="o" transform="translate({x} 0)" fill-rule="evenodd" d="{oval(v["owidth"])}"/>');x+=v['owidth']+v['gaps'][1]
    content.append(f'<path data-letter="v" transform="translate({x} 0) scale({v["vscale"]} 1)" d="{V}"/>');x+=68*v['vscale']+v['gaps'][2]
    for i,char in enumerate('an'):
        p,w=glyph(char,x,100,xscale=v['xscale']);content.append(p);x+=w+(v['gaps'][3] if i==0 else 0)
    x+=v['wordgap']
    for i,char in enumerate('Labs'):
        p,w=glyph(char,x,100,100*v['labscale'],v['xscale']);content.append(p);x+=w+(9*v['labscale'] if i<3 else 0)
    return ''.join(content),x

def b_wordmark():
    x=0;parts=[]
    for i,char in enumerate('Covan Labs'):
        if char==' ':x+=35;continue
        p,w=glyph(char,x,100,100);parts.append(p);x+=w+(8 if i<9 else 0)
    return ''.join(parts),x

def svg(w,h,body,label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:.4f}" height="{h:.4f}" viewBox="0 0 {w:.4f} {h:.4f}" role="img" aria-label="{label}"><title>{label}</title>{body}</svg>\n'

def mark(v,color):
    # A is extracted from its existing first glyph, uniformly scaled and centered.
    if v['direction']=='A':
        s=.76;x=(100-v['cwidth']*s)/2;y=12
        return f'<g fill="{color}" transform="translate({x:.4f} {y}) scale({s})"><path d="{v["c"]}"/></g>'
    return f'<path fill="{color}" d="{v["c"]}"/>'

def main():
    data=[]
    for key,v in VARIANTS.items():
        folder=OUT/key;folder.mkdir(exist_ok=True)
        word,width=a_wordmark(v) if v['direction']=='A' else b_wordmark()
        for name,color in COLORS.items():
            (folder/f'mark-{name}.svg').write_text(svg(100,100,mark(v,color),f'{key.upper()} standalone C'))
            (folder/f'wordmark-{name}.svg').write_text(svg(width+16,120,f'<g fill="{color}" transform="translate(8 10)">{word}</g>',f'Covan Labs — {key.upper()}'))
            if v['direction']=='A':
                lockup=svg(width+16,120,f'<g fill="{color}" transform="translate(8 10)">{word}</g>',f'Covan Labs — {key.upper()} wordmark-led identity')
                capwidth=(width+16)/120*28
            else:
                # Mark 28px / letter capitals 20px in a 36px-tall navbar asset.
                tx=40;scale=.2
                lockup=svg(tx+width*scale+2,36,f'<g transform="translate(0 4) scale(.28)">{mark(v,color)}</g><g fill="{color}" transform="translate({tx} 8) scale({scale})">{word}</g>',f'Covan Labs — {key.upper()} identity')
                capwidth=tx+width*scale+2
            (folder/f'identity-{name}.svg').write_text(lockup)
        data.append({**v,'id':key,'navbar_height':28 if v['direction']=='A' else 36,'navbar_width':round(capwidth,3),'wordmark_width':round(width+16,3)})
    (OUT/'manifest.json').write_text(json.dumps({'status':'unapproved monochrome studies','directions':2,'refinements_per_direction':2,'color':'monochrome only','a_extraction':'Exact C path from the wordmark; translation and uniform scale only','variants':data},indent=2)+'\n')
    build_page(data);build_sheet(data)
    print('Built A1/A2 custom wordmarks and extracted Cs; B1/B2 continuous C marks. Monochrome only.')

def build_page(data):
    sections=[]
    for direction,title,description in [('A','Wordmark first.','The C is drawn as the first letter of Covan. The standalone mark is that same letter, extracted without redrawing it.'),('B','One elegant C.','Two continuous curves, compared beside the same restrained wordmark. No modular seams or hidden-letter construction.')]:
        cards=[]
        for v in (v for v in data if v['direction']==direction):
            key=v['id'];native=''.join(f'<figure><img src="{key}/mark-white-{z}.png" width="{z}" height="{z}" alt="{key.upper()} at {z}px"><figcaption>{z}px</figcaption></figure>' for z in [16,24,32,64])
            cards.append(f'''<article class="study" id="{key}"><header class="study-label"><h3>{key.upper()}</h3><span>{v['label']}</span></header><div class="navbar-proof dark"><img class="identity" src="{key}/identity-white.svg" width="{v['navbar_width']}" height="{v['navbar_height']}" alt="{key.upper()} Covan Labs at actual navbar size"><span class="nav-text">Products　 About　 Contact</span></div><div class="navbar-proof light"><img class="identity" src="{key}/identity-navy.svg" width="{v['navbar_width']}" height="{v['navbar_height']}" alt="{key.upper()} Covan Labs in navy at actual navbar size"><span class="nav-text">Products　 About　 Contact</span></div><p class="proof-caption">Actual navbar scale · {'wordmark only' if direction=='A' else '28px mark / 20px cap height'}</p><div class="enlargement"><img src="{key}/identity-white.svg" width="{v['navbar_width']*2}" height="{v['navbar_height']*2}" alt="{key.upper()} identity enlarged two times"></div><div class="mark-proof"><img class="standalone" src="{key}/mark-white.svg" width="128" height="128" alt="{key.upper()} {'C extracted from the wordmark' if direction=='A' else 'standalone C'}"><div><span class="micro-label">{'The same C, extracted' if direction=='A' else 'Standalone C'}</span><div class="size-tests">{native}</div></div></div><details><summary>Refinement notes &amp; files</summary><p>{v['summary']}</p><ul>'''+''.join(f'<li>{change}</li>' for change in v['changes'])+f'''</ul><p class="files"><a href="{key}/identity-white.svg" download>White identity SVG</a><a href="{key}/identity-navy.svg" download>Navy identity SVG</a><a href="{key}/mark-white.svg" download>White C SVG</a><a href="{key}/mark-navy.svg" download>Navy C SVG</a><a href="{key}/mark-white-512.png" download>512px transparent C</a></p></details></article>''')
        sections.append(f'<section class="direction" aria-labelledby="heading-{direction}"><header class="direction-heading"><span class="eyebrow">Direction {direction}</span><h2 id="heading-{direction}">{title}</h2><p>{description}</p></header><div class="study-grid">'+''.join(cards)+'</div></section>')
    page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>Covan Labs — Two identity directions</title><link rel="icon" href="a1/mark-white.svg"><link rel="stylesheet" href="review.css"></head><body><a class="skip" href="#main">Skip to studies</a><main id="main"><header class="page-heading"><p><strong>Archived study.</strong> Superseded by <a href="/logo/two-origin/">the Two-Origin C family</a>.</p><p class="eyebrow">Covan Labs / Monochrome studies</p><h1>Two directions.<br>A quieter identity.</h1><p>Four refinements. Start with the name at navbar size.<br>No accent color. No hidden-letter stories. No scoring.</p></header>'''+''.join(sections)+'''<footer><p>Geometry remains open for review. Aqua comes only after approval.</p><div><a href="comparison-white.png">View comparison sheet</a><a href="covan-monochrome-identities.zip" download>Download SVG / PNG studies</a><a href="/">Studio website</a></div></footer></main></body></html>'''
    (OUT/'index.html').write_text(page)

def build_sheet(data):
    for colorname,color in COLORS.items():
        bg='#08111F' if colorname=='white' else '#F6F8FB';muted='#9EADBD' if colorname=='white' else '#647485';border='#27394D' if colorname=='white' else '#DCE4EC'
        parts=[f'<rect width="1440" height="960" fill="{bg}"/>']
        def label(text,x,y,size=14,fill=None):
            # Sheet labels need not form part of the outlined identity.
            return f'<text x="{x}" y="{y}" font-family="Inter,Arial,sans-serif" font-size="{size}" fill="{fill or muted}">{text}</text>'
        parts.append(label('COVAN LABS / MONOCHROME STUDIES',40,42,13))
        for i,v in enumerate(data):
            x=40+(i%2)*700;y=82+(i//2)*426;key=v['id']
            parts.append(f'<rect x="{x}" y="{y}" width="660" height="390" rx="12" fill="none" stroke="{border}"/>')
            parts.append(label(f'{key.upper()}  /  {v["label"]}',x+24,y+34))
            source=(OUT/key/f'identity-{colorname}.svg').read_text();contents=source[source.index('>')+1:source.rfind('</svg>')]
            import re
            view=re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"',source);iw,ih=map(float,view.groups())
            scale=v['navbar_height']/ih
            parts.append(label('NAVBAR SIZE',x+24,y+77,10))
            parts.append(f'<g transform="translate({x+24} {y+98}) scale({scale})">{contents}</g>')
            parts.append(f'<g transform="translate({x+24} {y+175}) scale({scale*2})">{contents}</g>')
            parts.append(label('2× DETAIL',x+24,y+265,10))
            for xx,z in [(24,16),(70,24),(124,32),(192,64)]:
                parts.append(f'<g transform="translate({x+xx} {y+320-z/2}) scale({z/100})">{mark(v,color)}</g>');parts.append(label(str(z),x+xx,y+370,10))
            parts.append(f'<g transform="translate({x+480} {y+278}) scale(.8)">{mark(v,color)}</g>')
        parts.append(label('A / Wordmark-derived C     B / Refined continuous C     ·     Geometry unapproved. No accent color.',40,943,12))
        (OUT/f'comparison-{colorname}.svg').write_text(svg(1440,960,''.join(parts),'Covan Labs: two restrained identity directions, two refinements each'))
if __name__=='__main__':main()
