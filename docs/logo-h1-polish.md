# Covan Labs — H1 master, final optical polish

**H1 Elegant Hybrid is the owner-selected master direction.** Current review: `/logo/h1-polish/`. Show only the unchanged H1 benchmark and two final optical-polish alternatives. No new concepts, silhouette families or favicon optimization.

## Scope

- **H1 benchmark:** preserve the selected source geometry, colors and current lockup exactly.
- **Polish A:** retain the complete H1 silhouette and aqua filled area. Adjust the curved confluence boundaries slightly toward the local source-contour tangent directions for a more fluid transition.
- **Polish B:** use A’s confluence with a very slight upward optical adjustment. Reduce lower-terminal visual mass by approximately 2–3%, without changing the tall, open body proportions. Stay within H1’s character.
- **Spacing:** compare the existing mark-to-wordmark spacing with 2px more at actual navbar size. Keep Inter at Covan 600 / Labs 425. Align the mark positions between spacing rows so the only difference is the gap.
- **Presentation:** 256 / 128 / 64px and actual navbar lockups, monochrome and aqua, with light-background proofs. No 16/24px exports or Micro C work in this round.

## Implemented optical changes

Polish A’s outline is byte-for-byte the same path as H1. Its curved source seams are reshaped, then their endpoints are reattached symmetrically along the actual spine contours to preserve the exact integrated overlap area. The endpoint control vectors retain their edited tangent directions. The aqua remains the real intersection of the upper/lower source forms, not a separate block.

Polish B uses those same seam curves, reattached **0.5 units upward in the 100-unit coordinate system**. That is 1.28px at 256px and 0.18px in the 36px navbar mark box. A very small symmetric reattachment correction retains the overlap area after the lift.

The lower-tip reduction is measured as **2.5% less filled area in the lower terminal region to the right of x=65**, shown by a dotted line in the detail proof. The reduction shifts the terminal’s inner endpoint and adjoining control points outward by approximately 0.45 horizontal / 0.33 vertical units. The outer body arcs, upper terminal, left spine and body proportions are unchanged. This measures a controlled local area reduction, not a 2.5% reduction of the entire logo or a claim about quantified human visual perception.

The exact aqua area is held at the benchmark’s geometric value for both alternatives. Small differences in raster-measured percentage reflect antialiasing and B’s slightly smaller total filled area; they are not an intentional increase in aqua.

The spacing test adds exactly 2px to the wordmark’s x-origin at the established navbar scale. The mark and type sizes, weights, letter shapes and baseline remain the same.

## Sources and checks

- `scripts/h1-polish-geometry.py`: copies H1 from the hybrid source, integrates cubic-path areas, edits the source seams and solves the local lower-tip reduction.
- `scripts/build-h1-polish.py`: builds the review and current / +2px lockups.
- `scripts/export-h1-polish.js`: renders native 64/128/256px PNGs at device scale factor 1.
- `scripts/check-h1-polish.py`: checks benchmark preservation, A’s unchanged silhouette, retained overlap area, B’s local reduction/position changes, primary-scale output and packages the review.

Run the standard-Python builder, export through Playwright CLI `run-code` from the local preview, then run the checker with Pillow available. `manifest.json` contains exact source geometry and measurements; `checks.json` records validation.

H1 is selected as the master direction. Final polish and spacing are pending review. The production website identity and themes are not automatically replaced by generating these alternatives.
