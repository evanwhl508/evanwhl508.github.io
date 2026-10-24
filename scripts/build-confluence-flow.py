#!/usr/bin/env python3
"""Build the three Curved Confluence studies, using existing outlined supporting type."""
from pathlib import Path
import runpy,json,html,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'logo/confluence-flow';OUT.mkdir(exist_ok=True)
G=runpy.run_path(str(ROOT/'scripts/confluence-flow-geometry.py'));xy=G['xy'];path=G['path']
NS={'s':'http://www.w3.org/2000/svg'}
TYPE=ET.parse(ROOT/'logo/confluence/02/identity-white.svg').getroot()
WORD_PATHS=[p.get('d') for p in TYPE.findall('s:g',NS)[-1].findall('s:path',NS)]
WIDTH=round(float(TYPE.get('viewBox').split()[2])+6,2)
COLORS={'white':'#FFFFFF','navy':'#08111F','black':'#000000','primary':'#F4F7FA','light':'#08111F'}
NAVY='#08111F';AQUA='#39C6C8';SILVER='#F4F7FA'
def svg(w,h,content,title,viewbox=None):
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="{viewbox or f"0 0 {w} {h}"}" role="img" aria-label="{html.escape(title)}"><title>{html.escape(title)}</title>{content}</svg>\n'
def mark(d,color,uid='ink'):
 fill=COLORS[color]
 if color in ('primary','light'):
  # One contour is rasterized once. The pattern is the exact source overlap.
  return f'<defs><pattern id="{uid}" width="100" height="100" patternUnits="userSpaceOnUse"><rect width="100" height="100" fill="{fill}"/><path d="{d["confluence"]}" fill="{AQUA}"/></pattern></defs><path d="{d["merged"]}" fill="url(#{uid})"/>'
 return f'<path d="{d["merged"]}" fill="{fill}"/>'
def lockup(d,color,uid='lock'):
 return f'<g transform="translate(0 2) scale(.36)">{mark(d,color,uid)}</g><g transform="translate(6 0)" fill="{COLORS[color]}">'+''.join(f'<path d="{p}"/>' for p in WORD_PATHS)+'</g>'
def grid(d):
 s=f'<rect width="100" height="100" fill="{NAVY}"/><g stroke="#27394D" stroke-width=".2">'+''.join(f'<path d="M{x} 0V100M0 {x}H100"/>' for x in range(0,101,10))+'</g>'
 s+=f'<g opacity=".17">{mark(d,"primary")}</g>'
 for q in d['segments']:
  s+=f'<path d="M{xy(q[0])}L{xy(q[1])}M{xy(q[2])}L{xy(q[3])}" stroke="#9EADBD" stroke-width=".25" fill="none"/>'
  for p in q[1:3]:s+=f'<circle cx="{p[0]}" cy="{p[1]}" r=".45" fill="#9EADBD"/>'
 s+=f'<path d="{d["merged"]}" fill="none" stroke="{SILVER}" stroke-width=".5"/>'
 for seam in ('upper_seam','lower_seam'):s+=f'<path d="{path([d[seam]])}" fill="none" stroke="{AQUA}" stroke-width=".55"/>'
 for x,y in (d['outer_join'],d['inner_join']):s+=f'<path d="M{x} {y-8}v16" stroke="{AQUA}" stroke-width=".3" stroke-dasharray="1 1"/><circle cx="{x}" cy="{y}" r=".7" fill="{AQUA}"/>'
 return svg(400,400,s,'Actual cubic construction, curved overlap boundaries and shared spine tangents','0 0 100 100')
def head(title,depth=''):
 return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{title} · Covan Labs</title><link rel="stylesheet" href="{depth}review.css"><link rel="icon" href="{depth}a/mark-primary.svg"></head><body><a class="skip" href="#main">Skip to content</a>'
def footer(depth=''):
 return f'<footer><p>Three refinements · No final selection</p><a href="{depth}covan-curved-confluence.zip" download>Download SVG + PNG proofs</a><a href="/">Studio website</a></footer></body></html>'
def sizes(k,color,prefix=''):
 return '<div class="sizes">'+''.join(f'<figure><img src="{prefix}mark-{color}-{z}.png" width="{z}" height="{z}" alt="{k.upper()}, {color}, {z}px"><figcaption>{z}px</figcaption></figure>' for z in (16,24,32,64))+'</div>'
def navbar(color,prefix=''):
 return f'<div class="navbar"><img src="{prefix}identity-{color}.svg" width="{WIDTH}" height="40" alt="Covan Labs, actual navbar size"><span>Products</span><span>About</span></div><p class="caption">36px mark box · 24px Inter · Covan 600 / Labs 425</p>'
def detail(v,d):
 k=v['id'];panels=[]
 for color,label in [('white','Monochrome / pure white'),('primary','Curved confluence / two-color'),('navy','Monochrome / pure navy'),('light','Curved confluence / light')]:
  panels.append(f'<section class="proof {"paper" if color in ("navy","light") else "ink"}"><h2>{label}</h2><img class="large" src="mark-{color}.svg" width="256" height="256" alt="{v["label"]}, {label}">{sizes(k,color)}{navbar(color)}</section>')
 parts=''.join(f'<figure><img src="{p}.svg" width="200" height="200" alt="{alt}"><figcaption>{label}</figcaption></figure>' for p,label,alt in [('origin-a','Upper origin','Upper source ribbon, including its overlap'),('origin-b','Lower origin','Lower source ribbon, including its overlap'),('mark-primary','Merged identity','Union of the two sources; aqua is their intersection')])
 return head('Curved Confluence / '+v['label'],'../')+f'''<main id="main"><nav class="top-nav"><a href="../">← All three refinements</a><span>{k.upper()} / {v['label']}</span></nav><header class="detail-heading"><p class="eyebrow">Curved Confluence C / {k.upper()}</p><h1>{v['label']}</h1><p>Judge the silhouette and real-size lockup first.</p></header><div class="proof-grid">{''.join(panels)}</div>
<section class="explanation"><header><p class="eyebrow">Signature opening</p><h2>A restrained reach. A generous return.</h2><p>{v['description']}</p></header><div class="geometry-layout"><figure class="opening"><img src="opening.svg" width="180" height="280" alt="Enlarged terminal relationship"><figcaption>Negative space formed by the actual outline</figcaption></figure><div><h3>One open passage</h3><p>The lighter upper terminal and fuller lower return point in different directions. Their inward and outward curves give the opening its character. The mark still reads directly as a C.</p><p>The proportions follow Confluence study 02, with a restrained influence from 04. The contours are now drawn as cubic curves, with optical corrections through the spine, crown and lower sweep.</p><a href="../../confluence/02/">View proportion reference 02 ↗</a></div></div></section>
<section class="explanation"><header><p class="eyebrow">Two origins / one continuous identity</p><h2>The confluence is a shared curve.</h2><p>The two source ribbons overlap through the spine. Both use the same tangent-continuous inner and outer contours through that transition. Aqua is their exact shared region, bounded by two curved seams.</p></header><div class="origins">{parts}</div><div class="geometry-layout"><figure><img class="grid" src="construction.svg" width="400" height="400" alt="Cubic controls, curved overlap seams and shared tangents"><figcaption>Silver: contour controls. Aqua: overlap seams.<br>Dotted verticals: shared tangents through the spine.</figcaption></figure><div><h3>Optically drawn</h3><p>The left spine is slightly stronger, the crown lighter and the lower sweep fuller. These are local corrections of approximately 5–8% relative to study 02, rather than a uniform stroke or a pair of concentric circles.</p><p>The 6–10% aqua target is measured against the filled area. White represents the stable structure; aqua marks the short transition shared by both origins.</p><p class="note">The mark is independent of type. All five color proofs use exactly the same contour.</p><a href="construction.svg" download>Download construction SVG</a></div></div><div class="transition-proof"><figure><img src="transition.svg" width="280" height="240" alt="Enlarged actual curved overlap"><figcaption>Curved transition detail</figcaption></figure><figure><img src="overlap.svg" width="200" height="200" alt="Exact intersection of the two source ribbons"><figcaption>Shared region only · same coordinates</figcaption></figure></div></section>
<section class="black-proof paper"><h2>Pure black / monochrome integrity</h2><img src="mark-black.svg" width="200" height="200" alt="{v['label']} in pure black">{sizes(k,'black')}{navbar('black')}</section><details class="downloads"><summary>SVG sources and transparent PNGs</summary><p>Native PNG sizes: 16, 24, 32, 64 and 512px.</p><ul>'''+''.join(f'<li>{color}: <a href="mark-{color}.svg" download>mark SVG</a> · <a href="identity-{color}.svg" download>navbar lockup SVG</a> · <a href="mark-{color}-512.png" download>512px PNG</a></li>' for color in COLORS)+f'''</ul><p><a href="origin-a.svg" download>Upper source</a> · <a href="origin-b.svg" download>Lower source</a> · <a href="overlap.svg" download>Exact overlap</a></p></details><nav class="bottom-nav"><a href="../">All three</a><a href="../{dict(a='b',b='c',c='a')[k]}/">Next refinement →</a></nav></main>'''+footer('../')
def gallery(items):
 cards=[]
 for v,d in items:
  k=v['id'];cards.append(f'<article class="candidate"><header><span>{k.upper()}</span><span>{v["label"]}</span></header><a class="hero-mark" href="{k}/" aria-label="Inspect {v["label"]}"><img src="{k}/mark-white.svg" width="200" height="200" alt="{v["label"]} in monochrome"></a><div class="color-mark"><img src="{k}/mark-primary.svg" width="160" height="160" alt="{v["label"]} with curved aqua confluence"></div><div class="compact-lock"><img src="{k}/identity-primary.svg" width="{WIDTH}" height="40" alt="Covan Labs at navbar size"></div>{sizes(k,"primary",k+"/")}<a class="inspect" href="{k}/">Construction, opening &amp; proofs ↗</a></article>')
 return head('Curved Confluence C — three refinements')+'''<main id="main"><header class="page-heading"><p class="eyebrow">Covan Labs / Curved Confluence C</p><h1>Proportion. Flow. One identity.</h1><p><strong>A / Balanced is the selected base.</strong> Continue to <a href="../confluence-finish/">A1–A3 optical finishing</a>.</p><p>Three refinements from study 02, with a restrained influence from 04.<br>Monochrome first. No final mark selected.</p></header><div class="candidate-grid">'''+''.join(cards)+'''</div><section class="overview-note"><h2>Two curves, one shared transition.</h2><p>The source ribbons now merge along shared tangents. Their overlap creates the curved aqua transition. Optical weight corrections and non-parallel terminal directions shape the open space within the C.</p><p>Each refinement includes separate source curves, the merged outline, construction controls, dark and light versions, pure white/navy/black proofs, and native 16 / 24 / 32 / 64px tests.</p><div class="links"><a href="comparison-white.png">Monochrome sheet</a><a href="comparison-primary.png">Two-color sheet</a><a href="comparison-light.png">Light-background sheet</a></div><p class="caption">References: <a href="../confluence/02/">study 02</a> · <a href="../confluence/04/">study 04</a>.</p></section></main>'''+footer()
def sheet(items,color):
 light=color=='light';bg='#F6F8FB' if light else NAVY;fg='#647485' if light else '#9EADBD';border='#DCE4EC' if light else '#27394D'
 def text(t,x,y,size=12):return f'<text x="{x}" y="{y}" fill="{fg}" font-family="Inter,Arial,sans-serif" font-size="{size}">{html.escape(t)}</text>'
 s=f'<rect width="1200" height="660" fill="{bg}"/>'+text('COVAN LABS / CURVED CONFLUENCE C',32,36,14)+text('Three refinements. No final selection.',32,62)
 for i,(v,d) in enumerate(items):
  x=32+i*384;s+=f'<rect x="{x}" y="90" width="368" height="500" rx="12" fill="none" stroke="{border}"/>'+text(v['id'].upper()+' / '+v['label'],x+24,124)
  s+=f'<g transform="translate({x+64} 148) scale(2.4)">{mark(d,color,"m"+v["id"])}</g>'
  s+=f'<g transform="translate({x+(368-WIDTH)/2} 410)">{lockup(d,color,"l"+v["id"])}</g>'
  for xx,z in [(74,16),(119,24),(169,32),(225,64)]:s+=f'<g transform="translate({x+xx} {520-z/2}) scale({z/100})">{mark(d,color,"s"+v["id"]+str(z))}</g>'+text(str(z)+'px',x+xx,569,10)
 s+=text('Curved source overlap · Optical contour corrections · Inter 600 / 425 · Native size proofs',32,634)
 return svg(1200,660,s,'Balanced, Flowing and Minimal: Curved Confluence C refinements')
def main():
 items=[];records=[]
 for v in G['VARIANTS']:
  d=G['construction'](v);items.append((v,d));folder=OUT/v['id'];folder.mkdir(exist_ok=True)
  for color in COLORS:
   (folder/f'mark-{color}.svg').write_text(svg(100,100,mark(d,color),v['label']+' / '+color))
   (folder/f'identity-{color}.svg').write_text(svg(WIDTH,40,lockup(d,color),'Covan Labs'))
  for key,name,color in [('origin_a','origin-a',SILVER),('origin_b','origin-b',SILVER),('confluence','overlap',AQUA)]:
   (folder/f'{name}.svg').write_text(svg(100,100,f'<path d="{d[key]}" fill="{color}"/>',name))
  (folder/'construction.svg').write_text(grid(d));(folder/'opening.svg').write_text(svg(180,280,mark(d,'white'),'Opening detail','63 22 30 56'))
  (folder/'transition.svg').write_text(svg(280,240,mark(d,'primary'),'Curved source overlap detail','7 37 28 24'))
  (folder/'index.html').write_text(detail(v,d));records.append({**v,**d})
 (OUT/'index.html').write_text(gallery(items))
 for color in ('white','primary','light'):(OUT/f'comparison-{color}.svg').write_text(sheet(items,color))
 (OUT/'manifest.json').write_text(json.dumps({'status':'three refinements; none final','concept':'Two origins. One continuous identity.','primary_reference':'Confluence 02','secondary_reference':'Confluence 04, restrained opening influence','wordmark':{'family':'Inter','Covan':600,'Labs':425,'size':24,'mark_box':36,'wordmark_origin':50,'prior_origin':44,'navbar_width':WIDTH},'aqua_target_percent':[6,10],'variants':records},indent=2)+'\n')
 print('Built exactly three curved-confluence refinements.')
if __name__=='__main__':main()
