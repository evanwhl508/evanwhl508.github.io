#!/usr/bin/env python3
"""Build five variations of ONE font-independent Two-Origin C. Standard library only."""
from pathlib import Path
import runpy,json,math,xml.etree.ElementTree as ET,html
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'logo/two-origin';OUT.mkdir(exist_ok=True)
G=runpy.run_path(str(ROOT/'scripts/two-origin-geometry.py'));VARIANTS=G['VARIANTS'];construction=G['construction'];xy=G['xy']
COLORS={'white':'#FFFFFF','navy':'#08111F'}
# Supporting lettering only. Geometry of the mark is supplied exclusively by G above.
WORD_SOURCE=ET.parse(ROOT/'logo/identity/b1/wordmark-white.svg').getroot()
WW,WH=map(float,WORD_SOURCE.get('viewBox').split()[2:])
WORD_PATHS=[p.attrib.copy() for p in WORD_SOURCE.findall('.//{http://www.w3.org/2000/svg}path')]
LOCK_WIDTH=48+WW*.2;LOCK_HEIGHT=40

def svg(w,h,content,label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{html.escape(label)}"><title>{html.escape(label)}</title>{content}</svg>\n'
def wordmark(color):
    # Existing wordmark paths use x=8 and y=10 on their parent, retained here.
    return f'<g fill="{color}" transform="translate(8 10)">'+''.join(f'<path d="{p["d"]}"/>' for p in WORD_PATHS)+'</g>'
def mark(d,color):return f'<path fill="{color}" d="{d["merged"]}"/>'
def lockup(d,color):
    return f'<g transform="translate(0 2) scale(.36)">{mark(d,color)}</g><g transform="translate(48 8) scale(.2)">{wordmark(color)}</g>'
def grid(v,d):
    # True construction circles, centres, axes, terminal normals and joining points.
    lines=''.join(f'<path d="M{x} 0V100M0 {x}H100"/>' for x in range(0,101,10))
    content=f'<rect width="100" height="100" fill="#08111F"/><g stroke="#27394D" stroke-width=".25" fill="none">{lines}</g><path fill="#FFFFFF" opacity=".08" d="{d["merged"]}"/>'
    for index,c in enumerate(d['circles']):
        dash=' stroke-dasharray="1.1 1.4"' if index%2 else ''
        content+=f'<circle cx="{c["cx"]}" cy="{c["cy"]}" r="{c["r"]}" fill="none" stroke="#9EADBD" stroke-width=".35"{dash}/><path d="M{c["cx"]-1} {c["cy"]}h2m-1 -1v2" stroke="#FFFFFF" stroke-width=".35"/>'
    content+=f'<path d="M{v["left"]} 0V100M{v["spine"]} 0V100M0 {v["y"]}H100" stroke="#9EADBD" stroke-width=".25" stroke-dasharray="2 2"/>'
    for points in (d['upper_terminal'],d['lower_terminal']):
        content+=f'<path d="M{xy(points[0])}L{xy(points[1])}" stroke="#FFFFFF" stroke-width=".8"/>'
    content+=f'<path fill="none" stroke="#FFFFFF" stroke-width=".6" d="{d["merged"]}"/>'
    for x,y in (d['outer_join'],d['inner_join']):content+=f'<circle cx="{x}" cy="{y}" r="1" fill="#FFFFFF"/>'
    return svg(100,100,content,'Actual circular construction: paired ribbons, shared outer tangent, offset inner arcs and normal terminal cuts')
def head(title,depth=''):
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{html.escape(title)} · Covan Labs</title><link rel="icon" href="{depth}01/mark-white.svg"><link rel="stylesheet" href="{depth}review.css"></head><body><a class="skip" href="#main">Skip to content</a>'
def footer(depth=''):
    return f'<footer><p>Monochrome geometry studies. No variant selected.</p><a href="{depth}covan-two-origin-c.zip" download>Download SVG / PNG studies</a><a href="/">Studio website</a></footer></body></html>'
def size_row(key,color,prefix=''):
    return '<div class="sizes">'+''.join(f'<figure><img src="{prefix}mark-{color}-{z}.png" width="{z}" height="{z}" alt="Variant {key}, {z}px"><figcaption>{z}px</figcaption></figure>' for z in (16,24,32,64))+'</div>'
def detail(v,d):
    k=v['id'];proofs=[]
    for color in COLORS:
        proofs.append(f'<section class="proof {"paper" if color=="navy" else "ink"}"><h2>{"Navy on light" if color=="navy" else "White on dark"}</h2><img class="large" src="mark-{color}.svg" width="240" height="240" alt="Two-Origin C variant {k}, merged silhouette">{size_row(k,color)}<div class="navbar"><img src="identity-{color}.svg" width="{LOCK_WIDTH}" height="40" alt="Variant {k} beside Covan Labs at navbar size"></div><p class="caption">36px mark box · 20px wordmark cap height</p></section>')
    figures=''.join(f'<figure><img src="{file}.svg" width="160" height="160" alt="{alt}"><figcaption>{label}</figcaption></figure>' for file,label,alt in [('origin-a-white','Origin 1','Upper curved ribbon shown independently'),('origin-b-white','Origin 2','Lower curved ribbon shown independently'),('mark-white','One C','Both ribbons merged; shared boundary removed')])
    values=[('Upper / lower outer radius',f'{v["upper"]} / {v["lower"]}'),('Upper / lower inner radius',f'{v["inner_upper"]} / {v["inner_lower"]}'),('Inner-centre offset',f'+{v["offset_upper"]} / −{v["offset_lower"]}'),('Opening angles',f'{v["opening_upper"]}° / {v["opening_lower"]}°'),('Shared spine',f'x = {v["left"]} to {v["spine"]}; y = {v["y"]}')]
    rows=''.join(f'<tr><th scope="row">{label}</th><td>{value}</td></tr>' for label,value in values)
    page=head(f'Two-Origin C / {k}', '../')+f'''<main id="main"><nav class="top-nav"><a href="../">← Compare all five</a><span>Two-Origin C / {k}</span></nav><header class="detail-heading"><p class="eyebrow">Variant {k}</p><h1>{v['label']}</h1><p>One construction. A change in curvature, opening and balance.</p></header><div class="proof-grid">{''.join(proofs)}</div><section class="construction"><header><p class="eyebrow">Construction</p><h2>Two curves. One continuous silhouette.</h2><p>Each origin is a curved ribbon drawn from circular arcs. The outside edges share a tangent at the back of the C. The offset inner arcs meet at one shallow cusp, giving the counter its shape. Their shared boundary is removed from the final outline.</p></header><div class="parts">{figures}</div><div class="grid-layout"><figure class="grid-figure"><img src="construction.svg" width="400" height="400" alt="True construction grid with four circles, their centres, the shared tangent and terminal cuts"><figcaption>Solid circles: outside curves. Dotted circles: inner curves.<br>Dots: shared outer tangent and inner meeting point. Grid: 10 units.</figcaption></figure><div><h3>One rule, varied.</h3><p>The terminal cuts follow the normal of their corresponding inner circle. The upper and lower radii set the balance; moving the inner centres sets the counter tension.</p><table><caption>Geometry in a 100 × 100 design space</caption><tbody>{rows}</tbody></table><p class="note">The mark uses only SVG arcs and straight closing cuts. No font outlines are used to construct it.</p></div></div><p class="origin-story">Two origins forming one C — a reference to Cobie + Evan becoming Covan.</p></section><details class="downloads"><summary>Files and 512px proofs</summary><div class="large-proofs">'''+''.join(f'<a class="{"paper" if color=="navy" else "ink"}" href="mark-{color}-512.png"><img src="mark-{color}-512.png" width="512" height="512" alt="Variant {k}, {color}, 512px"></a>' for color in COLORS)+f'''</div><ul>'''+''.join(f'<li>{color.capitalize()}: <a href="mark-{color}.svg" download>merged mark SVG</a> · <a href="identity-{color}.svg" download>identity SVG</a> · <a href="origin-a-{color}.svg" download>origin 1 SVG</a> · <a href="origin-b-{color}.svg" download>origin 2 SVG</a></li>' for color in COLORS)+'''<li><a href="construction.svg" download>Construction grid SVG</a></li></ul></details><nav class="bottom-nav"><a href="../">All five variants</a>'''+(f'<a href="../{int(k)+1:02}/">Next variant →</a>' if k!='05' else '<a href="../01/">Back to 01 →</a>')+'</nav></main>'+footer('../')
    return page

def gallery(items):
    cards=[]
    for v,d in items:
        k=v['id'];cards.append(f'<article class="candidate"><header><span>{k}</span><span>{v["label"]}</span></header><a class="hero-mark" href="{k}/" aria-label="Inspect variant {k}"><img src="{k}/mark-white.svg" width="160" height="160" alt="Two-Origin C variant {k}"></a><div class="mini-identity"><img src="{k}/identity-white.svg" width="{LOCK_WIDTH}" height="40" alt="Variant {k} beside Covan Labs at navbar size"></div>{size_row(k,"white",k+"/")}<a class="inspect" href="{k}/">Construction &amp; proofs <span aria-hidden="true">↗</span></a></article>')
    return head('Two-Origin C — Five variations')+'''<main id="main"><header class="page-heading"><p class="eyebrow">Covan Labs / Monochrome studies</p><h1>One C. Two origins.</h1><p><strong>Retained references:</strong> studies 01 and 04 inform the <a href="../confluence/">current Confluence C refinements</a>.</p><p>Five variations of the same paired-arc construction.<br>Judge the silhouette and navbar lockup first; inspect the geometry underneath each.</p></header><div class="candidate-grid">'''+''.join(cards)+'''</div><section class="overview-note"><h2>The shared construction</h2><p>Two curved ribbons meet at a common outer tangent. Their offset inner arcs create a single cusp in the counter. The final C is one uninterrupted silhouette, with the joining edge removed.</p><p>The five studies vary curvature, opening, counter depth and asymmetry. The wordmark stays the same throughout.</p><div class="links"><a href="comparison-white.png">View dark comparison sheet</a><a href="comparison-navy.png">View light comparison sheet</a></div></section></main>'''+footer()

def sheet(items,color):
    light=color=='navy';fg=COLORS[color];bg='#F6F8FB' if light else '#08111F';secondary='#647485' if light else '#9EADBD';border='#DCE4EC' if light else '#27394D'
    parts=[f'<rect width="1400" height="640" fill="{bg}"/>']
    def text(s,x,y,z=12):return f'<text x="{x}" y="{y}" fill="{secondary}" font-family="Inter,Arial,sans-serif" font-size="{z}">{s}</text>'
    parts.append(text('COVAN LABS / TWO-ORIGIN C',40,42,14));parts.append(text('One construction. Five monochrome variations.',40,68,13))
    for i,(v,d) in enumerate(items):
        x=40+i*268;y=100;parts.append(f'<rect x="{x}" y="{y}" width="248" height="470" rx="12" fill="none" stroke="{border}"/>');parts.append(text(v['id'],x+20,y+30));parts.append(text(v['label'],x+20,y+54))
        parts.append(f'<g transform="translate({x+34} {y+90}) scale(1.8)">{mark(d,fg)}</g>')
        parts.append(f'<g transform="translate({x+24} {y+294})">{lockup(d,fg)}</g>')
        for xx,z in [(25,16),(65,24),(110,32),(166,64)]:
            parts.append(f'<g transform="translate({x+xx} {y+390-z/2}) scale({z/100})">{mark(d,fg)}</g>');parts.append(text(str(z)+'px',x+xx,y+444,10))
    parts.append(text('All marks are drawn from SVG geometry. Supporting type is unchanged. No variant approved; color deferred.',40,614,12))
    return svg(1400,640,''.join(parts),'Five monochrome Two-Origin C variants with navbar lockups and size tests')

def main():
    items=[];records=[]
    for v in VARIANTS:
        d=construction(v);items.append((v,d));folder=OUT/v['id'];folder.mkdir(exist_ok=True)
        for color,fill in COLORS.items():
            (folder/f'mark-{color}.svg').write_text(svg(100,100,mark(d,fill),f'Two-Origin C {v["id"]}'))
            (folder/f'identity-{color}.svg').write_text(svg(LOCK_WIDTH,40,lockup(d,fill),'Covan Labs'))
            for key,name in [('origin_a','origin-a'),('origin_b','origin-b')]:
                (folder/f'{name}-{color}.svg').write_text(svg(100,100,f'<path fill="{fill}" d="{d[key]}"/>',f'Two-Origin C {v["id"]}, {name}'))
        (folder/'construction.svg').write_text(grid(v,d));(folder/'index.html').write_text(detail(v,d));records.append({**v,**d})
    (OUT/'index.html').write_text(gallery(items))
    (OUT/'manifest.json').write_text(json.dumps({'status':'unapproved monochrome studies','concept':'Two origins forming one C','mark_source':'SVG circular geometry; no font outlines','construction':'Two eccentric circular ribbons, shared outer tangent, single inner cusp; merged without a seam','navbar_width':LOCK_WIDTH,'navbar_height':40,'variants':records},indent=2)+'\n')
    for color in COLORS:(OUT/f'comparison-{color}.svg').write_text(sheet(items,color))
    print('Built five variations of one Two-Origin C, with actual construction grids and independent ribbon sources.')
if __name__=='__main__':main()
