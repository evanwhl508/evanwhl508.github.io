#!/usr/bin/env python3
"""Check static theme routing, preservation, metadata and internal resources."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.links, self.navigation, self.ids, self.meta = [], [], [], {}
        self.h1 = 0
        self.canonical = None
        self.theme = None
        self.feed(path.read_text())

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'html':
            self.theme = attrs.get('data-theme')
        if tag == 'h1':
            self.h1 += 1
        if tag == 'meta':
            self.meta[attrs.get('name', attrs.get('property'))] = attrs.get('content')
        if tag == 'a':
            self.navigation.append(attrs.get('href', ''))
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs['href']
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])


def main():
    pages = {p: Page(p) for p in ROOT.rglob('*.html')
             if not set(p.relative_to(ROOT).parts) & {'site', 'output', '.git', '.playwright-cli'}}
    count = 0
    for path, page in pages.items():
        assert len(page.ids) == len(set(page.ids)), f'Duplicate IDs: {path}'
        if page.theme:
            assert page.h1 == 1, f'Expected one h1: {path}'
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            target = ((ROOT / url.path.lstrip('/')) if url.path.startswith('/') else path.parent / url.path).resolve() if url.path else path
            if target.is_dir():
                target /= 'index.html'
            assert target.exists(), f'Broken link in {path}: {link}'
            if url.fragment and target in pages:
                assert unquote(url.fragment) in pages[target].ids, f'Missing anchor: {path}: {link}'
            count += 1
        if page.theme:
            assert page.canonical and '/theme' not in urlsplit(page.canonical).path, path
            for name in ('description', 'og:title', 'og:description', 'og:image', 'twitter:card'):
                assert page.meta.get(name), f'Missing {name}: {path}'
            asset = ROOT / urlsplit(page.meta['og:image']).path.lstrip('/')
            assert asset.is_file(), asset
            prefix = path.relative_to(ROOT).parts[0]
            if prefix in {'theme1', 'theme2'}:
                assert page.theme == prefix and 'noindex' in page.meta['robots'], path
                for link in page.navigation:
                    if link.startswith(('/#', '/privacy/', '/terms/', '/support/', '/products/')) or link == '/':
                        raise AssertionError(f'Theme escaped: {path}: {link}')
            else:
                assert page.theme == 'theme2', path
    # Verify preservation against the before-change source snapshot.
    manifest = json.loads((ROOT/'site/theme1/manifest.json').read_text())
    for route, digest in manifest.items():
        snapshot = ROOT/'site/theme1'/route
        assert hashlib.sha256(snapshot.read_bytes()).hexdigest() == digest, f'Theme 1 snapshot changed: {route}'
    assert (ROOT/'assets/site.css').read_bytes() == (ROOT/'site/theme1/site.css').read_bytes()
    # Every source studio page must exist in all route families.
    for route in manifest:
        for prefix in ('', 'theme1/', 'theme2/'):
            assert (ROOT/(prefix+route)).is_file(), prefix+route
    # New current-design routes must be generated with distinct metadata and sitemap entries.
    new_pages = json.loads((ROOT/'site/pages/routes.json').read_text())
    sitemap_urls = {item[0].text for item in ET.parse(ROOT/'sitemap.xml').getroot()}
    for route in new_pages:
        for prefix in ('', 'theme2/'):
            path = ROOT/(prefix+route)
            assert path in pages, f'Missing new product route: {path}'
            page = pages[path]
            expected = 'https://' + (ROOT/'CNAME').read_text().strip() + '/' + route.removesuffix('index.html')
            assert page.canonical == expected and expected in sitemap_urls, path
            assert page.meta['og:title'] == new_pages[route]['title'], path
            assert page.meta['description'] == new_pages[route]['description'], path
    for item in ET.parse(ROOT/'sitemap.xml').getroot():
        path = urlsplit(item[0].text).path
        assert not path.startswith(('/theme1', '/theme2')), path
        target = ROOT / path.lstrip('/')
        assert (target/'index.html' if target.is_dir() else target).is_file(), path
    print(f'PASS: {len(pages)} HTML pages, {count} local links/assets, theme routing and metadata.')
    print('PASS: theme 1 snapshot and CSS preserved; all three route families present.')


if __name__ == '__main__':
    main()
