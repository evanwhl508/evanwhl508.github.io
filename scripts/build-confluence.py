#!/usr/bin/env python3
"""Four Confluence C proofs. FontTools is used for supporting type ONLY."""
from pathlib import Path
import json,runpy,html
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'logo/confluence';OUT.mkdir(exist_ok=True)
G=runpy.run_path(str(ROOT/'scripts/confluence-geometry.py'));xy=G['xy']
COLORS={'white':'#FFFFFF','navy':'#08111F','black':'#000000','primary':'#F4F7FA','light':'#08111F','origin':'#F4F7FA'}
AQUA='#39C6C8';NAVY='#08111F';SILVER='#F4F7FA'
FONTS={w:instantiateVariableFont(TTFont(ROOT/'assets/fonts/InterVariable.woff2'),{'wght':w,'opsz':24},inplace=True) for w in (600,425)}
def lettering():
    paths=[];x=44
    for text,weight in [('Covan',600),('Labs',425)]:
        f=FONTS[weight];gs=f.getGlyphSet();cm=f.getBestCmap();scale=24/f['head'].unitsPerEm
        for ch in text:
            glyph=gs[cm[ord(ch)]];pen=SVGPathPen(gs,ntos=lambda n:f'{n:.4f}'.rstrip('0').rstrip('.'))
            glyph.draw(TransformPen(pen,(scale,0,0,-scale,x,28.5)));paths.append(pen.getCommands());x+=glyph.width*scale-.28
        if text=='Covan':x+=5.8
    return paths,round(x+2,2)
WORDS,LOCK_WIDTH=lettering()
def svg(w,h,content,label,viewbox=None):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="{viewbox or f"0 0 {w} {h}"}" role="img" aria-label="{html.escape(label)}"><title>{html.escape(label)}</title>{content}</svg>\n'
def mark(d,color,uid='fill'):
    fill=COLORS[color]
    if color in ('primary','light','origin'):
        zone=d['origin_zone' if color=='origin' else 'confluence_zone']
        # A single contour with a two-color pattern fill avoids seams or altered
        # edge coverage from layering duplicate antialiased outer silhouettes.
        return f'<defs><pattern id="{uid}" width="100" height="100" patternUnits="userSpaceOnUse"><rect width="100" height="100" fill="{fill}"/><path d="{zone}" fill="{AQUA}"/></pattern></defs><path d="{d["merged"]}" fill="url(#{uid})"/>'
    return f'<path d="{d["merged"]}" fill="{fill}"/>'
def lockup(d,color,uid='lock'):
    return f'<g transform="translate(0 2) scale(.36)">{mark(d,color,uid)}</g><g fill="{COLORS[color]}">'+''.join(f'<path d="{p}"/>' for p in WORDS)+'</g>'
def grid(d):
    lines=''.join(f'<path d="M{x} 0V100M0 {x}H100"/>' for x in range(0,101,10))
    s=f'<rect width="100" height="100" fill="{NAVY}"/><g stroke="#27394D" stroke-width=".25">{lines}</g><g opacity=".2">{mark(d,"primary")}</g>'
    for j,c in enumerate(d['circles']):
        s+=f'<circle cx="{c["cx"]}" cy="{c["cy"]}" r="{c["r"]}" fill="none" stroke="#9EADBD" stroke-width=".3"'+(' stroke-dasharray="1 1"' if j%2 else '')+'/>'
    s+=f'<path d="M{xy(d["outer_join"])}L{xy(d["inner_join"])}" stroke="{AQUA}" stroke-width=".55" stroke-dasharray="1 1"/>'
    s+=f'<path d="{d["merged"]}" fill="none" stroke="{SILVER}" stroke-width=".55"/>'
    for points,controls in [(list(reversed(d['upper_terminal'])),d['upper_controls']),(d['lower_terminal'],d['lower_controls'])]:
        s+=f'<path d="M{xy(points[0])}L{xy(controls[0])}M{xy(controls[1])}L{xy(points[1])}" fill="none" stroke="{AQUA}" stroke-width=".4"/>'
        for x,y in controls:s+=f'<circle cx="{x}" cy="{y}" r=".65" fill="{AQUA}"/>'
    for x,y in [d['outer_join'],d['inner_join']]:s+=f'<circle cx="{x}" cy="{y}" r=".9" fill="{AQUA}"/>'
    return svg(400,400,s,'True construction: source arcs, curved terminal handles and the shared join','0 0 100 100')
def head(title,depth=''):
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{title} · Covan Labs</title><link rel="stylesheet" href="{depth}review.css"><link rel="icon" href="{depth}01/mark-primary.svg"></head><body><a class="skip" href="#main">Skip to content</a>'
def footer(depth=''):
    return f'<footer><p>Four refinements · No final mark selected</p><a href="{depth}covan-confluence-c.zip" download>Download SVG + PNG proofs</a><a href="/">Studio website</a></footer></body></html>'
def sizes(k,color,prefix=''):
    return '<div class="sizes">'+''.join(f'<figure><img src="{prefix}mark-{color}-{z}.png" width="{z}" height="{z}" alt="Refinement {k}, {color}, {z}px"><figcaption>{z}px</figcaption></figure>' for z in (16,24,32,64))+'</div>'
def navbar(color,prefix=''):
    return f'<div class="navbar"><img src="{prefix}identity-{color}.svg" width="{LOCK_WIDTH}" height="40" alt="Covan Labs at actual navbar size"><span>Products</span><span>About</span></div><p class="caption">36px mark box · 24px Inter · Covan 600 / Labs 425</p>'
def detail(v,d):
    k=v['id'];panels=[]
    for color,label in [('white','Pure white'),('primary','Confluence / two-color'),('navy','Pure navy'),('light','Confluence / light')]:
        panels.append(f'<section class="proof {"paper" if color in ("navy","light") else "ink"}"><h2>{label}</h2><img class="large" src="mark-{color}.svg" width="256" height="256" alt="Refinement {k}: {label}">{sizes(k,color)}{navbar(color)}</section>')
    origins=''.join(f'<figure><img src="{p}.svg" width="200" height="200" alt="{alt}"><figcaption>{label}</figcaption></figure>' for p,label,alt in [('origin-a','Origin 1','Upper originating ribbon'),('origin-b','Origin 2','Lower originating ribbon'),('mark-primary','One continuous C','Merged C with aqua at the shared join')])
    return head(f'Confluence C / {k}','../')+f'''<main id="main"><nav class="top-nav"><a href="../">← All four refinements</a><span>Confluence C / {k}</span></nav><header class="detail-heading"><p class="eyebrow">Refinement {k} · from study {v['reference']}</p><h1>{v['label']}</h1><p>Judge the mark and its navbar lockup before the construction.</p></header><div class="proof-grid">{''.join(panels)}</div>
<section class="explanation"><header><p class="eyebrow">The signature gesture</p><h2>Two ends, one opening.</h2><p>{v['description']}</p></header><div class="geometry-layout"><figure class="opening"><img src="opening.svg" width="180" height="280" alt="Enlarged opening showing the complementary terminal curves"><figcaption>Opening detail · same final outline</figcaption></figure><div><h3>What changed</h3><p>The straight, matching cuts of study {v['reference']} are replaced by two custom cubic curves. Their relationship is visible in the finished silhouette. The circular body retains the reference’s balance and eccentric inner arcs.</p><p>The terminal relationship and the color perform different roles: the opening carries the signature; aqua locates the real meeting of the two source ribbons at the back.</p><a href="../../two-origin/{v['reference']}/">Compare reference study {v['reference']} ↗</a></div></div></section>
<section class="explanation"><header><p class="eyebrow">Construction</p><h2>Two origins. One continuous identity.</h2><p>The upper and lower ribbons meet across the back of the C. The internal joining line disappears in the merged outline. A short curved aqua section spans that join: structure becoming an active, shared identity.</p></header><div class="origins">{origins}</div><div class="geometry-layout"><figure><img class="grid" src="construction.svg" width="400" height="400" alt="Construction circles, Bézier handles and shared joining line"><figcaption>Solid circles: outer arcs. Dashed circles: inner arcs.<br>Aqua handles: terminal curves. Dotted aqua line: removed join.</figcaption></figure><div><h3>Drawn from geometry</h3><p>No font glyph is used in the mark. Two eccentric arc systems create the body; custom Bézier curves shape the opening. The unequal inner and outer centres preserve optical weight variation.</p><p>The aqua region follows the existing curved silhouette. It crosses both source ribbons, without a gap, overlap or detached block.</p><p class="note">Color represents confluence, not one colored half. The same outline is used for every color treatment.</p><a href="construction.svg" download>Download construction SVG</a></div></div></section>
<section class="explanation"><header><p class="eyebrow">Alternate color placement · same geometry</p><h2>Color at the origin.</h2><p>A short portion of the upper originating curve begins in aqua and continues into the unified white C. This is one alternate treatment, not an additional mark.</p></header><div class="alternate"><img src="mark-origin.svg" width="220" height="220" alt="Alternate treatment: upper origin starts aqua">{sizes(k,'origin')}<img src="identity-origin.svg" width="{LOCK_WIDTH}" height="40" alt="Origin treatment at navbar size"></div></section>
<section class="black-proof paper"><h2>Pure black / independent of color</h2><img src="mark-black.svg" width="200" height="200" alt="Refinement {k} in pure black">{sizes(k,'black')}{navbar('black')}</section>
<details class="downloads"><summary>SVG sources and transparent PNG exports</summary><p>Each SVG has the same merged contour. PNGs are available at 16, 24, 32, 64 and 512px.</p><ul>'''+''.join(f'<li>{name}: <a href="mark-{color}.svg" download>mark SVG</a> · <a href="identity-{color}.svg" download>lockup SVG</a> · <a href="mark-{color}-512.png" download>512px PNG</a></li>' for color,name in [('white','Pure white'),('navy','Pure navy'),('black','Pure black'),('primary','Confluence / dark'),('light','Confluence / light'),('origin','Alternate / origin')])+f'''</ul><p><a href="origin-a.svg" download>Upper source ribbon</a> · <a href="origin-b.svg" download>Lower source ribbon</a></p></details><nav class="bottom-nav"><a href="../">All four</a><a href="../{int(k)%4+1:02}/">Next refinement →</a></nav></main>'''+footer('../')
def gallery(items):
    cards=[]
    for v,d in items:
        k=v['id'];cards.append(f'<article class="candidate"><header><span>{k}</span><span>{v["label"]}</span></header><a class="hero-mark" href="{k}/" aria-label="Inspect refinement {k}"><img src="{k}/mark-white.svg" width="200" height="200" alt="Confluence C {k} in monochrome"></a><div class="color-mark"><img src="{k}/mark-primary.svg" width="140" height="140" alt="Confluence C {k} in two colors"></div><div class="compact-lock"><img src="{k}/identity-primary.svg" width="{LOCK_WIDTH}" height="40" alt="Covan Labs at actual navbar size"></div>{sizes(k,"primary",k+"/")}<a class="inspect" href="{k}/">Opening, geometry &amp; proofs ↗</a></article>')
    return head('Confluence C — four refinements')+'''<main id="main"><header class="page-heading"><p class="eyebrow">Covan Labs / Confluence C</p><h1>One opening. A shared identity.</h1><p>Retained references. Continue to the <a href="../confluence-flow/">three Curved Confluence refinements</a>, based primarily on study 02.</p><p>Four terminal relationships, developed from studies 01 and 04.<br>Monochrome first. Color second. No final mark selected.</p></header><div class="candidate-grid">'''+''.join(cards)+'''</div><section class="overview-note"><h2>Does the opening feel recognizably Covan?</h2><p>The shared idea is a receiving upper curve and a returning lower curve. The four studies test how their tension, curvature and alignment shape one opening. Aqua spans the actual joining point at the back of the C.</p><p>Each refinement includes pure white, navy and black proofs; dark and light two-color versions; a construction grid; separate source ribbons; native size tests; and the alternate origin-color treatment.</p><div class="links"><a href="comparison-primary.png">Two-color comparison</a><a href="comparison-white.png">Monochrome comparison</a><a href="comparison-light.png">Light-background comparison</a></div><p class="caption">Reference studies <a href="../two-origin/01/">01</a> and <a href="../two-origin/04/">04</a> remain available.</p></section></main>'''+footer()
def sheet(items,color):
    light=color in ('navy','light');bg='#F6F8FB' if light else NAVY;fg='#647485' if light else '#9EADBD';line='#DCE4EC' if light else '#27394D'
    s=f'<rect width="1200" height="640" fill="{bg}"/>'
    def text(t,x,y,size=12):return f'<text x="{x}" y="{y}" fill="{fg}" font-family="Inter,Arial,sans-serif" font-size="{size}">{html.escape(t)}</text>'
    s+=text('COVAN LABS / CONFLUENCE C',32,36,14)+text('Four refinements. One construction. No final selection.',32,62)
    for j,(v,d) in enumerate(items):
        x=32+j*288;s+=f'<rect x="{x}" y="90" width="272" height="478" rx="12" fill="none" stroke="{line}"/>'+text(v['id']+' / '+v['label'],x+20,122)
        s+=f'<g transform="translate({x+26} 150) scale(2.2)">{mark(d,color,"m"+v["id"])}</g>'
        s+=f'<g transform="translate({x+(272-LOCK_WIDTH)/2} 390)">{lockup(d,color,"l"+v["id"])}</g>'
        for xx,z in [(28,16),(73,24),(123,32),(179,64)]:
            s+=f'<g transform="translate({x+xx} {496-z/2}) scale({z/100})">{mark(d,color,"s"+v["id"]+str(z))}</g>'+text(str(z)+'px',x+xx,548,10)
    s+=text('SVG geometry · Curved terminal relationships · Inter 600 / 425 · Native 16 / 24 / 32 / 64px proofs',32,610)
    return svg(1200,640,s,'Four Confluence C refinements, native size tests and navbar wordmarks')
def main():
    items=[];records=[]
    for v in G['VARIANTS']:
        d=G['construction'](v);items.append((v,d));folder=OUT/v['id'];folder.mkdir(exist_ok=True)
        for color in COLORS:
            (folder/f'mark-{color}.svg').write_text(svg(100,100,mark(d,color),f'Confluence C {v["id"]} / {color}'))
            (folder/f'identity-{color}.svg').write_text(svg(LOCK_WIDTH,40,lockup(d,color),'Covan Labs'))
        for key,name in [('origin_a','origin-a'),('origin_b','origin-b')]:
            (folder/f'{name}.svg').write_text(svg(100,100,f'<path fill="{SILVER}" d="{d[key]}"/>',name))
        (folder/'construction.svg').write_text(grid(d))
        (folder/'opening.svg').write_text(svg(180,280,mark(d,'white'),'Terminal relationship in the final outline','63 22 30 56'))
        (folder/'index.html').write_text(detail(v,d));records.append({**v,**d})
    (OUT/'index.html').write_text(gallery(items))
    for color in ('white','primary','light'):(OUT/f'comparison-{color}.svg').write_text(sheet(items,color))
    (OUT/'manifest.json').write_text(json.dumps({'status':'four refinements for review; no final selection','concept':'Two origins. One continuous identity.','sources':'Paired SVG arcs and custom cubic terminal curves. No font input to marks.','wordmark':{'family':'Inter','Covan':600,'Labs':425,'font_size':24,'navbar_width':LOCK_WIDTH,'navbar_height':40,'mark_box':36},'variants':records},indent=2)+'\n')
    print('Built four Confluence C refinements with six color proofs each.')
if __name__=='__main__':main()
