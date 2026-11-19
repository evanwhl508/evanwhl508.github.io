# Bone Sweet Bone release pages

## Current listing — 19 November 2026

Version 1.0 is live on the [App Store](https://apps.apple.com/app/id6830231241),
verified using Apple’s public lookup. Added the official store icon and product
card to the default/theme 2 homepage, a download link to the existing product
page, and an entry in the shared support directory. The planned 1.0.1 rewarded
ads notice and privacy policy are retained; 1.0.1 is still awaiting review.
Theme 1 is unchanged.

Validation: site generator and checker pass (105 pages, 3,703 local links/assets).
Desktop 1440px and mobile 390px browser checks pass: official icon loaded, no
horizontal overflow, visible keyboard focus, keyboard Details navigation and
reduced-motion mode. Screenshots inspected under `output/playwright/`.

## Historical preparation

Prepared 4 November 2026 on the current production branch base. Product routes:

- Marketing: https://covanlabs.com/products/bone-sweet-bone/
- Support: https://covanlabs.com/products/bone-sweet-bone/support/
- Privacy: https://covanlabs.com/products/bone-sweet-bone/privacy/
- Public email: support@covanlabs.com (existing studio identity; mailbox delivery still requires owner confirmation).

Facts checked against necromancer-game commit 4f2f85e: four chapters / 32 stages; en, zh-Hant, zh-Hans; device-local save; DevelopmentTelemetryProvider with an in-memory queue, no remote telemetry; Packages/manifest.json excludes ad/IAP SDKs; UnityConnectSettings disables analytics, ads, purchasing and crash reporting. Paid/rewarded entry points remain disabled Coming Soon. Apple platform diagnostics are distinct from app collection.

Privacy copy requires owner review before publication. Do not silently merge or publish this policy, change DNS/mail, or imply physical-device acceptance. Store URLs should be entered only after publication and HTTP verification. No App Store release link until available. Existing theme 1 sources and styles are preserved.

Validation: python3 scripts/build-site.py; python3 scripts/check-site.py; git diff --check. Uses existing theme 2 document components, no new JavaScript, CSS or trackers.
