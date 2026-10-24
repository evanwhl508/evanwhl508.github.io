# Covan Labs — full concept exploration

Status: **archived following owner rejection**. The current brief is [two restrained identity directions](logo-identity.md), reviewed at `/logo/identity/`. The remainder records the superseded round. This is the current owner brief, superseding the selected Modular C base and the A/B/C refinement round. The studio's existing production logo remains provisional and unchanged. Earlier studies are archived, not alternative primary paths.

## Source priority and brand context

The latest owner brief resets the logo exploration only. The rest of [the canonical visual system](design-system.md), including navy/silver/aqua, restrained typography and path-based website themes, remains in force. No website port is prescribed.

Covan comes from **Cobie + Evan**. The central idea is **two origins becoming one identity**; “Two names. One lab. Many products.” is inspiration, not literal artwork. The name is not a request for a readable CE monogram. 高凡 is a secondary source of meaning: elevating ordinary ideas into useful products.

The studio builds apps, developer tools, SaaS, AI products, utilities and experiments. Its identity should be calm, technical, precise, premium, independent, trustworthy and product-focused. It must not resemble an agency, generic AI startup, crypto company, gaming studio, hacker/security brand or neon futuristic company.

## Creative priorities

Beauty first, meaning second. A strong concept should achieve at least three of first-sight beauty, discoverable meaning, name-specific meaning, distinctiveness, scalability and a concise explanation. It must work without its story. Favor balanced proportions, deliberate negative space, controlled curves, a memorable silhouette and a durable identity over five forced hidden letters.

“Metal + Water” is a secondary visual principle: precise circles, ellipses and structure combined with flow, openness, continuity and connected curves. It is not literal mystical symbolism. Avoid dominant triangles, spikes, heavy blocks and bulky closed forms; brand quality comes first.

## Ten genuinely different concepts

| IDs | Direction | Creative question |
| --- | --- | --- |
| 01–03 | Two-origin convergence | Can two independent starting forms become one coherent symbol? |
| 04–05 | Hidden C + E | Can the two initials share material or counterspace without spelling CE? |
| 06–07 | Hidden COVAN | Can shared geometry suggest the name without superimposing five glyphs? |
| 08 | 高凡 / elevating the ordinary | Can refinement be expressed through shaping rather than an upward arrow? |
| 09 | Many products, one system | Can independent elements retain a voice inside a coherent family? |
| 10 | Iteration / Covan loop | Can learning return into the product instead of circling outside it? |

The partial COVAN studies explicitly identify omitted letters. No diagrams invent strokes just to claim a complete alphabet. Scores do not select or rank a winner.

## Geometry and exclusions

Prefer circles, ellipses, smooth arcs, shared geometry, strong counters and occasional precise cuts. Avoid excessive chamfers, thin details, gratuitous seams and octagonal/blocky construction. Test 16, 24, 32, 64 and 512px in color and monochrome.

Do not create standalone generic C marks; literal C+V or readable CE overlays; random aqua blocks; stacked bars, menus or alignment controls; hexagons, cubes, code brackets, lab flasks, atoms, AI brains, robots, lightning, arrows, rockets, shields or mountains. Avoid chains, puzzle pieces, yin-yang, handshakes, infinity, generic partnership icons, orbit/loading/cycle/recycling marks, neon branding, purple gradients, 3D logos, metallic wall signage and fake presentation renders. Design for long-term use rather than current startup fashion.

## Color and wordmark

- Background: `#08111F`.
- Main silver: `#F4F7FA`; secondary silver: `#9EADBD`.
- Meaningful aqua: `#39C6C8`, targeted at **10–20% of filled area**. This latest range supersedes the previous refinement-only cap of approximately 11.7%.
- Required versions: primary two-color for dark and light backgrounds, pure white, pure dark/navy monochrome. The same silhouette must work with no aqua.
- The exploration uses the exact supplied aqua on both backgrounds. It is part of the mark, not small light-background text. Review controls on light surfaces use the darker accessible text-link token.
- Primary lockup: symbol + `Covan Labs`, with outlined Inter SemiBold. No 高凡 in the primary lockup; the Chinese name remains available for localized contexts.

## Presentation and review

Start at `/logo/exploration/`. Its neutral numbered gallery reveals no concept names, rationale or scores. Switching the preview palette changes presentation only; it never persists a brand choice or modifies the website. `/logo/concepts/` points to this current review.

Each concept page contains:

1. Large dark/light two-color proofs and large white/navy monochrome proofs.
2. Native 16/24/32/64px transparent PNG tests in all four colorways.
3. All four 512px transparent tests, viewable and downloadable at native size.
4. Dark/light horizontal wordmark lockups; four SVG lockups available for download.
5. A closed disclosure containing the name, one-sentence story, actual-contour construction diagram and rationale.
6. First impression, beauty, hidden meaning, Covan-specific meaning, transferability, aqua meaning, letter-reading limits and review weakness.
7. Ten 1–10 assessments: beauty, distinctiveness, brand-specific meaning, discoverability, timelessness, small-size readability, monochrome, memorability, balance and ownability.

Assessments are subjective design judgments, not measured aesthetic facts or trademark clearance. Abstract shapes can be reassigned to other companies; the review is explicit about where the brand connection is structural, narrative or weaker. No total score, recommended winner or automatic selection is included. Human choice should prioritize beauty, memorability, meaning and long-term fit.

## Reproduction

- `scripts/exploration-shapes.py`: editable SVG contours, integrated accent regions and construction notes.
- `scripts/exploration-content.py`: rationale and unranked scores.
- `scripts/build-logo-exploration.py`: mark SVGs, outlined wordmarks, construction diagrams, pages, manifest and contact sheets. Requires `fonttools[woff]` for the self-hosted Inter outlines.
- `scripts/export-logo-exploration.js`: Playwright CLI `run-code` program. Uses an isolated browser context at device scale 1 and renders 200 transparent PNGs, plus four contact sheets. It leaves the original tab at the gallery.
- `scripts/check-logo-exploration.py`: validates dimensions, transparency, palette, SVG/source counts, monochrome silhouette consistency and the measured accent proportions. Requires Pillow.
- `logo/exploration/manifest.json`: full geometry and editorial record.
- `logo/exploration/measurements.json`: raster area and export checks.
- `logo/exploration/covan-logo-exploration.zip`: standalone SVG/PNG assets, contact sheets, rationale and measurements.

The filled-area estimate uses alpha-weighted 512px pixels. Accent membership is estimated from the interpolation between the supplied silver and aqua. It is a raster measurement with edge antialiasing, not an analytic curve-area claim.

## Scope boundary

This round does not select a logo, replace the current website identity, change theme 1 or theme 2, deploy the site, or alter DNS, email or verification settings. The archived A/B/C review has a clear superseded notice. Existing production assets remain byte-identical to the pre-exploration snapshot.

## Validation record

- 10 concepts; 40 mark SVGs, 40 outlined horizontal lockups, 10 composite construction diagrams and isolated-contour SVGs.
- 200 transparent PNGs: all five requested sizes in all four colorways. Dimensions, transparency, unclipped bounds and monochrome output checked.
- Color and monochrome alpha silhouettes agree within the recorded antialiasing tolerance. Aqua estimates range from 10.50% to 18.66%; per-concept values are in `measurements.json`.
- Browser review at 320, 390, 768 and 1440 CSS pixels: 40 concept-page layouts, 16 gallery palette states, native sample widths, keyboard disclosures and reduced motion checked. No broken images, page overflow or page-script errors were detected.
- Static site validation: 47 HTML pages and 1,271 local links/assets passed. Theme 1 snapshot and CSS remained preserved.
- SHA-256 comparison: all 28 existing production logo/social assets and the homepage in the pre-exploration snapshot remained unchanged.

These checks establish rendering and presentation behavior. They do not turn the subjective beauty, meaning or ownability scores into test results.
