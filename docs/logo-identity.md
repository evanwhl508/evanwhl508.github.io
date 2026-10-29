# Covan Labs — two restrained identity directions

Status: **archived following owner feedback that the marks were too close to ordinary glyphs**. The current source is [Two-Origin C](logo-two-origin.md), reviewed at `/logo/two-origin/`. The remainder records the previous round. This owner brief supersedes the ten-symbol exploration and earlier Modular C refinements. It simplifies the process rather than expanding it.

## Current brief

Develop only two directions, with two or three serious refinements per direction. This set contains **two per direction: A1, A2, B1, B2**.

**A — Wordmark-led identity:** Design “Covan Labs” through proportions, terminals, spacing and selected letter geometry. The standalone C must be born from the wordmark and extracted naturally from its first letter. It must not be a separately designed icon paired with unchanged type afterward.

**B — Refined C:** Recover the earlier mark’s immediate readability while removing the modular technology-icon feeling. Focus on proportion, curvature, negative space and one restrained detail. Two balanced elements are permitted, not required. Do not add seams merely to illustrate two names.

Both directions start in monochrome only. Introduce aqua only after the owner approves the geometry. No hidden-letter puzzles, forced stories, abstract-symbol batch or numerical beauty scoring. “Metal / Water” remains a visual discipline of precision, circular balance, openness and flowing curves; beauty takes precedence.

The core test is: **Does this look beautiful and unmistakably intentional beside the words Covan Labs at navbar size, with no explanation?**

## What is actually customized

### A1 — Open proportions

- Authored capital C with a broad bowl, controlled overshoot and inclined terminals.
- Authored o with an elliptical counter related to the C, and v with a shallow curved interior join.
- Individually set C–o, o–v, v–a and a–n spacing.
- The remaining letters derive from outlined Inter at weight 520 / optical size 32. This is a customized wordmark, not a newly invented full typeface.
- Labs uses 91% of Covan’s cap height and a deliberately clear word space.

### A2 — Closer proportions

- The same wordmark family with a narrower authored C and more upright terminal cuts.
- Narrower o and v; a/n width adjusted to retain a consistent rhythm.
- Selectively tighter pair spacing; the same Labs scale.

For each A refinement, **the exact path used for the first C is reused in its standalone mark**, with only translation and uniform scaling. There is no separate icon geometry. The primary identity uses the wordmark alone, without a duplicate C symbol preceding the word Covan.

### B1 — Circular balance

- One continuous C contour with an almost circular counter.
- Matched oblique terminal cuts; no module seams.
- A 28px mark sits beside a 20px-cap-height outlined Inter wordmark in the navbar proof.

### B2 — Optical balance

- One continuous C with a more upright bowl and a slightly fuller lower return.
- The same supporting wordmark, spacing and scale as B1, isolating the change in C geometry.
- No claim that the contour encodes initials, a hidden alphabet or a company-origin diagram.

## Review and files

Current review: `/logo/identity/`. `/logo/concepts/` points here. The old ten-symbol gallery and A/B/C round are explicitly archived.

The page starts with actual navbar-sized identities on dark and light backgrounds, then a 2× enlargement, standalone C and native 16/24/32/64px samples. Short refinement notes are collapsed. No scores or automatic winner appear.

Assets under `logo/identity/`:

- Four refinement folders, each with white/navy SVG wordmark, standalone mark and primary identity.
- Transparent marks at 16, 24, 32, 64 and 512px, in white and navy: 40 PNGs.
- Primary identities at actual navbar size and 2×, in both colors: 16 PNGs.
- Dark/light comparison sheets in SVG and PNG.
- Manifest and downloadable ZIP.

All identity lettering is outlined. A’s custom letters are authored SVG contours; the remaining outlines use the repository’s licensed Inter font. Proof-sheet annotations are ordinary sans-serif labels and are not part of the identity.

## Reproduction and scope

Run `scripts/build-logo-identity.py` in a Python environment with `fonttools[woff]`. Then run `scripts/export-logo-identity.js` through Playwright CLI from the local preview. It creates an isolated browser context at scale 1 for exact pixel exports. The local server port is arbitrary; the existing preview uses 4173, not the earlier example port 8080.

The provisional production logo, website themes and social assets remain unchanged. This round does not publish a website or introduce aqua. Further geometry or color decisions await the owner’s review of these four refinements.
