# Direction 01 — Modular C refinements

Status: **archived and superseded by the full concept exploration reset**. Review the current ten concepts at `/logo/exploration/`; see [the current brief](logo-exploration.md). The text below records the earlier round, not a currently selected direction. This owner-supplied refinement brief supersedes any earlier suggestion that the logo geometry was final. The website identity remains provisional and is not replaced by this exploration.

## Owner brief

- **A — Soft Modular C:** keep three pieces; move toward a circular C, with smoother arcs and transitions and a few precise 45° cuts. Reduce octagonal/blocky character. Integrate the aqua terminal into the same baseline and construction logic as the lower white module, as its continuation/end-point rather than a detached square.
- **B — Modular C with Hidden V:** derive from A. Use only negative space or opposing angled cuts for a subtle V. No separate colored V. First glance must read as a C.
- **C — Continuous-flow Modular C:** reduce module separation; three segments should feel like one technical path. Aqua only at the terminal, approximately 10–15% of filled area, without increasing the original proportion.
- Balance circular/flowing geometry and technical cuts. Avoid a G silhouette.
- Test 16, 24, 32, 64 and 512px, including monochrome. The mark must work without aqua.
- No literal V, triangle, hexagon, cube, code bracket or crypto/Web3 visual language.
- Keep Direction 03 discarded. Direction 02 may inform only the hidden-V study; do not retain its literal aqua V.

## Construction

All three use a 64 × 64 viewBox, center (32,32), 26-unit outer radius and 15-unit inner radius. Circular inner and outer boundaries share the same center; the path width is 11 units. The open ends use 45° cuts. The right-hand opening stays unobstructed, with no inward crossbar. Each mark contains exactly three filled SVG paths, no gradients, strokes, masks or background shapes.

A uses a 3-unit horizontal gap between the two white modules and a 6° break before the terminal. Its lower module and aqua terminal use the same concentric arcs, rather than separate square construction.

B retains A’s outer silhouette and terminal. A shallow 2.5-unit dip, made from opposing 45° cuts, bends the left-hand negative-space seam. There is no additional glyph, colored V or isolated triangular element. The hidden detail is intentionally secondary and is expected to become less explicit at small sizes.

C replaces the horizontal division with a narrow 45° cut (approximately 1.2 units perpendicular width) and reduces the terminal break to 2.5°. This makes the three pieces read as segments of a single circular path. At 16px the thin seams may visually merge; recognizable C silhouette takes priority over visible seams.

## Filled-area measurements

| Study | Aqua share |
| --- | ---: |
| Original provisional base | 11.679% |
| A | 11.346% |
| B | 11.346% |
| C | 11.208% |

Values are calculated from sampled circular contours and straight cuts before rasterization. The measured JSON is `logo/refinements/geometry.json`. All three remain below the original aqua proportion and inside the requested 10–15% range. Raster antialiasing can change apparent proportions at favicon sizes.

## Review artifacts

- `/logo/refinements/`: side-by-side comparison with actual-size 16/24/32/64px rows and expandable 512px tests.
- `a-*.svg`, `b-*.svg`, `c-*.svg`: dark/light color and white/navy monochrome vector sources.
- Corresponding `*-16.png`, `*-24.png`, `*-32.png`, `*-64.png`, `*-512.png`: transparent native-size raster tests in all four colorways.
- `scripts/build-logo-refinements.py`: deterministic geometry and review-page generator; does not mutate the current website mark.
- `scripts/export-logo-refinements.js`: browser raster export and review screenshots.

The superseded literal-V and forward-module SVGs have been removed from the active exploration and its generator. The original Direction 01 SVG is retained as a construction reference only. No A/B/C variant is designated final or installed as the website logo.

## Review observations

- A: the three-piece structure remains most explicit in the native-size rows. The terminal follows the lower arc rather than reading as an attached square.
- B: the shallow negative-space V is visible at larger sizes and becomes a simple seam at 16px. Its primary reading remains C; no separate V is added.
- C: the narrow cuts soften or merge at the smallest size, consistent with its continuous-flow intent. The open counter is retained in monochrome.
- Color and monochrome exports have pixel-identical alpha geometry at each size; the silhouette is independent of aqua. All 60 PNGs have transparent backgrounds and the requested pixel dimensions.
- Website identity assets and homepage were hash-compared before/after and remain unchanged. These studies are not a final selection.
