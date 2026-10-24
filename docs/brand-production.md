# Covan Labs production identity

Approved master: **Polish B — Confluence C**. Meaning: two origins, Cobie and Evan, converge into one identity. No new silhouette family, symbols or hidden letters were introduced in production.

## Source and geometry

`source/master.json` in the identity kit freezes the approved silhouette and confluence with the SHA-256 of `logo/h1-polish/polish-b/mark-primary.svg`. All master coordinates scale exactly by 5.12 to a 512 × 512 viewBox. The existing optical position is preserved. A vector pattern colors one continuous silhouette, avoiding antialiasing seams along overlapping edges. No masks, raster assets, external references or font glyphs create the mark. The production master and approved source rendered identically at 512px in Chromium (all RGBA channel differences zero).

The editable source, production generator and checksum are the authority. Do not use historical exploration assets as alternatives. Changes to the master require explicit design approval.

## Color and typography

| Role | Color |
| --- | --- |
| Navy | #08111F |
| Cool white | #F4F7FA |
| Aqua | #39C6C8 |
| Silver | #9EADBD |
| Light-background aqua | #15999C |
| Print black | #000000 |

Primary artwork uses cool white and aqua on navy. Light artwork uses navy and dark aqua; the latter has 3.25:1 graphical contrast on the light reference surface. Logos are not body text: do not reuse the accent for small light-background copy without checking text contrast. No gradients, glow or shadows.

Inter remains the wordmark family after an actual-size comparison with Manrope. Its more compact, precise rhythm fits the existing identity; Manrope does not provide a material improvement. Covan is 600, Labs 425, optical size 24. Production lockups have outlined glyphs. The editable SVG uses live Inter text; licensed font files are included in the source folder. Localized lockups outline only 高凡 from Noto Sans TC 400. The Chinese name is secondary.

The mark-to-wordmark visible gap is approximately 0.56× visible mark height. The navbar lockup is approximately 184 × 40 CSS px. No letters have been made unusual to compete with the mark.

## Responsive use and minimum sizes

- Standalone master: 64px artboard and above.
- Approved horizontal navbar lockup: at least 160px wide; recommended 184px. The lockup is an explicitly tested compact exception to the standalone threshold. Use its supplied proportions.
- Micro C: 16–48px. Its slightly thicker counter, wider terminal clearance and simplified confluence are isolated from master geometry.
- Below 160px available width for the whole logo, use a Micro mark alone instead of shrinking the lockup.
- Monochrome favicon B is selected: the continuous luminance of its spine is clearer at 16px than the aqua interruption. Candidate A remains available for review/use at larger compact sizes. Both were checked at 16, 24, 32 and 48px on dark/light browser chrome.
- Browser favicons use a navy tile to remain legible on either chrome color. Apple/Android icons and avatars use the padded master on navy; these are deliberately opaque. All general logo PNG exports are transparent.

## Clear space

x = the master left-middle stroke thickness: (27.8 − 14) × 5.12 = **70.656 master units**. Leave at least 1x around all visible ink, for either the mark or the entire lockup. At a 36px mark artboard this is approximately 5px. The SVG canvas does not automatically provide that clearance. `proofs/clear-space.svg` illustrates the exact exclusion boundary. Lockup clear space uses the same measurement scaled with its mark.

## Assets and routes

The canonical files live in `public/brand/`. This is a static GitHub Pages repository, so their URL begins `/public/brand/`; no framework strips `public`. The brand reference is `/brand/`, with `/theme2/brand/` as the explicit theme 2 route. Theme 1 snapshots, styling, original branding and assets remain intact. Old temporary `/logo/covan-*` URLs are compatibility copies; the replaced temporary set is archived separately.

The complete zip includes SVGs, PNGs at 512/256/128/64/32px widths, native-size Micro exports, favicon candidates, Apple/Android icons, avatars, Open Graph artwork, editable sources and font licenses. Small PNGs of full lockups are compatibility exports, not recommended display sizes. Use the size rules above.

## Reusable component

The static site's `scripts/logo_component.py` provides `logo(variant='primary', layout='horizontal', size='md', decorative=False)`.

- Variants: primary, light, white, navy, monochrome.
- Layouts: mark, horizontal, stacked, localized.
- Sizes: xs, sm, md, lg, xl.
- Mark layout automatically uses Micro below 64px. Full lockups enforce minimum heights; never force them smaller with CSS.
- Asset mapping is centralized. Geometry is not duplicated in HTML components. Theme 2's navbar and footer use this component. Below 360px viewport width the navbar uses the Micro mark so the horizontal lockup never gets compressed. No React runtime is needed for a static site.

## Incorrect use

Do not stretch, rotate, recolor arbitrarily, change proportions, add gradients/shadows/outlines, make the whole mark aqua, rearrange geometry, modify the confluence or place on low-contrast backgrounds. Do not force the master into tiny interfaces. Use the supplied light/monochrome variants and Micro tier.

## Reproduction

Requires Python with `fonttools[woff]` (asset generation), Pillow (validation), and the Playwright CLI for browser PNG export. Fonts and licenses are bundled; font sources: Google Fonts `ofl/manrope` and `ofl/notosanstc`; existing Inter license is retained.

1. Run `scripts/build-brand-production.py` with the fontTools-enabled Python environment.
2. Run `python3 scripts/build-brand-reference.py` and `python3 scripts/build-site.py`.
3. Serve the repository on any local port. Run `scripts/export-brand-production.js` using Playwright CLI (adjust its local origin if needed).
4. Run `python3 scripts/finalize-brand-production.py` to package exports and update compatibility URLs.
5. Run `scripts/check-brand-production.py` with Pillow/fontTools and `python3 scripts/check-site.py`.
6. Run `scripts/qa-brand-production.js` through Playwright and inspect its screenshots under `output/playwright/`.

No deployment, DNS, email routing or external account change is part of this production task.
