#!/usr/bin/env python3
"""Generate static theme routes. Standard library only; no browser-side theme detection."""
from pathlib import Path
import re
from logo_component import logo

ROOT = Path(__file__).resolve().parents[1]
SITE_HOST = (ROOT / 'CNAME').read_text().strip()
assert re.fullmatch(r'[A-Za-z0-9.-]+', SITE_HOST), 'CNAME must contain one hostname'
ORIGIN = 'https://' + SITE_HOST
SOURCE = ROOT / 'site'
ROUTES = sorted(p.relative_to(SOURCE / 'theme1').as_posix() for p in (SOURCE / 'theme1').rglob('*.html'))
ARROW = '<svg class="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>'


def write(path, text):
    dest = ROOT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    text = re.sub(r'https://(?:covanlabs\.com|page\.clearcanvas\.app)(?=[/\"\s<]|$)', ORIGIN, text)
    text = text.replace('{{site_host}}', SITE_HOST).replace('website at covanlabs.com', 'website at ' + SITE_HOST)
    text = re.sub(r"[ \t]+(?=\n)", "", text)
    dest.write_text(text)


def scoped_links(html, prefix):
    """Scope only studio navigation, never assets, mail, external URLs or product sites."""
    paths = {'/' + p.removesuffix('index.html') for p in ROUTES} | {'/brand/'}
    def scope(match):
        href = match[1]
        path, _, fragment = href.partition('#')
        if path in paths:
            href = prefix + path + ('#' + fragment if fragment else '')
        return 'href="' + href + '"'
    return re.sub(r'href="([^\"]*)"', scope, html)


def shell(route):
    original = (SOURCE / 'theme1' / ('index.html' if route == 'brand/index.html' else route)).read_text()
    head = re.search(r'<head>([\s\S]*?)</head>', original)[1]
    head = head.replace('/assets/site.css', '/assets/theme2.css')
    head = head.replace('#101c1d', '#08111F')
    head = head.replace('/assets/covan-mark.svg', '/public/brand/favicon/favicon.svg')
    head = head.replace('/assets/apple-touch-icon.png', '/public/brand/favicon/apple-touch-icon.png')
    head = head.replace('/assets/social-card.png', '/public/brand/social/covan-og-brand.png')
    head = head.replace('Focused software for everyday problems.', 'Building useful software, one product at a time.')
    if route == 'index.html':
        head = head.replace('Covan Labs is an independent software studio in Hong Kong, building apps, games, web tools and AI-powered products.', 'Covan Labs is an independent software lab in Hong Kong, creating apps, developer tools, AI products and experiments.')
    head = re.sub(r'(<meta property="og:image:alt" content=")[^"]*', r'\1Covan Labs — Confluence C and studio wordmark', head)
    head += '\n  <meta name="twitter:image:alt" content="Covan Labs — Confluence C and studio wordmark">\n'
    head += '\n  <link rel="preload" href="/assets/fonts/InterVariable.woff2" as="font" type="font/woff2" crossorigin>\n  <script src="/assets/navigation.js" defer></script>\n'
    head += '\n  <link rel="icon" href="/public/brand/favicon/favicon-32.png" sizes="32x32" type="image/png">\n  <link rel="icon" href="/public/brand/favicon/favicon-16.png" sizes="16x16" type="image/png">\n  <link rel="manifest" href="/public/brand/site.webmanifest">\n'
    head = head.replace('"logo": "https://covanlabs.com/public/brand/favicon/apple-touch-icon.png"', '"logo": "https://covanlabs.com/public/brand/social/covan-avatar-512.png"')
    if route == 'brand/index.html':
        head = re.sub(r'<title>.*?</title>', '<title>Brand reference — Covan Labs</title>', head)
        head = head.replace('href="https://covanlabs.com/"', 'href="https://covanlabs.com/brand/"')
        head = head.replace('property="og:url" content="https://covanlabs.com/"', 'property="og:url" content="https://covanlabs.com/brand/"')
        head = re.sub(r'(<meta (?:name|property)="(?:description|og:description|twitter:description)" content=")[^"]*', r'\1Official Covan Labs logo assets, colors and usage guidelines.', head)
        head = re.sub(r'(<meta (?:name|property)="(?:og:title|twitter:title)" content=")[^"]*', r'\1Brand reference — Covan Labs', head)
    nav = '<a href="/#products">Products</a><a href="/#about">About</a><a href="/#contact">Contact</a>'
    header = f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="topbar page">
  <a class="brand" href="/" aria-label="Covan Labs home"><picture><source media="(max-width: 359px)" srcset="/public/brand/micro/covan-mark-micro-primary.svg">{logo(size='md')}</picture></a>
  <nav class="desktop-nav" aria-label="Primary navigation">{nav}</nav>
  <details class="mobile-nav"><summary>Menu <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M3 5h10M3 11h10"/></svg></summary><nav aria-label="Mobile navigation">{nav}</nav></details>
</header>'''
    footer = re.search(r'<footer[\s\S]*?</footer>', original)[0]
    footer = footer.replace('<p>', '<p>' + logo('white', 'mark', 'sm', decorative=True) + ' ', 1)
    footer = footer.replace('<a href="/privacy/">', '<a href="/brand/">Brand</a><a href="/privacy/">')
    body = (SOURCE / 'theme2/home.html' if route == 'index.html' else SOURCE / 'pages' / route).read_text().replace('{{arrow}}', ARROW)
    cls = 'home' if route == 'index.html' else 'document'
    return f'<!DOCTYPE html>\n<html lang="en" data-theme="theme2">\n<head>{head}</head>\n<body>\n{header}\n<main id="main" class="page {cls}">\n{body}</main>\n{footer}\n</body>\n</html>\n'


def main():
    for route in ROUTES:
        original = (SOURCE / 'theme1' / route).read_text()
        original = original.replace('<html lang="en">', '<html lang="en" data-theme="theme1">')
        # Root routes are canonical; explicit theme routes are preview alternatives.
        if 'name="robots"' not in original:
            original = original.replace('</head>', '  <meta name="robots" content="noindex, follow">\n</head>')
        write('theme1/' + route, scoped_links(original, '/theme1'))
        current = shell(route)
        write(route, current)
        if 'name="robots"' not in current:
            current = current.replace('</head>', '  <meta name="robots" content="noindex, follow">\n</head>')
        write('theme2/' + route, scoped_links(current, '/theme2'))
    brand = shell('brand/index.html')
    write('brand/index.html', brand)
    write('theme2/brand/index.html', scoped_links(brand.replace('</head>', '<meta name="robots" content="noindex, follow">\n</head>'), '/theme2'))
    # Legacy product policy URLs and crawler metadata share the publication origin.
    for legacy in ('mj-actuary/privacy.html', 'mj-actuary/terms.html'):
        write(legacy, (ROOT / legacy).read_text())
    write('robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {ORIGIN}/sitemap.xml\n')
    sitemap_paths = ['/' + r.removesuffix('index.html') for r in ROUTES if r != '404.html']
    sitemap_paths += ['/brand/', '/brewpoo/', '/brewpoo/privacy.html', '/brewpoo/support.html', '/mahjong4w/', '/mahjong4w/privacy.html']
    urls = ''.join(f'  <url><loc>{ORIGIN}{path}</loc></url>\n' for path in sorted(set(sitemap_paths)))
    write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n')
    # Preserve the original CSS byte-for-byte for theme 1.
    (ROOT / 'assets/site.css').write_bytes((SOURCE / 'theme1/site.css').read_bytes())
    print(f'Built {len(ROUTES)} pages in each of /, /theme1/ and /theme2/.')


if __name__ == '__main__':
    main()
