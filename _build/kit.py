"""Shared layout + components for the Gale AI static site.

Every component returns an HTML string. Plain-text arguments are escaped;
'\n' in text becomes a line break. Image arguments may be Tilda CDN URLs —
img() downloads them once into /assets/img/ and returns the local path.
"""
import hashlib, html, os, pathlib, re, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent          # repo root = site root
IMG_DIR = ROOT / 'assets' / 'img'
CALENDLY = 'https://calendly.com/pkokora/30min-meeting'
EMAIL = 'hello@galeapp.co'
PHONE = '+7 991 937-97-87'
WHATSAPP = 'https://wa.me/79919379787'
TELEGRAM = 'https://t.me/+79919379787'

# ---------------------------------------------------------------- helpers
def esc(s):
    return html.escape(s or '', quote=True)

def txt(s):
    """Escape text, keep line breaks, allow **bold**."""
    s = esc(s).strip()
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    return s.replace('\n', '<br>')

def img(url, alt=''):
    """Return a local /assets/img/... path for a remote image (downloaded once)."""
    if not url or not url.startswith('http'):
        return url
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    name = url.rsplit('/', 1)[-1].split('?')[0]
    ext = pathlib.Path(name).suffix.lower() or '.png'
    if ext not in ('.png', '.jpg', '.jpeg', '.webp', '.svg', '.gif'):
        ext = '.png'
    h = hashlib.md5(url.encode()).hexdigest()[:10]
    stem = re.sub(r'[^a-z0-9]+', '-', pathlib.Path(name).stem.lower()).strip('-')[:28] or 'img'
    local = IMG_DIR / f'{stem}-{h}{ext}'
    if not local.exists():
        req = urllib.request.Request(url.replace('static.tildacdn.info', 'static.tildacdn.com'),
                                     headers={'User-Agent': 'Mozilla/5.0'})
        try:
            data = urllib.request.urlopen(req, timeout=30).read()
        except Exception:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            data = urllib.request.urlopen(req, timeout=30).read()
        local.write_bytes(data)
    return '/assets/img/' + local.name

ICONS = {
    'check': '<path d="M20 6 9 17l-5-5"/>',
    'chart': '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/>',
    'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    'users': '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9"/><path d="M16 3.1a4 4 0 0 1 0 7.8"/>',
    'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    'spark': '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M5.6 18.4l2.8-2.8M15.6 8.4l2.8-2.8"/>',
    'phone': '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    'money': '<rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="2.5"/><path d="M6 12h.01M18 12h.01"/>',
    'link': '<path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/>',
    'target': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
    'book': '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M4 19.5V21h16"/>',
    'search': '<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>',
    'heart': '<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21l8.8-8.6a5.5 5.5 0 0 0 0-7.8z"/>',
    'doc': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h6"/>',
    'mic': '<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 10a7 7 0 0 0 14 0M12 17v5"/>',
    'trend': '<path d="m22 7-8.5 8.5-5-5L2 17"/><path d="M16 7h6v6"/>',
    'chat': '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    'building': '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M16 6h.01M12 6h.01M12 10h.01M12 14h.01M16 10h.01M16 14h.01M8 10h.01M8 14h.01"/>',
    'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>',
    'menu': '<path d="M4 6h16M4 12h16M4 18h16"/>',
}

def icon(name, size=24):
    p = ICONS.get(name, ICONS['check'])
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>')

# ---------------------------------------------------------------- i18n chrome
STR = {
    'ru': dict(demo='Забронировать демо', menu='Меню', home='/',
               nav=[('Платформа', '/#gale-platform'), ('Кейсы', '/cases/'), ('Колл-центр', '/ru/callcenter/'),
                    ('Партнёрам', '/partners/ru/'), ('Блог', '/blogru/')],
               foot=[('О продукте', '/'), ('Кейсы', '/cases/'), ('Партнёрская программа', '/partners/ru/'),
                     ('Блог', '/blogru/'), ('Политика обработки персональных данных', '/privacy/')],
               copy='© 2024 Gale AI (ИП Кокора Павел Евгеньевич)', skip='Перейти к содержанию'),
    'en': dict(demo='Book a demo', menu='Menu', home='/en/',
               nav=[('Platform', '/en/#gale-platform'), ('Contact center', '/en/contact-center/'),
                    ('Case studies', '/cases/'), ('Partners', '/partners/en/'), ('Blog', '/blogen/')],
               foot=[('About the product', '/en/'), ('Partner program', '/partners/en/'), ('Blog', '/blogen/'),
                     ('Privacy policy', '/privacy/')],
               copy='© 2024 Gale AI', skip='Skip to content'),
    'vn': dict(demo='Đặt lịch demo', menu='Menu', home='/vn/',
               nav=[('Nền tảng', '/vn/#platform'), ('Đối tác', '/partners/vn/'), ('Blog (EN)', '/blogen/')],
               foot=[('Về sản phẩm', '/vn/'), ('Chương trình đối tác', '/partners/vn/'), ('Chính sách bảo mật', '/privacy/')],
               copy='© 2024 Gale AI', skip='Chuyển đến nội dung'),
}
LANGS = ('ru', 'en')          # VN version removed
LANG_HOME = {'ru': '/', 'en': '/en/', 'vn': '/vn/'}
HTML_LANG = {'ru': 'ru', 'en': 'en', 'vn': 'vi'}

def header(lang, path, alts):
    s = STR[lang]
    cur_page = ' aria-current="page"'
    cur_lang = ' aria-current="true"'
    nav = ''.join(
        f'<a href="{h}"{cur_page if h.rstrip("/") == path.rstrip("/") else ""}>{esc(l)}</a>'
        for l, h in s['nav'])
    sw = ''.join(
        f'<a href="{esc(alts.get(k, LANG_HOME[k]))}" hreflang="{HTML_LANG[k]}"'
        f'{cur_lang if k == lang else ""}>{k.upper()}</a>' for k in LANGS)
    return f'''<a class="skip" href="#main">{esc(s['skip'])}</a>
<header class="hdr" id="hdr"><div class="wrap">
<a class="brand" href="{s['home']}"><span class="brand-mark"><img src="/assets/img/logo.png" alt=""></span><span class="brand-name">Gale AI</span></a>
<nav class="nav" aria-label="Main">{nav}</nav>
<div class="hdr-right"><div class="lang" aria-label="Language">{sw}</div>
<a class="btn btn-dark btn-sm btn-demo" href="{CALENDLY}" target="_blank" rel="noopener">{esc(s['demo'])}</a>
<button class="menu-btn" type="button" aria-label="{esc(s['menu'])}" aria-expanded="false" onclick="var h=document.getElementById('hdr');var o=h.classList.toggle('open');this.setAttribute('aria-expanded',o)">{icon('menu')}</button></div>
</div></header>'''

def footer(lang):
    s = STR[lang]
    links = ''.join(f'<a href="{h}">{esc(l)}</a>' for l, h in s['foot'])
    return f'''<footer class="ftr"><div class="wrap">
<span class="brand"><span class="brand-mark"><img src="/assets/img/logo.png" alt="Gale AI"></span><span>{esc(s['copy'])}</span></span>
<nav aria-label="Footer">{links}</nav>
</div></footer>'''

def page(*, lang, path, title, description='', body, alts=None, extra_head=''):
    alts = {k: v for k, v in (alts or {}).items() if k in LANGS}
    alt_links = ''.join(f'<link rel="alternate" hreflang="{HTML_LANG[k]}" href="{v}">' for k, v in alts.items())
    return f'''<!doctype html>
<html lang="{HTML_LANG[lang]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="website">
<meta property="og:image" content="/assets/img/og.png">
<link rel="icon" href="/assets/img/logo.png">
{alt_links}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Onest:wght@500;600;700&display=swap">
<link rel="stylesheet" href="/assets/site.css">
{extra_head}
</head>
<body>
{header(lang, path, alts)}
<main id="main">
{body}
</main>
{footer(lang)}
</body>
</html>
'''

BASE = os.environ.get('GALE_BASE', '').rstrip('/')   # e.g. '/galeai' when served from user.github.io/galeai/


def with_base(html_text):
    """Prefix root-relative links (/x) with BASE so the site works from a sub-path."""
    if not BASE:
        return html_text
    html_text = re.sub(r'((?:href|src|content)=")/(?!/)', rf'\g<1>{BASE}/', html_text)
    return re.sub(r'(url=)/(?!/)', rf'\g<1>{BASE}/', html_text)


def write(path, html_text):
    html_text = with_base(html_text)
    out =ROOT / path.strip('/') / 'index.html' if not path.endswith('.html') else ROOT / path.strip('/')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html_text, 'utf-8')
    return out

def redirect(old, new):
    write(old, f'<!doctype html><html><head><meta charset="utf-8"><title>Gale AI</title>'
               f'<link rel="canonical" href="{new}"><meta http-equiv="refresh" content="0; url={new}">'
               f'</head><body><a href="{new}">{new}</a></body></html>')

# ---------------------------------------------------------------- components
def btn(label, href, kind='primary', size=''):
    ext = href.startswith('http')
    t = ' target="_blank" rel="noopener"' if ext else ''
    return f'<a class="btn btn-{kind} {size}" href="{esc(href)}"{t}>{esc(label)}</a>'

def btns(*items):
    """items: (label, href[, kind])"""
    return '<div class="btns">' + ''.join(btn(*i) for i in items) + '</div>'

def section(body, title=None, kicker=None, lead=None, tone='', id=None, tight=False):
    """tone: '' (grey page bg), 'white', 'dark'."""
    cls = 'sec' + (f' sec-{tone}' if tone else '') + (' sec-tight' if tight else '')
    head = ''
    if title or kicker or lead:
        head = '<div class="sec-head">'
        if kicker: head += f'<span class="kicker">{txt(kicker)}</span>'
        if title: head += f'<h2 class="h2">{txt(title)}</h2>'
        if lead: head += f'<p class="lead">{txt(lead)}</p>'
        head += '</div>'
    i = f' id="{id}"' if id else ''
    return f'<section class="{cls}"{i}><div class="wrap stack-lg">{head}{body}</div></section>'

def hero(title, text=None, kicker=None, bullets=None, buttons=None, aside=None, tags=None, h1_accent=None):
    """aside: raw html or an image URL. h1_accent: substring of title to colour."""
    t = txt(title)
    if h1_accent:
        t = t.replace(esc(h1_accent), f'<span class="accent">{esc(h1_accent)}</span>', 1)
    main = ''
    if kicker: main += f'<span class="kicker">{txt(kicker)}</span>'
    main += f'<h1 class="h1">{t}</h1>'
    if tags: main += '<div class="tags">' + ''.join(f'<span class="tag">{txt(x)}</span>' for x in tags) + '</div>'
    if text: main += f'<p class="lead">{txt(text)}</p>'
    if bullets: main += dots(bullets)
    if buttons: main += btns(*buttons)
    side = ''
    if aside:
        if aside.startswith('http') or aside.startswith('/assets'):
            aside = f'<img src="{img(aside)}" alt="" loading="eager">'
        side = f'<div class="hero-aside">{aside}</div>'
    return f'<section class="hero"><div class="wrap hero-grid"><div class="hero-main">{main}</div>{side}</div></section>'

def dots(items):
    return '<ul class="dots">' + ''.join(f'<li><span>{txt(i)}</span></li>' for i in items) + '</ul>'

def cards(items, min=260):
    """items: dicts with title, text, optional icon, num, bullets, image."""
    out = []
    for it in items:
        c = '<div class="card">'
        if it.get('image'): c += f'<img src="{img(it["image"])}" alt="" loading="lazy" style="border-radius:12px">'
        if it.get('icon'): c += f'<span class="icon">{icon(it["icon"])}</span>'
        if it.get('num'): c += f'<span class="num">{esc(str(it["num"]))}</span>'
        if it.get('title'): c += f'<h3>{txt(it["title"])}</h3>'
        if it.get('text'): c += f'<p>{txt(it["text"])}</p>'
        if it.get('bullets'): c += '<ul>' + ''.join(f'<li>{txt(b)}</li>' for b in it['bullets']) + '</ul>'
        c += '</div>'
        out.append(c)
    return f'<div class="grid" style="--min:{min}px">' + ''.join(out) + '</div>'

def stats(items):
    """items: (value, label)"""
    return '<div class="stats">' + ''.join(
        f'<div class="stat"><b>{txt(v)}</b><span>{txt(l)}</span></div>' for v, l in items) + '</div>'

def steps(items):
    """items: (title, text) — numbered automatically."""
    return '<div class="steps">' + ''.join(
        f'<div class="step"><h3 class="h3" style="font-size:19px">{txt(t)}</h3>' + (f'<p>{txt(x)}</p>' if x else '') + '</div>'
        for t, x in items) + '</div>'

def quote(text, name, role='', link=None, photo=None):
    ph = f'<img src="{img(photo)}" alt="" loading="lazy">' if photo else ''
    r = txt(role)
    if link:
        short = re.sub(r'^https?://(www\.)?', '', link).rstrip('/')
        r = f'{r} · <a href="{esc(link)}" target="_blank" rel="noopener">{esc(short)}</a>'
    return (f'<figure class="quote"><blockquote>{txt(text)}</blockquote>'
            f'<figcaption class="who">{ph}<div><b>{txt(name)}</b><span>{r}</span></div></figcaption></figure>')

def quotes(items, min=340):
    return f'<div class="grid" style="--min:{min}px">' + ''.join(quote(**q) for q in items) + '</div>'

def case_cards(items, more='Смотреть кейс →'):
    """items: dicts value, title, tags, href"""
    return '<div class="grid" style="--min:250px">' + ''.join(
        f'<a class="case" href="{esc(i["href"])}"><b>{txt(i["value"])}</b><span class="t">{txt(i["title"])}</span>'
        f'<span class="tags">' + ''.join(f'<span class="tag">{txt(t)}</span>' for t in i.get('tags', [])) + '</span>'
        f'<span class="more">{esc(more)}</span></a>' for i in items) + '</div>'

def logos(items):
    """items: (image_url, alt)"""
    return '<div class="logos">' + ''.join(
        f'<div><img src="{img(u)}" alt="{esc(a)}" loading="lazy"></div>' for u, a in items) + '</div>'

def shot(url, alt='', caption=None):
    cap = f'<figcaption>{txt(caption)}</figcaption>' if caption else ''
    return f'<figure><div class="shot"><img src="{img(url)}" alt="{esc(alt)}" loading="lazy"></div>{cap}</figure>'

def split(left, right, reverse=False):
    return f'<div class="split{" rev" if reverse else ""}"><div class="stack">{left}</div><div>{right}</div></div>'

def text_block(title=None, text=None, bullets=None, h='h3'):
    o = ''
    if title: o += f'<h3 class="{h}">{txt(title)}</h3>' if h == 'h3' else f'<h2 class="h2">{txt(title)}</h2>'
    if text: o += f'<p class="lead">{txt(text)}</p>'
    if bullets: o += dots(bullets)
    return o

def faq(items):
    """items: (question, answer)"""
    return '<div class="faq">' + ''.join(
        f'<details><summary>{txt(q)}</summary><p>{txt(a)}</p></details>' for q, a in items) + '</div>'

CTA_TEXT = {
    'ru': dict(title='Поставьте рекорды продаж вместе с Gale AI',
               text='Покажем платформу на ваших звонках и запустим бесплатный тест.',
               q='Есть вопросы? С удовольствием ответим!', box='Покажем Gale на ваших звонках',
               box_text='Выберите удобное время в календаре — встреча займёт 30 минут.',
               mail='Написать на почту', wa='Telegram / WhatsApp'),
    'en': dict(title='Set sales records with Gale AI',
               text='We’ll show the platform on your own calls and run a free pilot.',
               q='Questions? We’re happy to help.', box='See Gale on your own calls',
               box_text='Pick a time in the calendar — the call takes 30 minutes.',
               mail='Email us', wa='Telegram / WhatsApp'),
    'vn': dict(title='Lập kỷ lục doanh số cùng Gale AI',
               text='Chúng tôi sẽ trình diễn nền tảng trên chính các cuộc gọi của bạn.',
               q='Bạn có câu hỏi? Chúng tôi luôn sẵn lòng hỗ trợ.', box='Xem Gale hoạt động trên cuộc gọi của bạn',
               box_text='Chọn thời gian phù hợp trong lịch — cuộc gọi kéo dài 30 phút.',
               mail='Gửi email', wa='Telegram / WhatsApp'),
}

def cta(lang, title=None, text=None, primary=None):
    c = CTA_TEXT[lang]
    label, href = primary or (STR[lang]['demo'], CALENDLY)
    return f'''<section class="sec" id="contact"><div class="wrap"><div class="cta">
<div><h2 class="h2">{txt(title or c['title'])}</h2><p>{txt(text or c['text'])}</p>
<div class="contacts"><span>{esc(c['q'])}</span><a href="mailto:{EMAIL}">{EMAIL}</a>
<span>{esc(c['wa'])}: <a href="{WHATSAPP}" target="_blank" rel="noopener">{PHONE}</a></span></div></div>
<div class="cta-box"><p style="font-family:var(--font-head);font-size:22px;font-weight:600;color:var(--ink)">{esc(c['box'])}</p>
<p>{esc(c['box_text'])}</p>{btn(label, href, 'primary')}{btn(c['mail'], 'mailto:' + EMAIL, 'ghost')}</div>
</div></div></section>'''

def prose(blocks, cls=''):
    """blocks: list of ('h2'|'h3'|'p'|'lede'|'img'|'ul', value)."""
    out = []
    for k, v in blocks:
        if k == 'img': out.append(f'<img src="{img(v)}" alt="" loading="lazy">')
        elif k == 'ul': out.append('<ul>' + ''.join(f'<li>{txt(x)}</li>' for x in v) + '</ul>')
        elif k == 'lede': out.append(f'<p class="lede">{txt(v)}</p>')
        elif k == 'html': out.append(v)
        else: out.append(f'<{k}>{txt(v)}</{k}>')
    return f'<div class="prose {cls}">' + ''.join(out) + '</div>'
