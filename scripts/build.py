"""Render both languages into static HTML. No third-party dependencies."""
from pathlib import Path
from html import escape
from urllib.parse import urlsplit, unquote
from html.parser import HTMLParser
import argparse
import json

ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://oscartired.github.io/SpiritByte-Terms/'
ARROW = '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>'

def language_links(language, filename):
    links = []
    for lang, label in [('es', 'Español'), ('en', 'English')]:
        target = filename if language == lang else ('en/' if language == 'es' else '../') + filename
        current = ' aria-current="true"' if language == lang else ''
        links.append(f'<a data-language="{lang}" href="{target}" lang="{lang}" hreflang="{lang}"{current}>{label}</a>')
    return ''.join(links)

def page(data, filename, content, title, description):
    language = data['lang']
    prefix = '' if language == 'es' else '../'
    canonical = BASE + ('' if language == 'es' else 'en/') + filename
    def nav(label, target):
        current = ' aria-current="page"' if filename == target else ''
        return f'<a href="{target}"{current}>{escape(label)}</a>'
    return f'''<!doctype html>
<html lang="{language}" data-theme="amber">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="dark">
  <meta name="theme-color" content="#0d0c0a">
  <meta name="description" content="{escape(description, quote=True)}">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <title>{escape(title)} · SpiritByte</title>
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="es" href="{BASE}{filename}">
  <link rel="alternate" hreflang="en" href="{BASE}en/{filename}">
  <link rel="alternate" hreflang="x-default" href="{BASE}{filename}">
  <link rel="icon" type="image/png" href="{prefix}assets/fox.png">
  <link rel="preload" href="{prefix}assets/geist-pixel-square.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{prefix}styles.css">
  <script src="{prefix}site.js" defer></script>
</head>
<body>
  <a class="skip" href="#contenido">{escape(data['skip'])}</a>
  <div class="shell">
    <header class="site-header">
      <a class="brand" href="index.html" aria-label="{escape(data['home_label'], quote=True)}"><img src="{prefix}assets/fox.png" alt="" width="46" height="46"><span>SPIRITBYTE<small>LOCAL / PRIVATE / YOURS</small></span></a>
      <div class="header-tools">
        <nav aria-label="{escape(data['nav_label'], quote=True)}">{nav(data['nav_privacy'], 'privacy.html')}{nav(data['nav_terms'], 'terms.html')}<a href="mailto:oscar@octa-dev.com">{escape(data['nav_contact'])}</a></nav>
        <nav class="language-switch" aria-label="{escape(data['language_label'], quote=True)}">{language_links(language, filename)}</nav>
      </div>
    </header>
    {content}
    <footer class="site-footer">
      <div><a class="footer-brand" href="index.html">SPIRITBYTE</a><p>{escape(data['footer_note'])}</p></div>
      <div><p>{escape(data['developer'])}</p><a href="mailto:oscar@octa-dev.com">oscar@octa-dev.com</a></div>
      <div class="footer-links"><a href="privacy.html">{escape(data['privacy']['title'])}</a><a href="terms.html">{escape(data['terms']['title'])}</a><span>© 2026 Octa_Dev</span></div>
    </footer>
  </div>
</body>
</html>
'''

def home(data):
    h = data['home']
    prefix = '' if data['lang'] == 'es' else '../'
    return f'''<main id="contenido" tabindex="-1">
  <section class="hero" aria-labelledby="home-title">
    <div class="hero-copy"><h1 id="home-title">{escape(h['heading'])}<br><span>{escape(h['heading_second'])}</span></h1><p class="lead">{h['lead']}</p><a class="button" href="privacy.html">{escape(h['action'])} {ARROW}</a><p class="hero-note"><span class="status-dot" aria-hidden="true"></span>{escape(h['note'])}</p></div>
    <div class="fox-panel" aria-hidden="true"><div class="fox-corner top-left"></div><div class="fox-corner top-right"></div><img src="{prefix}assets/fox.png" alt="" width="340" height="340"><p>LOCAL / PRIVATE / YOURS</p><div class="fox-corner bottom-left"></div><div class="fox-corner bottom-right"></div></div>
  </section>
  <section class="reading-room" aria-labelledby="documents-title"><div class="section-intro"><h2 id="documents-title">{escape(h['documents_heading'])}</h2><p>{escape(h['documents_intro'])}</p></div>
    <a class="document-link" href="privacy.html"><div><h3>{escape(h['privacy_title'])}</h3><p>{escape(h['privacy_intro'])}</p></div><span class="document-action">{escape(h['read'])} {ARROW}</span></a>
    <a class="document-link" href="terms.html"><div><h3>{escape(h['terms_title'])}</h3><p>{escape(h['terms_intro'])}</p></div><span class="document-action">{escape(h['read'])} {ARROW}</span></a>
  </section>
  <section class="local-note"><h2>{escape(h['local_heading'])}</h2><p>{escape(h['local_body'])}</p><a href="privacy.html#respaldos">{escape(h['backup_link'])} {ARROW}</a></section>
  <section class="contact-strip"><div><h2>{escape(h['contact_heading'])}</h2><p>{escape(h['contact_intro'])}</p></div><a href="mailto:oscar@octa-dev.com">oscar@octa-dev.com {ARROW}</a></section>
</main>'''

def document(data, key):
    doc = data[key]
    prefix = '' if data['lang'] == 'es' else '../'
    contents = ''.join(f'<li><a href="#{section["id"]}">{escape(section["heading"])}</a></li>' for section in doc['sections'])
    sections = []
    for section in doc['sections']:
        html = section['html'].replace('href="assets/', f'href="{prefix}assets/')
        sections.append(f'<section id="{section["id"]}" class="legal-section"><h2>{escape(section["heading"])}</h2>{html}</section>')
    body = ''.join(sections)
    return f'''<main id="contenido" tabindex="-1"><div class="document-heading"><a class="back-link" href="index.html">{escape(data['back'])}</a><h1>{escape(doc['heading'])}</h1><p class="lead">{escape(doc['intro'])}</p><div class="document-meta"><span>SpiritByte Android · Octa_Dev</span><span>{escape(data['updated'])} <time datetime="2026-10-13">{escape(data['date'])}</time></span><button class="text-button" type="button" data-print hidden>{escape(data['print'])}</button></div></div><div class="document-layout"><aside class="contents"><nav aria-label="{escape(data['contents'], quote=True)}"><h2>{escape(data['contents'])}</h2><ul>{contents}</ul></nav></aside><article class="legal-body" aria-label="{escape(doc['title'], quote=True)}"><div class="summary"><h2>{escape(data['summary_heading'])}</h2><p>{escape(doc['summary'])}</p></div>{body}<a class="back-top" href="#contenido">{escape(data['top'])}</a></article></div></main>'''

class HTMLReferences(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.refs = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            if attrs['id'] in self.ids: raise ValueError(f'Duplicate ID: {attrs["id"]}')
            self.ids.add(attrs['id'])
        if 'href' in attrs: self.refs.append(attrs['href'])
        if 'src' in attrs: self.refs.append(attrs['src'])

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Verify that committed HTML matches the sources and all local links resolve.')
    check = parser.parse_args().check
    languages = {lang: json.loads((ROOT / 'content' / f'{lang}.json').read_text(encoding='utf-8')) for lang in ['es', 'en']}
    for key in ['privacy', 'terms']:
        expected_ids = [s['id'] for s in languages['es'][key]['sections']]
        if expected_ids != [s['id'] for s in languages['en'][key]['sections']]:
            raise ValueError(f'The {key} sections must match between languages.')
    output = {}
    for language, data in languages.items():
        if data['lang'] != language: raise ValueError('Incorrect content language.')
        directory = ROOT if language == 'es' else ROOT / 'en'
        output[directory / 'index.html'] = page(data, 'index.html', home(data), data['home']['title'], data['home']['description'])
        for key in ['privacy', 'terms']:
            filename = key + '.html'
            output[directory / filename] = page(data, filename, document(data, key), data[key]['title'], data[key]['description'])
    parsed = {}
    for path, text in output.items():
        refs = HTMLReferences()
        refs.feed(text)
        parsed[path] = refs
    checked_links = 0
    for path, refs in parsed.items():
        for ref in refs.refs:
            url = urlsplit(ref)
            if url.scheme or url.netloc: continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not target.is_relative_to(ROOT): raise ValueError(f'Link outside site: {ref}')
            if target not in output and not target.is_file(): raise ValueError(f'Missing link: {ref}')
            if url.fragment and (target not in parsed or url.fragment not in parsed[target].ids):
                raise ValueError(f'Missing anchor: {ref}')
            checked_links += 1
        if check:
            if not path.is_file() or path.read_text(encoding='utf-8') != output[path]:
                raise ValueError(f'Outdated HTML: {path.relative_to(ROOT)}. Run python scripts/build.py.')
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(output[path], encoding='utf-8')
    print(f'{"Verified" if check else "Built"} {len(output)} bilingual pages and {checked_links} local links/anchors.')

if __name__ == '__main__':
    main()
