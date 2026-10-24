# Covan Labs — Selected A, optical finishing

**Historical finishing round:** Option A / Balanced was selected as the base direction. The owner has since reopened [primary exploration within Confluence C](logo-confluence-primary.md), with a separate future Micro C. The current task is to finish that identity through three optical refinements, not invent new concepts. Review: `/logo/confluence-finish/`. No final optical variant has been automatically approved or promoted.

## Three refinements only

| Variant | Change |
| --- | --- |
| A1 — Current benchmark | Exact selected A contour, source ribbons, overlap, proportions and wordmark. |
| A2 — Refined confluence | Identical silhouette to A1. Slightly smaller aqua overlap; independently positioned inner/outer endpoints and curved seams produce a gently rising transition. |
| A3 — Refined silhouette | A2’s overlap, a shorter reverse bend at the upper terminal and 97.5% horizontal scale around x=47.5. The fuller lower return is preserved under that same 2.5% width reduction. |

Focus: optical balance, curve smoothness, terminal tension, confluence integration and small-size legibility. Do not change the underlying identity. The current Inter wordmark remains Covan 600 / Labs 425, with its existing 6px increase in breathing room from the mark.

The source ribbons continue to share tangent-continuous spine contours. Their intersection defines aqua; the revised seams are curved, not radial straight cuts. A3 applies the same horizontal transformation to the overlap and outline, keeping the confluence integrated.

## Proofs

Each variant is shown in monochrome and aqua at native **16 / 24 / 32 / 64 / 256px**, with actual-size navbar lockups. White/navy/black and dark/light two-color exports are included. The 256px proofs are raster PNGs displayed without resizing, matching the smaller tests.

Browser-tab previews use the actual 16px PNG on neutral dark and light tab surfaces. They are labeled previews, not claimed screenshots of browser chrome. Each variant also has dark and light favicon-test documents that load the corresponding real PNG in the browser tab; browser chrome follows the user’s browser theme.

Construction diagrams and source curves remain available in collapsed details, keeping the review focused on the finished identity.

## Reproduction

- `scripts/confluence-finish-geometry.py` derives only from selected A in `confluence-flow-geometry.py`. A1 is copied without geometric edits.
- `scripts/build-confluence-finish.py` reuses existing SVG rendering helpers and the outlined supporting wordmark. Run with standard Python.
- `scripts/export-confluence-finish.js` runs through Playwright CLI `run-code` on the local preview, exporting native raster sizes at device scale factor 1.
- `scripts/check-confluence-finish.py` validates A1 preservation, A2 silhouette equality, A3’s exact width transformation and preserved lower curves, native continuity/open counter, colorway geometry and aqua proportions. It packages the proofs.

The exact sources are in `manifest.json`; measurements and validation results are in `checks.json`. Geometric and raster checks do not substitute for the owner’s aesthetic decision.

The selected base is recorded in the canonical design documentation. Production logos, favicons and theme files are not replaced until the final optical variant is chosen.
