# Evan Wong Developer Site

Developer website, app support pages, policy documents, and `app-ads.txt` hosting for products built by Evan Wong.

## Live URL

https://page.clearcanvas.app/

## Purpose

This site is used as the public developer website for store listings and ad-network verification.

It provides:

- A personal developer landing page for Evan Wong
- MJ Actuary product/support information
- ClearCanvas product link
- App Store link
- Privacy Policy and Terms of Service
- Root-level `app-ads.txt` for AdMob verification
- Support contact: `evanwhl508+mjactuary@gmail.com`

## Structure

```text
index.html                  # Developer landing page
CNAME                       # GitHub Pages custom domain
app-ads.txt                 # Authorized sellers for app ads
assets/
  mj-actuary-icon.png       # Resized MJ Actuary app icon
mj-actuary/
  privacy.html              # MJ Actuary privacy policy
  terms.html                # MJ Actuary terms of service
```

## AdMob Checklist

Use the site root in App Store Connect and AdMob:

```text
https://page.clearcanvas.app/
```

AdMob should crawl the root app-ads.txt file:

```text
https://page.clearcanvas.app/app-ads.txt
```

Current app-ads.txt content:

```text
google.com, pub-5494888077462930, DIRECT, f08c47fec0942fa0
```
