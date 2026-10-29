#!/usr/bin/env python3
"""Exploratory Direction 01 refinements. Never writes the active website identity."""
from pathlib import Path
import math
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'logo/refinements'
R, r, CX, CY = 26, 15, 32, 32
PALETTES = {
    'dark': ('#F4F7FA', '#39C6C8'),
    'light': ('#08111F', '#15999C'),
    'white': ('#FFFFFF', '#FFFFFF'),
    'navy': ('#08111F', '#08111F'),
}


def point(radius, angle):
    a = math.radians(angle)
    return (CX + radius * math.cos(a), CY + radius * math.sin(a))


def xy(p):
    return f'{p[0]:.5f} {p[1]:.5f}'


def angle(p):
    return math.degrees(math.atan2(p[1]-CY, p[0]-CX)) % 360


def arc(radius, start, end, clockwise=True):
    sweep = (end-start) % 360 if clockwise else (start-end) % 360
    command = f'A{radius} {radius} 0 {int(sweep>180)} {int(clockwise)} {xy(point(radius,end))}'
    steps = max(2, math.ceil(sweep*8))
    direction = 1 if clockwise else -1
    pts = [point(radius,start+direction*sweep*i/steps) for i in range(steps+1)]
    return command, pts


def area(points):
    return abs(sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(points,points[1:]+points[:1]))/2)


def segment(start,end):
    outer, op = arc(R,start,end)
    inner, ip = arc(r,end,start,False)
    return f'M{xy(op[0])} {outer} L{xy(ip[0])} {inner} Z', area(op+ip)


def horizontal(radius,y):
    return (CX-math.sqrt(radius**2-(y-CY)**2),y)


def diagonal(radius, intercept):
    # Left intersections with y = x + intercept; the cut is exactly 45 degrees.
    u=(-intercept-math.sqrt(2*radius**2-intercept**2))/2
    return (CX+u,CY+u+intercept)


def upper(outer_cut,inner_cut,seam=()):
    outer,op=arc(R,angle(outer_cut),315)
    inner,ip=arc(r,315,angle(inner_cut),False)
    return f'M{xy(outer_cut)} {outer} L{xy(ip[0])} {inner} '+''.join(f'L{xy(p)} ' for p in seam)+'Z', area(op+ip+list(seam))


def lower(start,outer_cut,inner_cut,seam=()):
    outer,op=arc(R,start,angle(outer_cut))
    inner,ip=arc(r,angle(inner_cut),start,False)
    return f'M{xy(op[0])} {outer} '+''.join(f'L{xy(p)} ' for p in seam)+f'L{xy(inner_cut)} {inner} Z', area(op+list(seam)+ip)


def shapes(name):
    if name in ['a','b']:
        # Shared circular contours; the terminal follows exactly the lower module's annulus.
        top_seam=[(14,30.5),(11.5,33),(9,30.5)] if name=='b' else []
        bottom_seam=[(9,33.5),(11.5,36),(14,33.5)] if name=='b' else []
        return [upper(horizontal(R,30.5),horizontal(r,30.5),top_seam),
                lower(80,horizontal(R,33.5),horizontal(r,33.5),bottom_seam),
                segment(45,74)]
    # A single uninterrupted circular path, divided by a slim diagonal seam and terminal gap.
    return [upper(diagonal(R,16.15),diagonal(r,16.15)),
            lower(77,diagonal(R,17.85),diagonal(r,17.85)),
            segment(45,74.5)]


VARIANTS = {
    'a': ('Soft Modular C', 'A circular C in three pieces. The lower white arc and aqua end share one continuous construction; 45° open ends retain a technical edge.'),
    'b': ('Modular C with Hidden V', 'Derived from A. Two shallow, opposing 45° cuts form a quiet V in the seam’s negative space. No separate V or colored glyph.'),
    'c': ('Continuous-flow Modular C', 'One circular path, divided by a narrow 45° seam and a smaller terminal gap. The modules feel connected; aqua only marks the endpoint.'),
}


def svg(paths,primary,accent,label):
    content=''.join(f'<path fill="{accent if i==2 else primary}" d="{path}"/>' for i,(path,_) in enumerate(paths))
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64" role="img" aria-label="{label}">\n{content}\n</svg>\n'


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    manifest={'status':'archived — superseded by full concept exploration','base':'Direction 01 — Modular C','center':[CX,CY], 'outer_radius':R,'inner_radius':r,'variants':{}}
    for key,(title,description) in VARIANTS.items():
        paths=shapes(key)
        total=sum(a for _,a in paths)
        aqua=100*paths[2][1]/total
        # Measure the prior base; never increase its aqua proportion.
        prior=100*144/(area([(20,8),(56,8),(56,20),(25,20),(18,27),(6,27),(6,22)])+area([(6,32),(18,32),(18,37),(25,44),(40,44),(40,56),(20,56),(6,42)])+144)
        assert 10 <= aqua <= min(15,prior), (key,aqua,prior)
        manifest['variants'][key]={'title':title,'description':description,'filled_area':round(total,3),'aqua_area_percent':round(aqua,3),'prior_base_aqua_percent':round(prior,3),'paths':3}
        for palette,(primary,accent) in PALETTES.items():
            (OUT/f'{key}-{palette}.svg').write_text(svg(paths,primary,accent,f'Variant {key.upper()}: {title}'))
    (OUT/'geometry.json').write_text(json.dumps(manifest,indent=2)+'\n')
    (OUT/'index.html').write_text(review_page(manifest))
    print(json.dumps({key:value['aqua_area_percent'] for key,value in manifest['variants'].items()}))


def review_page(manifest):
    cards=[]
    for key,(title,description) in VARIANTS.items():
        ratio=manifest['variants'][key]['aqua_area_percent']
        samples=''
        for style,label in [('dark','Two color · dark'),('white','One color · white'),('light','Two color · light'),('navy','One color · navy')]:
            imgs=''.join(f'<figure><img src="{key}-{style}-{size}.png" width="{size}" height="{size}" alt="Variant {key.upper()} at {size} pixels, {label}"><figcaption>{size}px</figcaption></figure>' for size in [16,24,32,64])
            samples+=f'<div class="test-label">{label}</div><div class="size-row {"light-surface" if style in ["light","navy"] else "dark-surface"}">{imgs}</div>'
        downloads=' · '.join(f'<a href="{key}-{style}.svg" download>{style.capitalize()} SVG</a>' for style in PALETTES)
        cards.append(f'''<article class="variant" id="{key}"><div class="variant-meta"><span>Variant {key.upper()}</span><span>{ratio:.2f}% aqua</span></div><div class="primary-mark"><img src="{key}-dark.svg" width="192" height="192" alt="{title} — three connected circular segments forming an open C"></div><h2>{title}</h2><p class="description">{description}</p>{samples}<div class="downloads">{downloads}</div><details><summary>View 512px tests</summary><p class="test-note">Each PNG is 512 × 512px. Previews fit this panel; open an image to inspect its native size.</p>'''+''.join(f'<a class="large-test {"light-surface" if style in ["light","navy"] else "dark-surface"}" href="{key}-{style}-512.png"><img src="{key}-{style}-512.png" width="512" height="512" alt="{title}, {style}, 512px"></a>' for style in PALETTES)+'''</details></article>''')
    return '''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex"><title>Modular C — Refinements A / B / C · Covan Labs</title><link rel="icon" href="/logo/covan-mark-dark.svg"><link rel="stylesheet" href="/assets/theme2.css"><link rel="stylesheet" href="review.css"></head>
<body><main class="page review"><header class="review-heading"><p class="eyebrow">Covan Labs / Direction 01</p><h1>Modular C, refined.</h1><p class="lead">Three explorations of a softer, more continuous C.</p><p class="status">Archived exploration. Modular C is no longer the selected direction. <a href="/logo/two-origin/">Review the current Two-Origin C family</a>.</p></header><div class="review-grid">'''+''.join(cards)+'''</div><section class="review-notes"><h2>Reading the studies</h2><p>A preserves the clearest modular breaks. B adds a shallow negative-space detail that should disappear before the C does. C prioritizes continuity, with finer seams that visually merge at the smallest sizes.</p><p>All three use concentric circular contours, an open right-hand counter, three filled paths and an aqua terminal below the original mark’s aqua proportion. There is no inward bar that turns the silhouette into a G.</p><p>Direction 02’s literal aqua V and Direction 03 are discarded. No refined variant has been promoted to the website identity.</p><div class="base-reference"><img src="/logo/concepts/01-modular-c.svg" width="48" height="48" alt="Original Modular C base, not final geometry"><span>Original Direction 01 · construction reference only</span></div><p><a href="geometry.json">Geometry and filled-area measurements</a></p></section></main></body></html>
'''


if __name__=='__main__':
    main()
