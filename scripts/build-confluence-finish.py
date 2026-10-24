#!/usr/bin/env python3
"""A1–A3 optical finishing proofs. Reuses the selected identity's outlined wordmark."""
from pathlib import Path
import runpy,json,html
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'logo/confluence-finish';OUT.mkdir(exist_ok=True)
B=runpy.run_path(str(ROOT/'scripts/build-confluence-flow.py'));G=runpy.run_path(str(ROOT/'scripts/confluence-finish-geometry.py'))
svg,mark,lockup,grid=B['svg'],B['mark'],B['lockup'],B['grid'];WIDTH=B['WIDTH'];COLORS=B['COLORS']
def head(title,depth=''):
 return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{title} · Covan Labs</title><link rel="stylesheet" href="{depth}review.css"><link rel="icon" href="{depth}a1/mark-primary.svg"></head><body><a class="skip" href="#main">Skip to content</a>'
def footer(depth=''):
 return f'<footer><p>Option A selected · Final optical variant pending review</p><a href="{depth}covan-a-optical-refinements.zip" download>Download SVG + PNG proofs</a><a href="/">Studio website</a></footer></body></html>'
def sizes(k,c,prefix=''):
 return '<div class="sizes">'+''.join(f'<figure><img src="{prefix}mark-{c}-{n}.png" width="{n}" height="{n}" alt="{k.upper()}, {c}, {n}px"><figcaption>{n}px</figcaption></figure>' for n in (16,24,32,64))+'</div>'
def large(k,c,prefix=''):
 return f'<figure class="large-proof"><img class="native-large" src="{prefix}mark-{c}-256.png" width="256" height="256" alt="{k.upper()}, {c}, native 256px"><figcaption>256px</figcaption></figure>'
def nav(c,prefix=''):
 return f'<div class="navbar"><img src="{prefix}identity-{c}.svg" width="{WIDTH}" height="40" alt="Covan Labs at actual navbar size"></div>'
def tabs(k,prefix=''):
 s='<div class="tab-proofs"><p class="caption">Browser-tab previews · native 16px favicons</p>'
 for c,label,theme in [('primary','Dark','dark'),('light','Light','light')]:
  s+=f'<div class="tab-strip tab-{theme}" aria-label="{label} browser-tab preview"><div class="browser-tab"><img src="{prefix}mark-{c}-16.png" width="16" height="16" alt="{k.upper()} favicon"><span>Covan Labs</span><span class="close" aria-hidden="true">×</span></div><span class="plus" aria-hidden="true">+</span></div>'
 s+=f'<div class="tab-links"><a href="{prefix}tab-dark.html" target="_blank" rel="noopener">Open dark favicon test ↗</a><a href="{prefix}tab-light.html" target="_blank" rel="noopener">Open light favicon test ↗</a></div></div>'
 return s
def gallery(items):
 cards=[]
 for v,d in items:
  k=v['id'];cards.append(f'<article class="candidate"><header><span>{k.upper()}</span><span>{v["label"]}</span></header>{large(k,"white",k+"/")}{sizes(k,"white",k+"/")}<div class="proof-divider"></div>{large(k,"primary",k+"/")}{sizes(k,"primary",k+"/")}<div class="compact-lock"><img src="{k}/identity-primary.svg" width="{WIDTH}" height="40" alt="{k.upper()} navbar lockup"></div>{tabs(k,k+"/")}<a class="inspect" href="{k}/">Light, monochrome &amp; detail proofs ↗</a></article>')
 return head('Selected A — optical finishing')+'''<main id="main"><header class="page-heading"><p class="eyebrow">Covan Labs / Selected A</p><h1>Finishing the identity.</h1><p>Previous finishing round. Continue to the <a href="../confluence-primary/">current primary-mark exploration</a> and responsive identity approach.</p><p>One selected base. Three optical refinements.<br>A1 preserves the benchmark; A2 refines the confluence; A3 refines the silhouette.</p></header><div class="candidate-grid">'''+''.join(cards)+'''</div><section class="overview-note"><h2>Small changes. Direct comparison.</h2><p>A1 uses the exact selected geometry. A2 changes only the curved overlap. A3 keeps that overlap, tightens the upper terminal slightly and reduces the mark’s width by 2.5%. The wordmark stays consistent across all three.</p><p>Every size proof is shown at its native dimensions: 16, 24, 32, 64 and 256px. Tab previews use the exported 16px favicon; the test links open a document with that actual favicon.</p><div class="links"><a href="comparison-white.png">Monochrome comparison</a><a href="comparison-primary.png">Aqua comparison</a><a href="comparison-light.png">Light-background comparison</a></div><a href="../confluence-flow/a/">Selected A reference ↗</a></section></main>'''+footer()
def detail(v,d):
 k=v['id'];panels=[]
 for c,label in [('white','Pure white'),('primary','Cool white + aqua'),('navy','Pure navy'),('light','Navy + aqua')]:
  panels.append(f'<section class="proof {"paper" if c in ("navy","light") else "ink"}"><h2>{label}</h2>{large(k,c)}{sizes(k,c)}{nav(c)}<p class="caption">36px mark box · Inter 600 / 425</p></section>')
 return head(k.upper()+' — '+v['label'],'../')+f'''<main id="main"><nav class="top-nav"><a href="../">← Compare A1–A3</a><span>Selected A / {k.upper()}</span></nav><header class="detail-heading"><p class="eyebrow">Optical refinement {k.upper()}</p><h1>{v['label']}</h1><p>{v['description']}</p></header><div class="proof-grid">{''.join(panels)}</div><section class="tab-section"><h2>Favicon in context</h2>{tabs(k)}<p class="caption">These are tab-surface previews. Test pages load the real 16px favicon; browser chrome follows your browser’s own theme.</p></section><section class="explanation"><header><h2>Confluence and terminal detail</h2><p>{v['description']} The final contour and the overlap are both drawn from the selected A source geometry.</p></header><div class="transition-proof"><figure><img src="transition.svg" width="280" height="240" alt="Actual curved confluence enlarged"><figcaption>Confluence detail</figcaption></figure><figure class="opening"><img src="opening.svg" width="180" height="280" alt="Actual upper and lower terminal detail"><figcaption>Opening detail</figcaption></figure></div><details class="downloads"><summary>Construction curves</summary><div class="origins">'''+''.join(f'<figure><img src="{p}.svg" width="200" height="200" alt="{label}"><figcaption>{label}</figcaption></figure>' for p,label in [('origin-a','Upper origin'),('origin-b','Lower origin'),('mark-primary','Merged identity')])+'''</div><img class="grid" src="construction.svg" width="400" height="400" alt="Actual contour controls, overlap curves and shared spine tangents"></details></section><section class="black-proof paper"><h2>Pure black</h2>'''+large(k,'black')+sizes(k,'black')+nav('black')+'''</section><details class="downloads"><summary>Download source files</summary><ul>'''+''.join(f'<li>{c}: <a href="mark-{c}.svg" download>mark SVG</a> · <a href="identity-{c}.svg" download>lockup SVG</a> · <a href="mark-{c}-256.png" download>256px PNG</a></li>' for c in COLORS)+'''</ul></details></main>'''+footer('../')
def testpage(v,theme):
 color='primary' if theme=='dark' else 'light';bg='#08111F' if theme=='dark' else '#F6F8FB';fg='#F4F7FA' if theme=='dark' else '#08111F'
 return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="{bg}"><title>Covan Labs · {v["id"].upper()}</title><link rel="icon" type="image/png" sizes="16x16" href="mark-{color}-16.png"><style>body{{margin:48px 24px;background:{bg};color:{fg};font:16px/1.6 system-ui}}main{{max-width:720px;margin:auto}}a{{color:inherit}}a:focus-visible{{outline:2px solid #39C6C8;outline-offset:4px}}img{{display:block;margin:24px 0}}</style></head><body><main><h1>{v["id"].upper()} · {theme.capitalize()} favicon test</h1><p>The browser tab uses the actual 16px PNG shown below. Browser chrome follows your browser’s theme.</p><img src="mark-{color}-16.png" width="16" height="16" alt="Actual 16px favicon"><a href="./">Return to refinement</a></main></body></html>'
def sheet(items,color):
 # Reuse the established comparison grid and exact supporting type.
 s=B['sheet'](items,color)
 s=s.replace('CURVED CONFLUENCE C','SELECTED A / OPTICAL FINISHING').replace('Three refinements. No final selection.','A1 benchmark / A2 confluence / A3 silhouette.').replace('Curved source overlap · Optical contour corrections · Inter 600 / 425 · Native size proofs','Selected A · Native 16 / 24 / 32 / 64 / 256px · Inter 600 / 425')
 s=s.replace('scale(2.4)','scale(2.56)')
 # Center the 256px box in the existing 368px column.
 for i in range(3):s=s.replace(f'translate({32+i*384+64} 148)',f'translate({32+i*384+56} 140)')
 return s
def main():
 items=[];records=[]
 for v in G['VARIANTS']:
  d=G['construction'](v);items.append((v,d));folder=OUT/v['id'];folder.mkdir(exist_ok=True)
  for c in COLORS:
   (folder/f'mark-{c}.svg').write_text(svg(100,100,mark(d,c),v['id'].upper()+' / '+c))
   (folder/f'identity-{c}.svg').write_text(svg(WIDTH,40,lockup(d,c),'Covan Labs'))
  for key,name,color in [('origin_a','origin-a','#F4F7FA'),('origin_b','origin-b','#F4F7FA'),('confluence','overlap','#39C6C8')]:
   (folder/f'{name}.svg').write_text(svg(100,100,f'<path d="{d[key]}" fill="{color}"/>',name))
  (folder/'construction.svg').write_text(grid(d));(folder/'transition.svg').write_text(svg(280,240,mark(d,'primary'),'Confluence detail','7 37 28 24'));(folder/'opening.svg').write_text(svg(180,280,mark(d,'white'),'Opening detail','63 22 30 56'))
  (folder/'index.html').write_text(detail(v,d))
  for theme in ('dark','light'):(folder/f'tab-{theme}.html').write_text(testpage(v,theme))
  records.append({**v,**d})
 (OUT/'index.html').write_text(gallery(items))
 for c in ('white','primary','light'):(OUT/f'comparison-{c}.svg').write_text(sheet(items,c))
 (OUT/'manifest.json').write_text(json.dumps({'status':'Option A selected as base; final optical refinement pending review','variants':records,'wordmark':{'family':'Inter','Covan':600,'Labs':425,'size':24,'mark_box':36,'wordmark_origin':50,'navbar_width':WIDTH},'native_sizes':[16,24,32,64,256],'tab_previews':'HTML tab-surface simulations using actual 16px PNGs; individual test pages load the real favicon'},indent=2)+'\n')
 print('Built A1, A2 and A3 only.')
if __name__=='__main__':main()
