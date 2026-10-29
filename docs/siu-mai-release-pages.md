# Siu Mai Roach Rumble — store website handoff

Prepared 28 October 2026. These are repository changes, not a deployment or an App Store submission. Follow the existing site release window; do not merge or publish automatically.

## URLs after deployment

| App Store Connect field | URL |
| --- | --- |
| Marketing URL | https://page.clearcanvas.app/products/siu-mai-roach-rumble/ |
| Support URL | https://page.clearcanvas.app/products/siu-mai-roach-rumble/support/ |
| Privacy Policy URL | https://page.clearcanvas.app/products/siu-mai-roach-rumble/privacy/ |
| User Privacy Choices URL (optional) | https://page.clearcanvas.app/products/siu-mai-roach-rumble/privacy/#choices |

Use the same pages for English and Traditional Chinese listings; support includes a Traditional Chinese help section. No Simplified Chinese listing changes are included. Public contact: support@covanlabs.com. Do not expose the private App Review email or phone on the website.

The origin comes from `CNAME` (currently `page.clearcanvas.app`), not the future `covanlabs.com` domain. Rebuild and update this handoff if the hostname changes. DNS, mail delivery, domain migration and App Store Connect fields have not been modified.

## Source and behavior evidence

Game checkout: `../siu-mai-td`, current source at preparation time. `Runtime/SaveStore.cs` stores local progress and excludes unfinished attempts. `Runtime/BuildChannel.cs` disables monetization unless explicitly compiled back in and disables diagnostics in TestFlight. `Runtime/GameTelemetry.cs` initializes Firebase only when eligible and opted in. `Runtime/SaveStore.cs` defaults diagnostics to false; `Runtime/MenuScreens.cs` exposes the optional setting only where allowed. `Editor/ReleaseServices.cs` sets native Analytics/Crashlytics collection and IDFA collection defaults off. Paths are under `Assets/SiuMaiTD/`.

The policy describes optional production diagnostics and the current beta exception separately. It does not claim “Data Not Collected” for an unverified final production build. Official references: [Apple review requirements](https://developer.apple.com/app-store/review/guidelines/), [Firebase data handling](https://firebase.google.com/support/privacy), [GitHub Pages visitor logging](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).

## Before App Store submission

- Deploy during the approved site release workflow and verify the three canonical URLs over HTTPS, without authentication; verify support email delivery separately.
- Confirm the final production binary and Firebase configuration match the policy, and make App Privacy answers reflect that binary and its SDKs. The existing beta exception is not a production privacy audit.
- Add accessible support/privacy links inside the game. Website work alone does not add them to Settings.
- Keep the public product page marked Coming soon until the game is actually available, then add the verified App Store link and remove the launch-status wording.
- The support/privacy pages introduce no web trackers, forms, external fonts or embedded third-party content. The approved game icon is copied unchanged. No new game screenshots are claimed.

## Validation

Run `python3 scripts/build-site.py` then `python3 scripts/check-site.py`. New routes participate in metadata, local-resource, anchor, sitemap and theme-scope checks. Theme 1 snapshots and CSS remain frozen. Browser QA belongs under `output/playwright/`.

Verified locally on 28 October: 93 HTML pages and 3,365 local links/assets; 24 browser route/viewport combinations at 320, 390 and 1440 px with no horizontal overflow or missing images; keyboard skip link and mobile menu; support/privacy navigation and privacy-choice anchor; reduced-motion behavior; policy text contrast at least 4.5:1. Marketing desktop/mobile and support mobile captures were visually reviewed. Captures are in `output/playwright/siu-mai-*.png` (ignored).
