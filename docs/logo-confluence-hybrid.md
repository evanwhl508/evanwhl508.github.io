# Covan Labs — Final hybrid logo refinement

Status: **H1 Elegant Hybrid selected as the master direction**. The hybrid studies remain at `/logo/confluence-hybrid/`. Continue to [H1 final optical polish](logo-h1-polish.md) at `/logo/h1-polish/`.

## Current owner direction

Preserve 01 Elegant Flow’s tall, slightly slim, open silhouette as the primary foundation. Introduce restrained asymmetry and terminal personality from 03 Organic Balance. Borrow only enough discipline from 02 Architectural Precision to keep the geometry confident. Do not import 03’s heavy lower body or 02’s square proportions, enterprise weight or rigid construction.

The identity remains a simple, immediately recognizable Confluence C: elegant, fluid, calm, premium, technical and intentionally drawn. No new concepts, extra symbols or hidden-letter puzzles. The opening should carry distinctiveness without becoming a mouth, smile, arrow, V, heart, speech bubble or broken ring.

## Exactly three studies

- **H1 — Elegant Hybrid:** closest to 01. A slightly firmer spine, gently drifting inner counter and restrained upper terminal; the lower return stays extended and light.
- **H2 — Signature Hybrid:** the most expressive opening. A compact receiving curve above and a longer inward return below create stronger asymmetry, while the slender body and controlled lower sweep remain anchored in 01.
- **H3 — Structured Hybrid:** a more regular oval skeleton and cleaner terminal faces add discipline. The body stays tall and light, without square shoulders or bulky proportions.

These are refinements of the same identity. No study is automatically preferred based on its name or stated target.

## Geometry and confluence

Each mark is directly drawn from cubic SVG curves. The upper and lower source ribbons share tangent-continuous spine contours. Their union defines the primary outline; their curved intersection defines aqua. No font glyph is an input to the symbol.

The spine is slightly stronger than 01, and the lower sweep gains only controlled fullness. The counter is optically placed rather than concentric. The upper and lower terminal directions remain different. Local corrections are approximately 5–8% where useful; this is not a uniform stroke-width transformation.

Colors remain deep navy `#08111F`, cool white `#F4F7FA` and aqua `#39C6C8`. The latest brief restores a **roughly 6–10% filled-area** aqua target. The actual shared region follows the body contour and uses curved seams; it is not an independently attached block or radial sector. Monochrome proofs use the identical outline.

The supporting outlined Inter wordmark remains **Covan 600 / Labs 425**, with its existing breathing room. This gives each study the same restrained lockup for comparison.

## Presentation and responsive identity

Evaluate at **256 / 128 / 64px and actual navbar size**. Each study includes:

- Large monochrome and two-color marks.
- Pure white/navy/black and dark/light two-color proofs.
- Native primary-size PNGs and the navbar lockup.
- Visible construction/curve overlay and opening close-up.
- Independent upper/lower source forms and their merged result.

16/24px images are direct reductions in a secondary disclosure, not proposed favicon masters. A simplified Micro C can be derived only after primary selection. No master geometry is optimized against a 16px gate in this round.

## Reproduction and verification

- `scripts/confluence-hybrid-geometry.py`: three hybrid contour sets; uses the existing source-overlap construction from `confluence-primary-geometry.py`.
- `scripts/build-confluence-hybrid.py`: generates SVG assets, comparison sheets, opening details and the review pages.
- `scripts/export-confluence-hybrid.js`: exports native PNGs through Playwright CLI at device scale factor 1.
- `scripts/check-confluence-hybrid.py`: checks primary-scale geometry/raster continuity, open counters, monochrome integrity, aqua area and assets, then packages the review.

Run the builder with standard Python, pass the export script to Playwright CLI `run-code` from the existing local preview, then run the checker with Pillow installed. Exact geometry is recorded in `manifest.json`; validation and measured aqua areas are in `checks.json`.

These checks establish construction and output integrity, not subjective beauty, ownability or trademark clearance. Production identity files and themes remain unchanged pending final selection.
