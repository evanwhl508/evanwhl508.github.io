# Covan Labs — Confluence C

Status: **four refinements for review; no final mark selected**. This round is retained for reference at `/logo/confluence/`. The latest [Curved Confluence brief](logo-confluence-flow.md) develops study 02, with restrained influence from 04, at `/logo/confluence-flow/`. Studies 01 and 04 from `/logo/two-origin/` are retained as the two geometric references.

## Brief and scope

The signature should live in the C’s opening: a complementary relationship between the upper and lower terminals. It must remain a simple, immediately readable C. Do not add letters, symbols, puzzles or a new concept family. Avoid heart, V, arrow, puzzle-piece, yin-yang and broken-ring readings.

“Two origins. One continuous identity.” refers to Cobie + Evan becoming Covan. The upper and lower source ribbons join at the back of the C. The terminal relationship gives the finished silhouette a visible gesture; the confluence accent identifies the actual shared join.

The owner now explicitly authorizes color exploration after the successful monochrome test. This supersedes the earlier monochrome-only restriction, without approving a final logo.

- Background: deep navy `#08111F`.
- Main two-color ink: cool white `#F4F7FA`, or navy on light.
- Accent: aqua `#39C6C8`, approximately 12–18% of the filled area.
- Preferred placement: a short curved portion spanning the true join of both source ribbons.
- One alternate placement: the upper source begins in aqua and continues into the white body.
- No gradient, detached terminal block, gap or outline change between color treatments.
- Pure white, pure navy and pure black proofs remain required.
- Wordmark: same Inter family, Covan 600 / Labs 425, 24px at navbar size. Small spacing adjustments; no unusual lettering. The mark contains no font geometry.

## Four refinements

| Refinement | Reference | Terminal relationship |
| --- | --- | --- |
| 01 — Cupped opening | Two-Origin 01 | Concave upper cut and convex lower return; unequal lengths make a gently leaning opening. |
| 02 — Shared inflection | Two-Origin 01 | A shallow reverse curve at the upper terminal, answered by a quieter lower transition. |
| 03 — Staggered return | Two-Origin 04 | An extended upper reach and a rounded lower shoulder; the opening remains off-axis. |
| 04 — Swept opening | Two-Origin 04 | A restrained upper reverse curve and a longer lower sweep. |

The body radii are held to the two selected references. This is a terminal-relationship round, not a set of radius or opening-angle variations. The eccentric inner circles and unequal upper/lower arc systems preserve the existing optical modulation. No additional 5–8% numerical weight target is claimed: that was an optional guide, and the owner’s selected reference proportions are retained.

## Construction and proof presentation

Each refinement has a large monochrome mark first, followed by two-color and light-background proofs, actual 16 / 24 / 32 / 64px raster tests, a real-size 36px-mark-box navbar lockup, separate upper and lower source ribbons, the merged silhouette, a true construction grid, an enlarged opening, alternate origin-color placement and a pure-black proof. Transparent 512px PNGs and SVGs are included.

The source construction consists of four eccentric circular arcs and two custom cubic Bézier terminal curves. The ribbons share the same outer tangent and inner meeting point. The internal joining line is removed in the final single path. Aqua uses a fill partition clipped by that same contour; it cannot add a block or change the silhouette. The approximately 40-degree confluence sector crosses the actual join at the back, producing a short curved band.

The construction diagram shows the actual circles, terminal control handles and removed joining line. It does not imply that the opening is the physical source join: the opening carries the visual relationship, while the back is where the source geometry meets.

## Reproduction

1. Use Python with `fonttools[woff]` for `scripts/build-confluence.py`. Only supporting wordmark outlines use FontTools. The standalone mark source, `scripts/confluence-geometry.py`, uses the standard library and imports the retained reference geometry from `scripts/two-origin-geometry.py`.
2. Open the existing local preview and pass `scripts/export-confluence.js` to Playwright CLI `run-code`. It renders transparent PNGs at exact native dimensions using device scale factor 1.
3. Run `python3 scripts/check-confluence.py` with Pillow installed. It validates the construction, raster continuity, monochrome fills, aqua area and bounds, and builds the download package.

`logo/confluence/manifest.json` contains exact source geometry. `checks.json` records measured aqua areas and raster checks. Tiny Chromium edge-coverage differences, if present, are recorded explicitly; they are not changes to the SVG outline.

The proof gallery is responsive and uses the canonical navy/silver/aqua palette. Pure black and pure white are confined to requested monochrome logo proofs, not adopted as site surface or body-text colors.

Production assets, website logos, favicons and themes are unchanged. No candidate is promoted or ranked. Geometry and raster checks establish construction and basic legibility, not beauty, memorability or legal distinctiveness; those remain review judgments.
