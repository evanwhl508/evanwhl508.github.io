#!/usr/bin/env python3
"""Build the unselected 10-concept review. Requires fonttools[woff] for outlined Inter."""
from pathlib import Path
import runpy, importlib.util, json, html
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'logo/exploration'
SHAPES=runpy.run_path(str(ROOT/'scripts/exploration-shapes.py'))['SHAPES']
editorial=runpy.run_path(str(ROOT/'scripts/exploration-content.py'))
CONTENT,METRICS=editorial['CONTENT'],editorial['METRICS']
spec=importlib.util.spec_from_file_location('brand',ROOT/'scripts/build-brand.py')
brand=importlib.util.module_from_spec(spec);spec.loader.exec_module(brand)
PALETTES={'dark':('#F4F7FA','#39C6C8'),'light':('#08111F','#39C6C8'),'white':('#FFFFFF','#FFFFFF'),'navy':('#08111F','#08111F')}
LABELS={'dark':'Primary · dark background','light':'Primary · light background','white':'Monochrome · white','navy':'Monochrome · navy'}
esc=html.escape

def body(s,primary,accent,uid='mark',transform=True):
    paths=''.join(f'<path d="{p}"/>' for _,p in s['parts'])
    contents=f'<defs><pattern id="{uid}" patternUnits="userSpaceOnUse" width="100" height="100"><rect width="100" height="100" fill="{primary}"/><path fill="{accent}" d="{s["accent"]}"/></pattern></defs><g fill="url(#{uid})" fill-rule="evenodd">{paths}</g>'
    return f'<g transform="{s.get("transform", "translate(0 0)") if transform else "translate(0 0)"}">{contents}</g>'

def svg(w,h,content,label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(label)}"><title>{esc(label)}</title>{content}</svg>\n'

def diagram(s):
    cells=[];n=len(s['parts'])+1;w=n*180
    for i,(name,path) in enumerate(s['parts']):
        ghost=''.join(f'<path d="{p}"/>' for _,p in s['parts'])
        cells.append(f'<g transform="translate({i*180+30} 24) scale(1.2)" fill-rule="evenodd"><path d="M50 0V100M0 50H100" stroke="#27394D" stroke-width=".6"/><g fill="#F4F7FA" opacity=".12">{ghost}</g><path fill="#F4F7FA" d="{path}"/></g>')
        cells.append(f'<text x="{i*180+90}" y="176" fill="#9EADBD" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="12">{i+1:02} · {esc(name)}</text>')
    cells.append(f'<g transform="translate({(n-1)*180+30} 24) scale(1.2)">{body(s,"#F4F7FA","#39C6C8","assembled")}</g><text x="{(n-1)*180+90}" y="176" fill="#9EADBD" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="12">Together</text>')
    return svg(w,200,'<rect width="100%" height="100%" fill="#08111F"/>'+''.join(cells),f'Concept {s["id"]}: actual component contours and their assembly')

def head(title,depth=''):
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex, nofollow"><title>{esc(title)} · Covan Labs</title><link rel="icon" href="/logo/covan-mark-dark.svg"><link rel="stylesheet" href="/assets/theme2.css"><link rel="stylesheet" href="{depth}review.css"></head><body><a class="skip-link" href="#main">Skip to content</a>'

def footer():
    return '<footer class="review-footer"><p>Covan Labs · Concept exploration · No concept selected</p><a href="/">Studio website</a></footer></body></html>'

def detail(s,c):
    panels=[]
    for palette in PALETTES:
        samples=''.join(f'<figure><img src="mark-{palette}-{z}.png" width="{z}" height="{z}" alt="Concept {s["id"]}, {palette}, {z}px"><figcaption>{z}px</figcaption></figure>' for z in [16,24,32,64])
        panels.append(f'<section class="proof-panel {"paper" if palette in ("light","navy") else "ink"}"><h2>{LABELS[palette]}</h2><img class="large-mark" src="mark-{palette}.svg" width="256" height="256" alt="Concept {s["id"]}, {LABELS[palette]}"><div class="native-tests">{samples}</div><a href="mark-{palette}.svg" download>SVG</a><span aria-hidden="true"> / </span><a href="mark-{palette}-512.png" download>512px PNG</a></section>')
    rationales=[('First impression',c['impression']),('Why the shape works',c['beauty']),('What to discover',c['hidden']),('Why Covan',c['specific']),('Could it belong to another company?',c['portability']),('What the aqua means',c['aqua']),('Letter-reading limits',c['letters']),('Watch in review',c['watch'])]
    score_rows=''.join(f'<tr><th scope="row">{m}</th><td>{v}<span class="out-of"> / 10</span></td></tr>' for m,v in zip(METRICS,c['scores']))
    previous=f'<a href="../{int(s["id"])-1:02}/">← Previous</a>' if s['id']!='01' else '<span></span>'
    following=f'<a href="../{int(s["id"])+1:02}/">Next →</a>' if s['id']!='10' else '<span></span>'
    return head(f'Concept {s["id"]}', '../')+f'''<main class="review detail" id="main"><nav class="review-nav" aria-label="Concept review"><a href="../">← All ten concepts</a><span>Concept {s['id']} / 10</span></nav><header class="detail-heading"><p class="eyebrow">Covan Labs · Exploration</p><h1>Concept {s['id']}</h1><p>Judge the mark first. The story and assessment stay closed until you choose to read them.</p></header><div class="proof-grid">{''.join(panels)}</div><section class="lockups"><h2>In the name of Covan Labs.</h2><div class="lockup ink"><img src="lockup-dark.svg" width="420" height="100" alt="Concept {s['id']} with Covan Labs wordmark on dark"></div><div class="lockup paper"><img src="lockup-light.svg" width="420" height="100" alt="Concept {s['id']} with Covan Labs wordmark on light"></div></section><details class="full-size"><summary>Inspect the 512px tests</summary><p>These are 512 × 512 transparent PNGs. They display at native size where space allows; open an image for an unscaled view on a smaller screen.</p><div class="full-grid">'''+''.join(f'<a class="full-mark {"paper" if p in ("light","navy") else "ink"}" href="mark-{p}-512.png"><img src="mark-{p}-512.png" width="512" height="512" alt="Concept {s["id"]} at 512px, {LABELS[p]}"></a>' for p in PALETTES)+f'''</div></details><details class="meaning" id="meaning"><summary>Reveal the story, construction and assessment</summary><header class="meaning-heading"><p class="eyebrow">{esc(s['group'])}</p><h2>{esc(s['name'])}</h2><p class="story">{esc(c['story'])}</p></header><section class="construction"><h3>Same contours. Revealed.</h3><p>The highlighted paths are the actual filled components used in this SVG. Faint paths show their relationship; no extra letters have been drawn over the mark.</p><div class="construction-steps">{''.join(f'<figure><img src="component-{i+1}.svg" width="120" height="120" alt="Isolated {esc(name)} against the complete structure"><figcaption>{i+1:02} · {esc(name)}</figcaption></figure>' for i,(name,_) in enumerate(s['parts']))}<figure><img src="mark-dark.svg" width="120" height="120" alt="Assembled concept"><figcaption>Together</figcaption></figure></div><ol>'''+''.join(f'<li>{esc(n)}</li>' for n in s['notes'])+'''</ol></section><div class="rationale-grid">'''+''.join(f'<section><h3>{esc(t)}</h3><p>{esc(p)}</p></section>' for t,p in rationales)+f'''</div><section class="assessment"><h3>Design assessment</h3><p>Subjective 1–10 judgments for discussion, not test results or a ranking. “Ownability” describes perceived visual potential; no trademark or similarity clearance is claimed. There is no total or selected winner.</p><table><caption>Concept {s['id']} · ten review criteria</caption><thead><tr><th scope="col">Criterion</th><th scope="col">Assessment</th></tr></thead><tbody>{score_rows}</tbody></table></section></details><section class="downloads"><h2>Source files</h2><p>Native SVG marks and outlined Inter wordmarks. PNGs retain transparent backgrounds.</p><ul>'''+''.join(f'<li>{LABELS[p]}: <a href="mark-{p}.svg" download>mark SVG</a> · <a href="lockup-{p}.svg" download>lockup SVG</a> · <a href="mark-{p}-512.png" download>512px PNG</a></li>' for p in PALETTES)+f'''</ul><a href="construction.svg" download>Construction diagram SVG</a></section><nav class="previous-next" aria-label="More concepts">{previous}<a href="../">All concepts</a>{following}</nav></main>'''+footer()

def gallery():
    cards=[]
    for s in SHAPES:
        cards.append(f'<a class="concept-card" href="{s["id"]}/" aria-label="Open concept {s["id"]}"><span class="concept-number">{s["id"]}</span><img data-concept="{s["id"]}" src="{s["id"]}/mark-dark.svg" width="160" height="160" alt="Concept {s["id"]}"><span class="inspect">Inspect <span aria-hidden="true">↗</span></span></a>')
    return head('Ten logo concepts')+'''<main class="review" id="main"><header class="gallery-heading"><p><strong>Archived study.</strong> This round was rejected. <a href="/logo/two-origin/">Review the current Two-Origin C family</a>.</p><p class="eyebrow">Covan Labs · Logo exploration</p><h1>Start with the mark.</h1><p>Ten different constructions. No names, stories or scores here.<br>Open any concept when you are ready to look closer.</p></header><fieldset class="palette-switch"><legend>Compare in</legend><label><input type="radio" name="palette" value="dark" checked> Two color · dark</label><label><input type="radio" name="palette" value="white"> White</label><label><input type="radio" name="palette" value="light"> Two color · light</label><label><input type="radio" name="palette" value="navy"> Navy</label></fieldset><div class="concept-grid" data-palette="dark">'''+''.join(cards)+'''</div><section class="review-next"><h2>Like it first. Discover it second.</h2><p>Each study includes dark and light proofs, monochrome, native 16 / 24 / 32 / 64px samples, 512px exports, wordmark lockups and a construction diagram. Stories and assessments remain collapsed on entry.</p><p>No concept has been selected or applied to the studio website. This round replaces the earlier Modular C refinement direction.</p><div class="download-row"><a href="contact-sheet-dark.svg" download>Contact sheet SVG</a><a href="contact-sheet-dark.png" download>Contact sheet PNG</a><a href="covan-logo-exploration.zip" download>Download all concepts</a></div></section></main><script src="review.js"></script>'''+footer()

def contact_sheet(palette):
    main,accent=PALETTES[palette];light=palette in ('light','navy');bg='#F6F8FB' if light else '#08111F';muted='#647485' if light else '#9EADBD';border='#DCE4EC' if light else '#27394D'
    rows=[f'<rect width="1280" height="800" fill="{bg}"/>']
    text,_=brand.text_paths('Covan Labs / 10 concepts',22,40,53,main);rows.append(text)
    for index,s in enumerate(SHAPES):
        x=40+(index%5)*244;y=86+(index//5)*326
        rows.append(f'<rect x="{x}" y="{y}" width="224" height="302" rx="12" fill="none" stroke="{border}"/>')
        t,_=brand.text_paths(s['id'],13,x+18,y+30,muted);rows.append(t)
        rows.append(f'<g transform="translate({x+32} {y+65}) scale(1.6)">{body(s,main,accent,"sheet"+s["id"])}</g>')
        for offset,size in [(22,16),(63,24),(114,32),(160,40)]:
            rows.append(f'<g transform="translate({x+offset} {y+246-size/2}) scale({size/100})">{body(s,main,accent,"small"+s["id"]+str(size))}</g>')
    t,_=brand.text_paths('Exploration only. No concept selected.',13,40,775,muted);rows.append(t)
    return svg(1280,800,''.join(rows),'Covan Labs: ten unselected logo concepts, shown without stories')

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    manifest={'status':'unselected exploration','supersedes':'Modular C A/B/C refinements','sizes':[16,24,32,64,512],'palette':PALETTES,'assessment':'subjective design judgment; not trademark clearance','concepts':[]}
    for s,c in zip(SHAPES,CONTENT):
        directory=OUT/s['id'];directory.mkdir(exist_ok=True)
        for palette,(primary,accent) in PALETTES.items():
            (directory/f'mark-{palette}.svg').write_text(svg(100,100,body(s,primary,accent),f'Concept {s["id"]}'))
            first,cursor=brand.text_paths('Covan ',39,112,64,primary,.2)
            second,_=brand.text_paths('Labs',39,cursor,64,primary if palette in ('white','navy') else ('#647485' if palette=='light' else '#9EADBD'),.2)
            (directory/f'lockup-{palette}.svg').write_text(svg(350,100,'<g transform="translate(0 7) scale(.86)">'+body(s,primary,accent)+'</g>'+first+second,'Covan Labs'))
        ghost=''.join(f'<path d="{p}"/>' for _,p in s['parts'])
        for i,(name,path) in enumerate(s['parts']):
            (directory/f'component-{i+1}.svg').write_text(svg(100,100,f'<g fill-rule="evenodd"><g fill="#F4F7FA" opacity=".12">{ghost}</g><path fill="#F4F7FA" d="{path}"/></g>',name))
        (directory/'construction.svg').write_text(diagram(s))
        (directory/'index.html').write_text(detail(s,c))
        manifest['concepts'].append({**s,**c,'scores':dict(zip(METRICS,c['scores']))})
    (OUT/'index.html').write_text(gallery())
    (OUT/'manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
    for palette in PALETTES:
        (OUT/f'contact-sheet-{palette}.svg').write_text(contact_sheet(palette))
    print('Built 10 independent studies, 40 mark SVGs, 40 outlined lockups, 10 diagrams and 4 contact sheets. No winner selected.')
if __name__=='__main__': main()
