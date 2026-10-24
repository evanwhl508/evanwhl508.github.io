# Covan Labs — Two-Origin C

Status: **five monochrome variations of one construction; none approved**. This owner brief supersedes the wordmark-led A/B round, the ten-symbol exploration, and earlier Modular C studies. Retained reference review: `/logo/two-origin/`. The owner identified studies 01 and 04 as the strongest references. The next round is [Confluence C](logo-confluence.md) at `/logo/confluence/`; no final mark has been selected.

## Current brief

Create a simple, beautiful, recognizable C with one dedicated construction idea. It must immediately read as C, retain clarity below 24px and have character independent of color or explanation. Draw the mark from SVG geometry; do not use a font C as its source. The supporting Covan Labs wordmark remains restrained and consistent.

Covan comes from Cobie + Evan. Two independent curved forms should visually combine into one C; their origin can be explained afterward. Avoid puzzles, yin-yang, chain links, obvious two-color halves, a broken C, modular-tech styling, crypto-like forms, hidden alphabets or added geometry solely for a story.

Only five or six variants are requested. This set has five and varies only curvature, opening, terminal geometry, negative space and asymmetry. Metal / Water remains a design discipline of precision, circular geometry, balance, flow and openness. Beauty takes precedence over symbolism.

Monochrome only. Introduce aqua only after the owner approves geometry. No automatic selection or numerical aesthetic score.

## One construction used throughout

The mark is built from **two eccentric circular ribbons**. Each is one independent closed shape with an outer arc, inner arc and closing edges.

1. Their outer circles have a common left-hand tangent at the back of the C. Upper and lower radii may differ.
2. Their inner circle centres sit on opposite sides of the horizontal joining axis. Each inner circle passes through the same counter point.
3. Those two inner arcs create one shallow cusp in the counter. This visible meeting is the construction detail; it does not require a seam or additional part.
4. Each exposed terminal is cut along the normal of its corresponding inner circle, retaining a substantial end rather than a sharp tip.
5. The final mark follows the two outer arcs and two inner arcs as **one continuous SVG outline**, removing their shared joining edge. It is the geometric union of the two source ribbons.

The upper and lower source shapes are shown individually. The grid shows the actual circles, centres, common tangent, counter meeting point and terminal cuts. It is not a decorative explanation drawn over unrelated geometry.

The name connection is simply: **two origins forming one C**. Neither ribbon is assigned a personality or business role. The construction is specific to this study, but no claim of trademark exclusivity or verified market uniqueness is made.

## Five variations

| Variant | Variable emphasized |
| --- | --- |
| 01 — Upper sweep | Larger upper outer radius; the upper curve carries farther forward. |
| 02 — Lower sweep | More lower curvature and a changed inner-centre balance. |
| 03 — Deeper counter | Increased spine width and inner-circle offset. |
| 04 — Inclined opening | Unequal opening angles give the aperture a stronger inclination. |
| 05 — Open crown | A wider upper opening with a shorter inner-radius pair. |

All five use the same construction function and unchanged supporting lettering. Parameter values and exact paths are in `logo/two-origin/manifest.json` and on the individual review pages.

## Presentation

The overview shows merged silhouettes, actual navbar lockups and native 16/24/32/64px samples. Each variant page shows:

- White on dark and navy on light.
- Merged silhouette and native-size tests.
- The same Covan Labs lockup at a 36px mark box / 20px wordmark cap height.
- Origin 1, Origin 2 and the final merged shape separately.
- True construction grid and parameter table.
- Downloadable SVGs and transparent 512px proofs.

No winner is selected. The human review remains whether the C looks intentional, attractive and recognizable before the construction is explained.

## Source separation and reproduction

- `scripts/two-origin-geometry.py` uses only standard-library mathematics. It contains no font import, glyph extraction or reference to typography. This is the complete source of all mark contours.
- `scripts/build-two-origin.py` generates the five variants, independent origins, grids, review pages and comparison sheets. It reads the previously outlined Inter supporting wordmark solely for the text beside the mark. Changing the text cannot change the C geometry.
- `scripts/export-two-origin.js` runs through Playwright CLI from the local review. It renders all five native sizes in both monochrome colorways, plus independent two-ribbon union proofs and dark/light comparison sheets.
- `scripts/check-two-origin.py` validates monochrome output, dimensions, source counts, continuity at the joining tangent and union equivalence, and packages the studies.

The first internal test used a smooth counter and still resembled a conventional glyph. It was rejected before this review set. Only the paired-arc cusp construction is presented here.

## Scope

Earlier reviews are archived and point to this round. Existing website branding, theme 1, theme 2, social images and production favicon remain unchanged. No logo has been promoted, no site deployed, and no accent color introduced.

## Validation record

- Five union proofs: rendering Origin 1 and Origin 2 together produces the exact same 512px alpha silhouette as the merged path.
- Fifty transparent PNGs checked for native dimensions, monochrome fill and unclipped bounds.
- At 16/24/32/64px, every mark is one connected ink component and its counter remains open to the right. White/navy native-size silhouettes match exactly.
- At 512px, Chromium produced a coverage difference at one boundary pixel in variant 01 between white and navy. The SVG geometry is identical; this is recorded explicitly in `checks.json` rather than claimed as pixel-identical output.
- Thirty responsive page checks across 320/390/768/1200/1440px passed, including native-size rendering and 25 keyboard disclosures. No page overflow, missing images or script errors were detected.
- Static validation passed for 54 HTML pages and 1,562 local links/assets. Theme 1 snapshots remain preserved; all 28 existing production identity/homepage files match their earlier hashes.

These establish source fidelity and rendering behavior. Beauty and long-term brand fit remain the purpose of the owner's review.
