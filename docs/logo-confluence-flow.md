# Covan Labs — Curved Confluence C

Status: **A / Balanced selected as the base direction**. This round is retained at `/logo/confluence-flow/`. Continue to [A1–A3 optical finishing](logo-confluence-finish.md) at `/logo/confluence-finish/`. The owner’s latest brief uses Confluence study 02 as the primary proportion reference, with a restrained influence from study 04’s opening. Earlier studies remain references.

## Current brief

Produce exactly three refinements of the same Two-Origin / Confluence C concept:

- **A — Balanced:** closest to study 02, with the new flowing confluence and optical corrections.
- **B — Flowing:** a slightly more generous lower return and expressive terminal relationship, influenced by study 04 but restrained.
- **C — Minimal:** the same geometry with the upper reverse bend removed, simplifying the terminal for 16–24px use.

The mark must remain immediately readable as C. Its character should come from proportion, flow, the negative-space opening and the confluence. Do not introduce another concept family or a set of opening-angle variations. No hidden letters, added symbols, heart, arrow, V, mouth, puzzle-piece, yin-yang or broken-ring imagery.

### Curved confluence

Replace the earlier pie-slice treatment. The upper and lower source curves should merge tangentially and share a short curved transition. Aqua occupies **6–10% of filled area**, bounded by curved seams, with no gradient or detached module. This owner-directed target supersedes the earlier 12–18% range.

White/silver is the stable engineering structure. Aqua marks the moment when two origins converge into one identity: Cobie + Evan → Covan.

### Optical shape and opening

Use optically drawn contours, not subtraction of concentric circles. Approximately 5–8% local corrections are appropriate: strengthen the spine, lighten the upper terminal, fill the lower sweep and refine the curvature through the opening. Keep the construction modern and geometric, not calligraphic.

The upper reach is restrained and the lower return more generous. Non-parallel terminal directions create an open inward/outward passage. The negative space is the intended signature; no extra symbol is used to explain it.

### Wordmark

Keep Inter at Covan 600 / Labs 425. The 36px mark box and 24px supporting type remain at actual navbar size. The wordmark origin moves from x=44 to x=50, adding 6px of breathing room; the two words stay grouped on one baseline.

## Implemented construction

The mark is drawn with cubic Bézier contours in a 100 × 100 design space. Typography is not an input. There are no circular-arc commands in the new outline.

Both originating ribbons follow the same outer and inner contours through the spine. Their tangents align vertically at x=10 and the optically adjusted inner spine. De Casteljau subdivision defines the start and end of the overlap without changing those contours. Two S-curved cross-seams close the independent ribbons. Their union is the final silhouette; their intersection is the aqua region. The seams do not appear in monochrome.

The color treatment uses that exact intersection in a pattern fill on a single merged contour. It does not paint an independently sized wedge or change the outer silhouette.

Measured local thicknesses are axis-based optical stations, not a claim of constant stroke width everywhere:

| Station | Study 02 | A Balanced | B Flowing | C Minimal |
| --- | ---: | ---: | ---: | ---: |
| Spine | 20 | 21.2 (+6.0%) | 21.4 (+7.0%) | 21.0 (+5.0%) |
| Crown | 21 | 19.8 (−5.7%) | 19.6 (−6.7%) | 19.9 (−5.2%) |
| Lower sweep | 18 | 19.2 (+6.7%) | 19.4 (+7.8%) | 19.1 (+6.1%) |

Each review page presents large monochrome and two-color marks, white/navy/black proofs, dark/light backgrounds, actual-size 16/24/32/64px PNGs, navbar lockups, separate originating curves, the merged result, construction controls, opening detail and confluence detail. The proofs use the same geometry at every size; Minimal is a selectable refinement, not an automatic replacement for other candidates at small sizes.

## Reproduction and validation

- `scripts/confluence-flow-geometry.py`: font-independent source contours, subdivisions, ribbons and overlap.
- `scripts/build-confluence-flow.py`: standard-library builder. Reuses the existing outlined Inter wordmark from Confluence study 02, moving it 6px farther from the mark. No new font dependency is needed.
- `scripts/export-confluence-flow.js`: Playwright CLI renderer, device scale factor 1, producing 75 transparent PNGs plus independent source/overlap QA renders and comparison sheets.
- `scripts/check-confluence-flow.py`: validates shared tangents, identical colorway contours, source union/intersection, native continuity and open counter, dimensions, monochrome fills and measured aqua coverage. It packages the proofs.

Run the builder, use the export script through Playwright CLI `run-code` from the local preview, then run the checker with Pillow installed. Exact geometry is recorded in `manifest.json`; measured results are in `checks.json`. Small boundary rasterization differences in independent source renders are recorded explicitly.

No final mark is selected. Production logos, favicons and both website themes are unchanged. These checks establish construction and basic raster legibility; beauty and recognizability remain human review judgments.
