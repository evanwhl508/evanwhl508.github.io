#!/usr/bin/env python3
"""Three hybrid studies: Elegant Flow foundation, restrained organic tension."""
from pathlib import Path
import runpy,json
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'logo/confluence-hybrid';OUT.mkdir(exist_ok=True)
B=runpy.run_path(str(ROOT/'scripts/build-confluence-flow.py'));G=runpy.run_path(str(ROOT/'scripts/confluence-hybrid-geometry.py'))
svg,mark,lockup,grid=B['svg'],B['mark'],B['lockup'],B['grid'];WIDTH=B['WIDTH'];COLORS=B['COLORS']
def head(t,depth=''):
 return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{t} · Covan Labs</title><link rel="stylesheet" href="{depth}review.css"><link rel="icon" href="/logo/favicon-32.png"></head><body><a class="skip" href="#main">Skip to content</a>'
def footer(depth=''):
 return f'<footer><p>Hybrid refinement · Micro C follows selection</p><a href="{depth}covan-hybrid-studies.zip" download>Download SVG + PNG proofs</a><a href="/">Studio website</a></footer></body></html>'
def large(k,c,prefix=''):
 return f'<figure class="large-proof"><img class="native-large" src="{prefix}mark-{c}-256.png" width="256" height="256" alt="Study {k.upper()}, {c}, 256px"><figcaption>256px / primary mark</figcaption></figure>'
def sizes(k,c,prefix='',micro=False):
 return '<div class="sizes '+('micro-sizes' if micro else 'primary-sizes')+'">'+''.join(f'<figure><img src="{prefix}mark-{c}-{z}.png" width="{z}" height="{z}" alt="Study {k.upper()}, {c}, {z}px"><figcaption>{z}px</figcaption></figure>' for z in ((16,24) if micro else (128,64)))+'</div>'
def navbar(c,prefix=''):
 return f'<div class="navbar"><img src="{prefix}identity-{c}.svg" width="{WIDTH}" height="40" alt="Covan Labs at actual navbar size"></div><p class="caption">Navbar · 36px mark box · Inter 600 / 425</p>'
def micro(k,prefix=''):
 return '<details class="downloads secondary-reference"><summary>Secondary 16 / 24px reference</summary><p>These are direct reductions of the primary mark. They are not the Micro C. After the primary is approved, its micro version may simplify the curves, opening and color.</p>'+sizes(k,'primary',prefix,True)+sizes(k,'white',prefix,True)+'</details>'
def gallery(items):
 cards=[]
 for v,d in items:
  k=v['id'];cards.append(f'<article class="candidate"><header><span>{k.upper()}</span><span>{v["label"]}</span></header>{large(k,"white",k+"/")}<div class="proof-divider"></div>{large(k,"primary",k+"/")}{sizes(k,"primary",k+"/")}<div class="compact-lock"><img src="{k}/identity-primary.svg" width="{WIDTH}" height="40" alt="{v["label"]}, navbar lockup"></div><p class="character">{v["character"]}</p><a class="inspect" href="{k}/">Primary sizes, light &amp; construction ↗</a></article>')
 return head('Confluence C — hybrid refinement')+'''<main id="main"><header class="page-heading"><p class="eyebrow">Covan Labs / Hybrid refinement</p><h1>Elegant Flow, refined.</h1><p><strong>H1 is the selected master direction.</strong> Continue to <a href="../h1-polish/">H1 final optical polish</a>.</p><p>Three hybrids built on 01’s tall, open silhouette.<br>Restrained personality from 03. A touch of precision from 02.</p></header><div class="candidate-grid">'''+''.join(cards)+'''</div><section class="overview-note"><h2>One foundation. Three refinements.</h2><p>H1 stays closest to Elegant Flow. H2 adds the strongest opening character. H3 brings a little more geometric discipline. Each keeps the slender body and generous counter, with aqua following the curved source overlap.</p><p>Evaluate at 256, 128 and 64px, then in the navbar. A simplified Micro C follows primary selection; small reductions remain secondary references only.</p><div class="links"><a href="comparison-white.png">Monochrome comparison</a><a href="comparison-primary.png">Aqua comparison</a><a href="comparison-light.png">Light-background comparison</a></div></section></main>'''+footer()
def detail(v,d):
 k=v['id'];panels=[]
 for c,label in [('white','Monochrome / pure white'),('primary','Cool white + aqua'),('navy','Monochrome / pure navy'),('light','Navy + aqua')]:
  panels.append(f'<section class="proof {"paper" if c in ("navy","light") else "ink"}"><h2>{label}</h2>{large(k,c)}{sizes(k,c)}{navbar(c)}</section>')
 return head(v['label'],'../')+f'''<main id="main"><nav class="top-nav"><a href="../">← Compare three hybrids</a><span>Hybrid / {k.upper()}</span></nav><header class="detail-heading"><p class="eyebrow">Study {k.upper()}</p><h1>{v['label']}</h1><p>{v['description']}</p></header><div class="proof-grid">{''.join(panels)}</div><section class="explanation"><header><h2>Two origins. One continuous C.</h2><p>{v['description']} The upper and lower source forms overlap along the spine. Aqua is their actual shared region, bounded by curves.</p></header><div class="origins">'''+''.join(f'<figure><img src="{p}.svg" width="200" height="200" alt="{label}"><figcaption>{label}</figcaption></figure>' for p,label in [('origin-a','Upper source'),('origin-b','Lower source'),('mark-primary','Merged identity')])+'''</div><div class="geometry-layout"><figure><img class="grid" src="construction.svg" width="400" height="400" alt="Actual Bézier controls and curved source overlap"><figcaption>Actual curve controls and shared overlap</figcaption></figure><figure class="opening"><img src="opening.svg" width="180" height="320" alt="Enlarged opening and non-parallel terminal curves"><figcaption>Opening close-up · same final contour</figcaption></figure></div><p class="note">The mark is drawn directly as SVG curves. Aqua is the shared region of the upper and lower source forms. No typeface glyph is used in the symbol.</p><p><a href="../../confluence-primary/01/">Primary foundation: 01 Elegant Flow ↗</a></p></section>'''+micro(k)+f'''<section class="black-proof paper"><h2>Pure black / primary silhouette</h2>{large(k,'black')}{sizes(k,'black')}{navbar('black')}</section><details class="downloads"><summary>Download primary sources</summary><ul>'''+''.join(f'<li>{c}: <a href="mark-{c}.svg" download>mark SVG</a> · <a href="identity-{c}.svg" download>navbar SVG</a> · <a href="mark-{c}-256.png" download>256px PNG</a></li>' for c in COLORS)+'''</ul></details><nav class="bottom-nav"><a href="../">Compare all three hybrids</a></nav></main>'''+footer('../')
def sheet(items,color):
 light=color=='light';bg='#F6F8FB' if light else '#08111F';fg='#647485' if light else '#9EADBD';line='#DCE4EC' if light else '#27394D'
 def text(t,x,y,z=12):return f'<text x="{x}" y="{y}" fill="{fg}" font-family="Inter,Arial,sans-serif" font-size="{z}">{t}</text>'
 s=f'<rect width="1200" height="780" fill="{bg}"/>'+text('COVAN LABS / HYBRID CONFLUENCE C',32,36,14)+text('01’s elegance + restrained 03 personality + a touch of 02 precision.',32,62)
 for i,(v,d) in enumerate(items):
  x=32+i*384;s+=f'<rect x="{x}" y="90" width="368" height="620" rx="12" fill="none" stroke="{line}"/>'+text(v['id'].upper()+' / '+v['label'],x+24,124)
  s+=f'<g transform="translate({x+56} 150) scale(2.56)">{mark(d,color,"m"+v["id"])}</g>'+text('256px',x+24,430,10)
  for dx,z in [(62,128),(224,64)]:s+=f'<g transform="translate({x+dx} {540-z/2}) scale({z/100})">{mark(d,color,"s"+v["id"]+str(z))}</g>'+text(str(z)+'px',x+dx,620,10)
  s+=f'<g transform="translate({x+(368-WIDTH)/2} 650)">{lockup(d,color,"l"+v["id"])}</g>'
 s+=text('Three hybrids · 256 / 128 / 64px · Actual navbar lockups · No final selection',32,752)
 return svg(1200,780,s,'Three hybrid Confluence C studies, 256 128 64px and navbar size')
def main():
 items=[];records=[]
 for v in G['VARIANTS']:
  d=G['construction'](v);items.append((v,d));folder=OUT/v['id'];folder.mkdir(exist_ok=True)
  for c in COLORS:
   (folder/f'mark-{c}.svg').write_text(svg(100,100,mark(d,c),v['label']+' / '+c))
   (folder/f'identity-{c}.svg').write_text(svg(WIDTH,40,lockup(d,c),'Covan Labs'))
  for key,name,c in [('origin_a','origin-a','#F4F7FA'),('origin_b','origin-b','#F4F7FA'),('confluence','overlap','#39C6C8')]:
   (folder/f'{name}.svg').write_text(svg(100,100,f'<path d="{d[key]}" fill="{c}"/>',name))
  (folder/'construction.svg').write_text(grid(d));(folder/'opening.svg').write_text(svg(180,320,mark(d,'white'),'Opening close-up','60 15 32 70'));(folder/'index.html').write_text(detail(v,d));records.append({**v,**d})
 (OUT/'index.html').write_text(gallery(items))
 for c in ('white','primary','light'):(OUT/f'comparison-{c}.svg').write_text(sheet(items,c))
 (OUT/'manifest.json').write_text(json.dumps({'status':'three hybrid refinements; no final selection; micro deferred','concept':'Confluence C — two origins forming one identity','primary_sizes':[64,128,256],'secondary_reference_sizes':[16,24],'micro_created':False,'wordmark':{'family':'Inter','Covan':600,'Labs':425,'size':24,'mark_box':36,'width':WIDTH},'variants':records},indent=2)+'\n')
 print('Built H1, H2 and H3; no Micro C generated.')
if __name__=='__main__':main()
