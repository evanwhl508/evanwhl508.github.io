#!/usr/bin/env python3
"""The selected H1 master, with only two final polish alternatives."""
from pathlib import Path
import json,runpy
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'logo/h1-polish';OUT.mkdir(exist_ok=True)
B=runpy.run_path(str(ROOT/'scripts/build-confluence-flow.py'));G=runpy.run_path(str(ROOT/'scripts/h1-polish-geometry.py'))
svg,mark,grid=B['svg'],B['mark'],B['grid'];WIDTH=B['WIDTH'];COLORS=B['COLORS']
def lockup(d,c,extra=0,uid='lock'):
 return f'<g transform="translate(0 2) scale(.36)">{mark(d,c,uid)}</g><g transform="translate({6+extra} 0)" fill="{COLORS[c]}">'+''.join(f'<path d="{p}"/>' for p in B['WORD_PATHS'])+'</g>'
def head(t,depth=''):
 return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{t} · Covan Labs</title><link rel="stylesheet" href="{depth}review.css"><link rel="icon" href="/logo/favicon-32.png"></head><body><a class="skip" href="#main">Skip to content</a>'
def footer(depth=''):
 return f'<footer><p>H1 master selected · Final polish pending review</p><a href="{depth}covan-h1-final-polish.zip" download>Download SVG + PNG proofs</a><a href="/">Studio website</a></footer></body></html>'
def large(k,c,prefix=''):
 return f'<figure class="large-proof"><img class="native-large" src="{prefix}mark-{c}-256.png" width="256" height="256" alt="{k}, {c}, 256px"><figcaption>256px</figcaption></figure>'
def sizes(k,c,prefix=''):
 return '<div class="sizes primary-sizes">'+''.join(f'<figure><img src="{prefix}mark-{c}-{n}.png" width="{n}" height="{n}" alt="{k}, {c}, {n}px"><figcaption>{n}px</figcaption></figure>' for n in (128,64))+'</div>'
def spacing(c,prefix=''):
 return '<div class="spacing-proof">'+''.join(f'<figure><figcaption>{label}</figcaption><img src="{prefix}identity-{c}{suffix}.svg" width="{WIDTH+extra}" height="40" alt="Covan Labs, {label}"></figure>' for suffix,extra,label in [('',0,'Current spacing'),('-roomier',2,'+2px wordmark spacing')])+'</div>'
def gallery(items):
 cards=[]
 for v,d in items:
  k=v['id'];cards.append(f'<article class="candidate"><header><span>{v["label"]}</span></header>{large(k,"white",k+"/")}<div class="proof-divider"></div>{large(k,"primary",k+"/")}{sizes(k,"primary",k+"/")}{spacing("primary",k+"/")}<a class="inspect" href="{k}/">Light, monochrome &amp; optical details ↗</a></article>')
 return head('H1 — final optical polish')+'''<main id="main"><header class="page-heading"><p class="eyebrow">Covan Labs / Selected H1 master</p><h1>Final optical finishing.</h1><p>The unchanged H1 benchmark and two polish alternatives.<br>Compare at 256, 128 and 64px, then test both navbar spacings.</p></header><div class="candidate-grid">'''+''.join(cards)+'''</div><section class="overview-note"><h2>The same master, lightly polished.</h2><p>Polish A refines the confluence curves while preserving H1’s silhouette and aqua area. Polish B adds a small lower-tip reduction and an upward confluence adjustment. Both keep H1’s tall, open proportions.</p><p>The second lockup adds 2px between the mark and wordmark. All type remains Inter 600 / 425 at the same size. No favicon optimization is included.</p><div class="links"><a href="comparison-white.png">Monochrome sheet</a><a href="comparison-primary.png">Aqua sheet</a><a href="comparison-light.png">Light-background sheet</a></div><a href="../confluence-hybrid/h1/">Selected H1 reference ↗</a></section></main>'''+footer()
def detail(v,d):
 k=v['id'];panels=[]
 for c,label in [('white','Pure white'),('primary','Cool white + aqua'),('navy','Pure navy'),('light','Navy + aqua')]:
  panels.append(f'<section class="proof {"paper" if c in ("navy","light") else "ink"}"><h2>{label}</h2>{large(k,c)}{sizes(k,c)}{spacing(c)}<p class="caption">Actual navbar scale · 36px mark box · Inter 600 / 425</p></section>')
 return head(v['label'],'../')+f'''<main id="main"><nav class="top-nav"><a href="../">← H1 and two polish alternatives</a><span>Selected H1</span></nav><header class="detail-heading"><p class="eyebrow">Final optical finishing</p><h1>{v['label']}</h1><p>{v['description']}</p></header><div class="proof-grid">{''.join(panels)}</div><section class="explanation"><header><h2>Optical details</h2><p>The confluence remains the actual overlap of the two source curves. Its integrated filled area is held constant across the benchmark and both alternatives.</p></header><div class="geometry-layout"><figure><img src="confluence-detail.svg" width="240" height="300" alt="Enlarged confluence on the actual H1 contour"><figcaption>Confluence detail · same source geometry</figcaption></figure><figure><img src="terminal-detail.svg" width="300" height="240" alt="Lower tip detail with the measurement boundary at x equals 65"><figcaption>Lower-tip detail · dotted line marks the measured region</figcaption></figure></div><p class="note">Polish B reduces the filled area to the right of the dotted line by 2.5%. Only the lower terminal face and adjoining inner return change; the outer body arcs stay fixed. The confluence lift is 0.5 units in the 100-unit design space, equivalent to 1.28px at 256px.</p><details class="downloads"><summary>Source curves and controls</summary><div class="origins">'''+''.join(f'<figure><img src="{p}.svg" width="200" height="200" alt="{label}"><figcaption>{label}</figcaption></figure>' for p,label in [('origin-a','Upper source'),('origin-b','Lower source'),('mark-primary','Merged master')])+'''</div><img class="grid" src="construction.svg" width="400" height="400" alt="Actual control points and source overlap"></details></section>'''+f'''<section class="black-proof paper"><h2>Pure black</h2>{large(k,'black')}{sizes(k,'black')}{spacing('black')}</section><details class="downloads"><summary>Download vectors and native PNGs</summary><ul>'''+''.join(f'<li>{c}: <a href="mark-{c}.svg" download>mark SVG</a> · <a href="identity-{c}.svg" download>current lockup</a> · <a href="identity-{c}-roomier.svg" download>+2px lockup</a> · <a href="mark-{c}-256.png" download>256px PNG</a></li>' for c in COLORS)+'''</ul></details></main>'''+footer('../')
def sheet(items,c):
 light=c=='light';bg='#F6F8FB' if light else '#08111F';fg='#647485' if light else '#9EADBD';border='#DCE4EC' if light else '#27394D'
 def text(t,x,y,z=12):return f'<text x="{x}" y="{y}" fill="{fg}" font-family="Inter,Arial,sans-serif" font-size="{z}">{t}</text>'
 s=f'<rect width="1200" height="880" fill="{bg}"/>'+text('COVAN LABS / H1 FINAL OPTICAL POLISH',32,36,14)+text('One selected master. Two polish alternatives. No new silhouette families.',32,62)
 for i,(v,d) in enumerate(items):
  x=32+384*i;s+=f'<rect x="{x}" y="90" width="368" height="724" rx="12" fill="none" stroke="{border}"/>'+text(v['label'],x+24,124)
  s+=f'<g transform="translate({x+56} 150) scale(2.56)">{mark(d,c,"m"+v["id"])}</g>'+text('256px',x+24,430,10)
  for dx,n in [(62,128),(224,64)]:s+=f'<g transform="translate({x+dx} {540-n/2}) scale({n/100})">{mark(d,c,"s"+v["id"]+str(n))}</g>'+text(str(n)+'px',x+dx,620,10)
  for y,extra,label in [(652,0,'Current spacing'),(736,2,'+2px wordmark spacing')]:
   s+=text(label,x+24,y-8,10)+f'<g transform="translate({x+(368-WIDTH-2)/2} {y})">{lockup(d,c,extra,"l"+v["id"]+str(extra))}</g>'
 s+=text('H1 master selected · 256 / 128 / 64px · Actual navbar lockups · Optical differences are intentionally subtle',32,856)
 return svg(1200,880,s,'H1 benchmark, Polish A and Polish B with current and roomier navbar lockups')
def main():
 items=[];records=[]
 for v in G['VARIANTS']:
  d=G['construction'](v);items.append((v,d));folder=OUT/v['id'];folder.mkdir(exist_ok=True)
  for c in COLORS:
   (folder/f'mark-{c}.svg').write_text(svg(100,100,mark(d,c),v['label']+' / '+c))
   for extra,suffix in [(0,''),(2,'-roomier')]:
    (folder/f'identity-{c}{suffix}.svg').write_text(svg(WIDTH+extra,40,lockup(d,c,extra),'Covan Labs'))
  for key,name,c in [('origin_a','origin-a','#F4F7FA'),('origin_b','origin-b','#F4F7FA'),('confluence','overlap','#39C6C8')]:
   (folder/f'{name}.svg').write_text(svg(100,100,f'<path d="{d[key]}" fill="{c}"/>',name))
  (folder/'construction.svg').write_text(grid(d));(folder/'confluence-detail.svg').write_text(svg(240,300,mark(d,'primary'),'Confluence detail','11 42 22 28'))
  (folder/'terminal-detail.svg').write_text(svg(300,240,mark(d,'white')+'<path d="M65 62V88" stroke="#9EADBD" stroke-width=".2" stroke-dasharray=".5 .6"/>','Lower-tip measurement region','62 64 26 21'))
  (folder/'index.html').write_text(detail(v,d));records.append({**v,**d})
 (OUT/'index.html').write_text(gallery(items))
 for c in ('white','primary','light'):(OUT/f'comparison-{c}.svg').write_text(sheet(items,c))
 (OUT/'manifest.json').write_text(json.dumps({'status':'H1 selected as master; Polish A/B pending review','master':'H1 Elegant Hybrid','primary_sizes':[64,128,256],'micro_created':False,'wordmark':{'family':'Inter','Covan':600,'Labs':425,'size':24,'mark_box':36,'width':WIDTH,'current_origin':50,'roomier_origin':52,'additional_spacing':2},'variants':records},indent=2)+'\n')
 print('Built exact H1 benchmark and only Polish A / Polish B.')
if __name__=='__main__':main()
