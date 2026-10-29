# Covan Labs — Primary Confluence C directions

Status: **retained source studies** at `/logo/confluence-primary/`. The owner selected 01 as the primary foundation, 03 for restrained personality and 02 for limited structure in the [final hybrid refinement](logo-confluence-hybrid.md) at `/logo/confluence-hybrid/`. This latest owner brief supersedes the preceding A1–A3 optical-finishing scope while retaining the same Confluence C identity concept.

## Responsive identity

1. **Primary mark:** evaluate beauty, silhouette, proportion and signature at 256, 128 and 64px, and in the actual navbar lockup. Do not weaken this identity to preserve every detail at 16px.
2. **Micro C:** derive separately after primary approval. It may simplify curves/confluence, widen the opening, increase contrast, remove details or use monochrome. Its geometry need not match the master exactly; both should feel like one identity.

No Micro C or new favicon is created in this round. The 16/24px exports are direct reductions of each master, provided only as secondary references in collapsed sections. Their appearance is not a primary design acceptance criterion.

## Exactly three directions

| Direction | Silhouette and opening | Confluence |
| --- | --- | --- |
| 01 — Elegant Flow | Taller, slimmer oval body; generous counter; long lower sweep; controlled receiving curve at the upper terminal. | Soft, lower-set transition following the slender spine. |
| 02 — Architectural Precision | Firmer rounded shoulders; compact structured counter; deliberate terminal faces with different tensions. | A disciplined curved joint moving through the spine, rather than a horizontal band. |
| 03 — Organic Balance | Broad upper arc; asymmetric counter; fuller lower return and changing visual weight. | An oblique, softer shared region following the changing inner/outer contours. |

The differences are authored changes to whole contours, counter proportions, mass distribution and terminals—not 2–3% transforms. Each still reads immediately as C. There are no added symbols or hidden-letter puzzles.

All three use direct SVG cubic geometry. Each contains two originating ribbons sharing the spine contours; their union is the primary C and their intersection is the aqua region. Curved seam positions and tensions are independently authored for each direction. The supporting Inter wordmark remains 600 / 425 with unchanged spacing, allowing a fair comparison of the marks themselves.

The latest brief allows aqua shape and proportion to change meaningfully. Earlier fixed percentage targets are not acceptance gates for this round. The navy, cool-white and aqua brand palette remains unchanged; the mark must also work in monochrome.

## Presentation

The gallery shows large monochrome and aqua versions first, then 128/64px and navbar lockups. Detail pages add light backgrounds, pure navy and black, source ribbons and construction controls. Each mark is shown at its native raster dimensions. Primary comparison sheets contain no 16/24px proofs.

Secondary reductions are explicitly labeled as unmodified master references, not the future Micro C. The review favicon remains the existing production favicon to avoid implying micro approval.

## Source and verification

- `scripts/confluence-primary-geometry.py`: three independently authored cubic contour sets and their source intersections; no font outlines.
- `scripts/build-confluence-primary.py`: builds the review, SVGs, construction proofs and constant supporting wordmark.
- `scripts/export-confluence-primary.js`: native PNG export at device scale factor 1, plus large comparison sheets.
- `scripts/check-confluence-primary.py`: validates assets and primary-scale continuity/open counters, records aqua areas and packages the review. It does not judge 16/24px reduction quality or enforce favicon constraints.

Run the builder with standard Python, export through Playwright CLI `run-code` from the local preview, then run the checker with Pillow available. Exact contours are in `manifest.json`; measured output is in `checks.json`.

No primary direction is automatically selected. The production website identity remains unchanged. Micro development follows the owner’s primary selection as a separate task.
