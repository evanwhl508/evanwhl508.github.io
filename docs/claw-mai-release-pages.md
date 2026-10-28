# Claw Mai — App Store website handoff

Prepared 29 October 2026 on `release/covan-labs-2026-10-29`. These are repository changes, not a deployment or an App Store submission. Follow the existing owner-controlled website release workflow.

## URLs after deployment

| App Store Connect field | URL |
| --- | --- |
| Marketing URL | https://page.clearcanvas.app/products/claw-mai/ |
| Support URL | https://page.clearcanvas.app/products/claw-mai/support/ |
| Privacy Policy URL | https://page.clearcanvas.app/products/claw-mai/privacy/ |
| User Privacy Choices URL (optional) | https://page.clearcanvas.app/products/claw-mai/privacy/#choices |

The current publication origin comes from `CNAME`: `page.clearcanvas.app`. Domain migration to `covanlabs.com` is separate. Both root and `/theme2/` routes are generated; the root URLs above are canonical. Theme 1 remains frozen. English pages include Traditional Chinese marketing/help sections and a privacy summary. Public contact: `support@covanlabs.com`.

## Product and privacy evidence

Reviewed the current `../claw-mai` source and release configuration for TestFlight 0.7.2 (5):

- `MachineCatalog.cs`: eight characters, 16 full/head dolls, five themes. `ThemeProgression.cs`: free quest-based unlocks and rotating showcase. No D&D branding is used.
- `Economy.cs` and `FreeCoins.cs`: first three attempts free; one coin per subsequent round; ten-minute coin regeneration below 20; two-minute Shake regeneration up to three; daily +3 claim at the UTC reset. Earned currency can exceed the regeneration threshold.
- `SaveStore.cs`, `ClawGame.cs` and `GoalsAndMetrics.cs`: local save, backup fallback, preferences and local play statistics; no account or cloud-save backend. Local metrics are not uploaded analytics.
- `ClawTuning.asset`: `monetizationComingSoon=true`, `rewardedCoinOffer=false`. `RewardedAds.Start()` exits before connecting the ad/consent client when disabled. Google Mobile Ads and consent libraries remain in the binary but are inactive. No Firebase analytics from the separate Roach Rumble project is attributed to this game.
- `ProjectSettings/UnityConnectSettings.asset`: Unity analytics, engine diagnostics, cloud crash reporting, purchasing and Unity Ads are disabled.
- The archived app's `UIDeviceFamily` contains 1 and 2 (iPhone and iPad). The existing approved `Assets/Art/AppIcon.png` is copied unchanged to `assets/claw-mai-icon.png`.

The policy separates on-device records, voluntarily emailed support information, Apple-provided feedback/diagnostics and website-host handling. It does not make an App Store privacy-label submission or certify a future ad-enabled build.

Official sources checked: [Apple app privacy details](https://developer.apple.com/app-store/app-privacy-details/), [Apple app deletion/offloading](https://support.apple.com/en-ca/108429), [Apple privacy policy](https://www.apple.com/legal/privacy/), [GitHub Pages visitor IP logging](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).

## Before the App Store release

- Deploy through the approved site release process and verify all three root URLs over HTTPS without authentication. Test support email delivery and replies separately.
- Confirm the final release binary still matches this policy and enter the corresponding App Privacy answers in App Store Connect. Update the policy and required consent flow before enabling ads, purchases or analytics.
- Add accessible support/privacy links inside the game if not already present; website changes do not modify the game UI.
- Keep “Coming soon” until public availability is confirmed, then add the verified App Store download link and update the status wording.
- No DNS, email routing, `app-ads.txt`, store metadata, production publishing or unrelated product content was changed.

## Validation

Build with `python3 scripts/build-site.py`, then run `python3 scripts/check-site.py`. Browser QA output is under `output/playwright/claw-*.png` (ignored).

Validated locally: 99 HTML pages and 3,537 local links/assets; 30 browser route/viewport combinations at 320, 390 and 1440 px. No horizontal overflow, missing images or browser errors. Keyboard skip link, mobile menu, help/privacy navigation, mailto subject and Chinese-help anchor passed. Reduced motion passed; sampled body text/link contrast ratios were 8.26:1 and 9.08:1. Desktop/mobile marketing and mobile support/privacy captures were visually reviewed. Theme 1 preservation checks passed.
