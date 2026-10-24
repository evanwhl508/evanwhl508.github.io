# Covan Labs / 高凡

Official developer and studio website for Covan Labs, an independent software studio founded and operated by Evan Wong in Hong Kong.

Prepared publishing URL: **https://page.clearcanvas.app/**. The eventual studio domain is `covanlabs.com`; migration is deferred. `CNAME` supplies the generated publication hostname. **Release PR only: do not merge or publish before the owner acts during the 29 October 2026, 15:15–16:30 HKT release window.** Local changes do not configure DNS, mail or account verification.

## Local preview

The checked-in static output can be previewed without installing dependencies:

```sh
python3 -m http.server 4173 --bind 127.0.0.1
```

Open http://127.0.0.1:4173/ (theme 2 by default), `/theme1/` (preserved original) or `/theme2/` (explicit current design). The port is arbitrary; themes are selected exclusively by the path. GitHub Pages serves the same static files. Directory routes work with or without a trailing slash (the host redirects to the slash).

## Content

- `index.html`: studio positioning, products, About, services and contacts.
- `assets/site.css`: preserved theme 1 styles.
- `assets/theme2.css`: canonical theme 2 design tokens and components.
- `assets/fonts/`: locally hosted Inter variable font and its SIL OFL license.
- `assets/navigation.js`: small progressive enhancement for the theme 2 mobile menu; it does not select a theme or store preferences.
- `logo/`: current vector identity, transparent PNG exports, monochrome and light variants, social preview and the current logo refinements.
- `assets/covan-mark.svg`: preserved theme 1 mark and favicon.
- `assets/social-card.svg` / `.png`: preserved theme 1 social preview. Theme 2 uses `logo/social-card.svg` / `.png`.
- `assets/apple-touch-icon.png`: preserved theme 1 icon; theme 2 uses `logo/apple-touch-icon.png`.
- `/privacy/`, `/terms/`: website policies, separate from app policies.
- `/support/`: product help and policy directory.
- `/products/mj-actuary/`: product page, with `/privacy/` and `/terms/` underneath.
- `/products/maidday/privacy/`: link to the maintained policy on `maidday.app`, rather than a second copy.
- `/mj-actuary/privacy.html`, `/mj-actuary/terms.html`: legacy URLs that redirect to the new product policy pages, with ordinary fallback links.
- `/brewpoo/`, `/mahjong4w/`: existing product support and policies, retained with the new support email.
- `robots.txt`, `sitemap.xml`, `404.html`: crawler guidance and fallback page.
- `app-ads.txt`: existing authorized seller record, preserved unchanged.

Product domains remain independent. Product icon sources: existing MJ Actuary asset, Maidday website favicon, and ClearCanvas apple-touch icon. Product policy changes should be made in their canonical locations. MJ Actuary policy substance and original effective dates are retained; studio identity/contact updates are dated separately. Existing app-specific developer ownership references remain where relevant.

## Theme editing and generation

The canonical source is [docs/design-system.md](docs/design-system.md). Any deviation must be recorded in [docs/design-decisions.md](docs/design-decisions.md).

- `site/theme1/` freezes the previous HTML/CSS. Do not restyle it when editing theme 2.
- `site/theme2/home.html` is the current homepage content.
- `site/pages/` holds shared document content for the default/theme 2 pages. Theme 1 remains the preserved snapshot.
- `scripts/build-site.py` emits each studio page at its canonical path and under both theme prefixes. It also shares the navbar/footer shell. All internal studio navigation stays within its current theme prefix.
- Explicit theme routes are `noindex, follow`, with canonicals pointing to the unprefixed site. The sitemap contains only canonical URLs. Existing app-specific product sites remain independent.
- `_config.yml` excludes source templates, docs, tooling and QA output from GitHub Pages publishing.

After changing templates or shell code:

```sh
python3 scripts/build-site.py
python3 scripts/check-site.py
```

Generated HTML is checked in, so GitHub Pages requires no custom build environment. Run the generator before committing source changes.

## Brand assets

**Polish B — Confluence C is the final approved master.** Review the production identity at `/brand/` (or `/theme2/brand/`). Canonical assets and the downloadable kit are in `public/brand/`. The website uses Inter 600 / 425 and the monochrome Micro favicon. Theme 1 remains unchanged.

See [production guidelines and reproduction workflow](docs/brand-production.md). `scripts/build-brand-production.py` generates vectors from frozen approved paths, `scripts/export-brand-production.js` exports PNGs through Playwright, and `scripts/finalize-brand-production.py` packages the kit and maintains old asset URLs. `scripts/check-brand-production.py` verifies geometry, portable SVGs, dimensions, transparency and contrast. `scripts/logo_component.py` is the reusable static logo component.

The master is not regenerated from historical exploration parameters. Do not run old exploration generators as a production workflow.

## Email identity

| Address | Purpose |
| --- | --- |
| `contact@covanlabs.com` | Monitored business correspondence, Google / D&B / organization verification |
| `support@covanlabs.com` | Public product support and store support contact |
| `no-reply@covanlabs.com` | Automated outbound email only; never use for verification or support |

All three inbound addresses can forward to one verified destination mailbox. Inbound forwarding does not configure authenticated outbound sending. Configure sending separately for automated messages and for replies that should come from the domain. See [Cloudflare routing setup](https://developers.cloudflare.com/email-service/get-started/route-emails/) and [sending setup](https://developers.cloudflare.com/email-service/get-started/send-emails/).

## Launch checklist — external setup still required

- [ ] Confirm `Covan Labs / 高凡` matches the registered business identity used for BR, D-U-N-S, Google Payments and Play Console. Do not publish the BR number.
- [ ] Configure and test `contact@` and `support@` inbound routing before publishing these addresses. Verify the destination mailbox; test delivery from another account and check replies.
- [ ] Configure outbound sending for `no-reply@` when an app needs it, including the chosen sender's DNS authentication records. Use `support@` as Reply-To where appropriate.
- [ ] Add and verify the domain in the GitHub account, configure apex DNS for GitHub Pages, set the repository Pages custom domain to `covanlabs.com`, and enable HTTPS after the certificate is available. Follow [GitHub's custom domain instructions](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).
- [ ] Coordinate publishing `CNAME` with DNS. It replaces `page.clearcanvas.app`; one Pages site does not retain two custom-domain bindings. Arrange a redirect on the old domain to the new one, preserving paths, for existing store links and bookmarks.
- [ ] Deploy the site and check the homepage, policies, support, legacy redirects, share image and `https://covanlabs.com/app-ads.txt` over HTTPS.
- [ ] Create a Search Console **Domain property** for `covanlabs.com`, add the exact DNS TXT verification token issued by Google, verify it and retain the record. Submit `https://covanlabs.com/sitemap.xml`. See [Google's ownership verification instructions](https://support.google.com/webmasters/answer/9008080). No placeholder token is included in this repo.
- [ ] Update store developer website/support links and AdMob to the new domain; keep the authorized seller line unchanged.
- [ ] Check that hosting/email behavior and product facts still match the published privacy policies at launch.

No DNS, email routes, outbound mail service, Search Console property, store listing or business verification account has been configured by these repository changes.

## Historical logo studies

Earlier studies remain under `logo/` for provenance. The final approved source is `logo/h1-polish/polish-b/mark-primary.svg`; its checksum is frozen in `public/brand/source/master.json`. Previous temporary website assets are archived in `logo/archive-provisional/`. The production workflow above supersedes the review workflows.
