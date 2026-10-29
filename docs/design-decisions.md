# Theme 2 implementation decisions

Reference: [canonical design system](design-system.md), owner supplied 20 October 2026. The original design remains theme 1 by explicit request.

## Routes and preservation

- `/` and unprefixed studio pages use theme 2. `/theme1/` and `/theme2/` are explicit, independently reloadable static routes. Directory redirects support `/theme1` and `/theme2` without the final slash on GitHub Pages and Python's local server.
- Every studio policy, support and product page is also emitted under both prefixes. Navigation stays within the selected prefix. No query parameters, local storage, cookie or JavaScript theme detector is involved.
- Theme 1 snapshots are in `site/theme1/`; its CSS and branding assets remain unchanged. Theme 1 rendering changes only route targets, the `data-theme` diagnostic attribute and `noindex` metadata.
- Unprefixed pages are canonical. Explicit theme previews use `noindex, follow` and point to the equivalent unprefixed canonical URL to avoid duplicating indexed content. The sitemap lists canonical content only.
- BrewPoo and 四方雲集 retain their independent product pages. These are product-specific destinations linked from the shared support directory, not studio theme previews.

## Identity — approved Polish B production system

Polish B is the owner-approved final master. Production uses its frozen paths and SHA-256 provenance in `public/brand/source/master.json`; the 100-unit source is scaled exactly to a 512-unit artboard, with no silhouette or positioning changes. A single silhouette filled by a vector pattern preserves the approved seam-free confluence rendering. No raster, masks or external references are used.

The latest production brief supersedes the exploration-only restrictions. One related Micro C is authorized for small sizes. Theme 2 and default routes receive the final identity; theme 1 and its original assets remain preserved. On this static GitHub Pages site, `public` is a real URL directory, so assets are served from `/public/brand/`, not an assumed framework public-root mapping. `/brand/` and `/theme2/brand/` provide the reference page.

Portable lockups use outlined glyphs, with editable text sources and licensed fonts retained separately. Master geometry is never sourced from typography. Light artwork uses the existing dark-aqua token for stronger graphical contrast. Final size, spacing and favicon decisions are recorded in `docs/brand-production.md` after visual QA.

## Explicit choices and scoped deviations

- **Updates navigation omitted for now:** the recommended navbar contains Updates but the homepage treats that section as optional. No confirmed release/update content has been supplied. We keep Products / About / Contact rather than create an empty or invented updates destination. Add it when real updates exist.
- **Tablet product headings use the supplied H4 scale (22/30):** the three-column layout between 768 and 1023px needs compact titles; larger screens use H3 (28/36). Semantic heading levels remain unchanged.
- **Light UI mode is not implemented:** optional in the source. Required light-background logo assets and light design tokens are included. Theme 1 is the preserved earlier design, not a light version of theme 2.
- **Hero uses Display L (56/62), rather than Display XL:** both are supplied scales. This keeps the two-line proposition restrained. Mobile uses 42/48 as specified.
- **Services remain a short About subsection:** required by the earlier company-site brief, framed as selected work alongside owned products. It is not a primary service-selling section.
- **No product screenshots added:** supplied product icons and verified descriptions are retained. There is no need to invent or synthesize UI.
- **Contrast takes priority over a token's name:** secondary text is used for small copy on elevated surfaces where the muted token would fail AA. Muted/disabled tokens remain available for appropriate future use. Dark aqua is not used as small text on light backgrounds; light logo accents are graphical shapes, not text.
- **Motion is limited to 180ms UI transitions and a 2px card lift:** reduced-motion removes both. No hero animation or glow is needed.

No other visual deviations are intended. New deviations must be recorded here with a reason and scope before implementation.

## Local release preparation — 24 October 2026

The owner chose to retain `page.clearcanvas.app` for the first release because `covanlabs.com` does not currently resolve. CNAME is the single source for generated canonical/social URLs and the sitemap. The Covan identity and email naming remain unchanged. Theme 1 source snapshots stay untouched; only the generated publication hostname is normalized. Publishing is explicitly on hold until the owner approves after local review.

## Release PR authorization — 24 October 2026

The owner authorized pushing an isolated release branch and creating a PR for manual merge during 29 October 2026, 15:15–16:30 HKT (07:15–08:30 UTC). This supersedes the earlier hold on all pushes only for the release branch/PR. It does not authorize merging, pushing to `main`, auto-merge or an immediate deployment. See `release-2026-10-29.md`.
