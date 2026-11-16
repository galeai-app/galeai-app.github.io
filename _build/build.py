"""Build the Gale AI static site into the repo root.

Run:  python3 _build/build.py
Sources: _build/src (hand-designed landings), _build/data (content pulled from the old Tilda site),
         _build/pages_*.py (hand-written page content).
"""
import base64, hashlib, importlib, json, pathlib, re, sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import kit
from kit import *  # noqa

B = pathlib.Path(__file__).parent
DATA = B / 'data'


def load(name):
    return json.loads((DATA / f'{name}.json').read_text('utf-8'))


# ------------------------------------------------------------------ landings
def save_datauri(m):
    mime, b64 = m.group(1), m.group(2)
    ext = {'image/png': '.png', 'image/jpeg': '.jpg', 'image/webp': '.webp', 'image/svg+xml': '.svg'}.get(mime, '.png')
    raw = base64.b64decode(b64)
    name = 'landing-' + hashlib.md5(raw).hexdigest()[:10] + ext
    kit.IMG_DIR.mkdir(parents=True, exist_ok=True)
    (kit.IMG_DIR / name).write_bytes(raw)
    return '/assets/img/' + name


def landing(lang, path, alts):
    src = (B / 'src' / f'landing-{lang}.html').read_text('utf-8')
    # logo = first image in the landing header
    m = re.search(r'<header.*?src="data:(image/[a-z+]+);base64,([^"]+)"', src, re.S)
    if m and not (kit.IMG_DIR / 'logo.png').exists():
        kit.IMG_DIR.mkdir(parents=True, exist_ok=True)
        (kit.IMG_DIR / 'logo.png').write_bytes(base64.b64decode(m.group(2)))
    src = re.sub(r'<header.*?</header>\s*', '', src, count=1, flags=re.S)
    src = re.sub(r'<footer.*?</footer>\s*', '', src, count=1, flags=re.S)
    src = re.sub(r'data:(image/[a-z+]+);base64,([A-Za-z0-9+/=]+)', save_datauri, src)
    trial = '/freetrial/ru/' if lang == 'ru' else CALENDLY
    src = re.sub(r'href="#popup:myform"([^>]*>)(Протестировать бесплатно|Try it free)',
                 lambda m: f'href="{trial}"{m.group(1)}{m.group(2)}', src)
    src = src.replace('href="#popup:myform"', f'href="{CALENDLY}" target="_blank" rel="noopener"')
    src = src.replace('http://gale.ai.tilda.ws/cases/portalbilet', '/cases/portalbilet/')
    src = src.replace('http://gale.ai.tilda.ws/cases/domgroup', '/cases/domgroup/')
    src = src.replace('http://gale.ai.tilda.ws/cases', '/cases/')
    src = src.replace('Откроется форма заявки — оставьте имя, телефон и Telegram, и мы свяжемся с вами.',
                      'Выберите удобное время в календаре — встреча займёт 30 минут.')
    src = src.replace('A short form will open — leave your name, phone and Telegram, and we’ll get back to you.',
                      'Pick a time in the calendar — the call takes 30 minutes.')
    src = re.sub(r'<span([^>]*)>\+7 991 937-97-87</span>',
                 rf'<a href="{WHATSAPP}" target="_blank" rel="noopener"\1>+7 991 937-97-87</a>', src)
    meta = {
        'ru': ('Gale AI — ИИ-аналитика звонков для отдела продаж и контакт-центра',
               'Gale AI анализирует 100% звонков отдела продаж: показывает, где теряется прибыль, чего хотят клиенты и как повысить эффективность менеджеров.'),
        'en': ('Gale AI — AI call analytics for sales teams and contact centers',
               'Gale AI analyzes 100% of your sales calls and shows where revenue leaks, what customers want and how to make your team more effective.'),
    }[lang]
    write(path, page(lang=lang, path=path, title=meta[0], description=meta[1], body=src, alts=alts))


# ------------------------------------------------------------------ blog
def split_106(text):
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    out = []
    if len(lines) > 1 and len(lines[0]) < 90 and not lines[0].endswith('.'):
        out.append(('h2', lines[0]))
        lines = lines[1:]
    out += [('p', l) for l in lines]
    return out


def article(name):
    d = load(name)
    title, lede, date, blocks = d['meta']['title'], '', '', []
    for b in d['blocks']:
        t, items = b['type'], b['items']
        flat = ' '.join(i[1] for i in items if i[0] != 'img')
        if t == '396' or flat.startswith(('Связаться с нами', 'Contact us', 'Contact')):
            continue
        if t == '255' or t == '18':
            title = items[-1][1]
        elif t == '127':
            lede = items[0][1]
        elif t == '106':
            blocks += split_106(items[0][1])
        elif t == '3':
            blocks.append(('img', items[0][1]))
        elif t == '43':
            for i in items:
                blocks.append(('h2' if i[0] == 'h' else 'p', i[1]))
        elif t == '40':
            date = items[0][1].replace('\n', ' ').replace(' / ', ' ')
    return dict(title=title, lede=lede, date=date, blocks=blocks)


BLOG = {
    'ru': dict(index='/blogru/', title='Блог Gale AI', lead='Интересные статьи про искусственный интеллект от Gale AI',
               crumbs='Блог', read='Читать статью →',
               posts=[('blogru5', '/blogru5/'), ('blogru4', '/blogru4/'), ('blogru3', '/blogru3/'),
                      ('blog2', '/blog2/'), ('blogru1', '/blogru1/')], src='blogru'),
    'en': dict(index='/blogen/', title='Gale AI blog', lead='Articles about artificial intelligence from the Gale AI team',
               crumbs='Blog', read='Read the article →',
               posts=[('page49110001.html', '/blogen/ai-in-finance/'), ('page49107819.html', '/blogen/ai-in-transportation/'),
                      ('page49043229.html', '/blogen/ai-in-education/'), ('page49041315.html', '/blogen/ai-in-medicine/'),
                      ('page49036701.html', '/blogen/ai-empowering-businesses/'),
                      ('page47979465.html', '/blogen/ai-transforming-the-world/')], src='blogen'),
}
# EN ↔ RU counterparts (same topics) for the language switcher
BLOG_PAIRS = {'/blogen/ai-in-finance/': '/blogru5/', '/blogen/ai-in-transportation/': '/blogru4/',
              '/blogen/ai-in-education/': '/blogru3/', '/blogen/ai-in-medicine/': '/blog2/',
              '/blogen/ai-empowering-businesses/': '/blogru1/'}


def blog(lang):
    cfg = BLOG[lang]
    idx = load(cfg['src'])
    listing = [b for b in idx['blocks'] if b['type'] == '404'][0]['items']
    covers, cur = [], {}
    for it in listing:   # img, date, title, [excerpt]
        if it[0] == 'img':
            cur = {'img': it[1]}; covers.append(cur)
        elif it[0] == 'h' and 'date' not in cur:
            cur['date'] = it[1]
        elif it[0] == 'h':
            cur['title'] = it[1]
        elif it[0] == 't':
            cur['excerpt'] = it[1]
    posts = []
    for (name, path), cov in zip(cfg['posts'], covers):
        a = article(name)
        a.update(path=path, cover=cov['img'], excerpt=cov.get('excerpt', a['lede']))
        a['date'] = fmt_date(a['date'] or cov.get('date', ''), lang)
        a['list_date'] = a['date']
        posts.append(a)
    # index
    cards_html = '<div class="grid" style="--min:300px">' + ''.join(
        f'<a class="post" href="{p["path"]}"><img src="{img(p["cover"])}" alt="" loading="lazy">'
        f'<div><time>{esc(p["date"] or p["list_date"])}</time><h3>{esc(p["title"])}</h3>'
        f'<span class="accent" style="font-weight:600;font-size:15px">{esc(cfg["read"])}</span></div></a>'
        for p in posts) + '</div>'
    other = 'en' if lang == 'ru' else 'ru'
    alts = {lang: cfg['index'], other: BLOG[other]['index']}
    body = hero(cfg['title'], cfg['lead'], kicker='Gale AI') + section(cards_html)
    write(cfg['index'], page(lang=lang, path=cfg['index'], title=cfg['title'], description=cfg['lead'], body=body, alts=alts))
    rev = {v: k for k, v in BLOG_PAIRS.items()}
    for p in posts:
        pair = BLOG_PAIRS.get(p['path']) or rev.get(p['path'])
        alts = {lang: p['path']}
        if pair: alts[other] = pair
        head = (f'<div class="article-head"><div class="crumbs"><a href="{cfg["index"]}">{esc(cfg["crumbs"])}</a>'
                f'<span>/</span><span>{esc(p["date"] or p["list_date"])}</span></div>'
                f'<h1 class="h1" style="font-size:clamp(32px,4.4vw,50px)">{esc(p["title"])}</h1></div>')
        content = [('lede', p['lede'])] if p['lede'] else []
        content += [('img', p['cover'])] + p['blocks']
        body = (f'<section class="sec sec-white"><div class="wrap stack-lg">{head}{prose(content)}</div></section>'
                + cta(lang))
        write(p['path'], page(lang=lang, path=p['path'], title=p['title'] + ' — Gale AI',
                              description=(p['lede'] or p['excerpt'])[:160], body=body, alts=alts))
    return posts


# ------------------------------------------------------------------ privacy
def privacy():
    d = load('privacy')
    texts = [i[1] for b in d['blocks'] if b['type'] == '106' for i in b['items'] if i[0] == 't']
    title = texts[0].strip()
    blocks = []
    for line in texts[1].split('\n'):
        line = line.strip()
        if not line:
            continue
        if re.match(r'^\d{1,2}\.\s+\S', line) and len(line) < 120:
            blocks.append(('h2', line))
        else:
            blocks.append(('p', line))
    head = f'<div class="article-head"><h1 class="h1" style="font-size:clamp(30px,4vw,46px)">{esc(title)}</h1></div>'
    body = f'<section class="sec sec-white"><div class="wrap stack-lg">{head}{prose(blocks, "legal")}</div></section>'
    write('/privacy/', page(lang='ru', path='/privacy/', title=title + ' — Gale AI',
                            description='Политика обработки персональных данных Gale AI (ИП Кокора Павел Евгеньевич).', body=body))


# ------------------------------------------------------------------ main
MONTHS_RU = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
MONTHS_EN = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
MON_KEYS = ['jan', 'feb', 'mar', 'apr', 'ma', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
MON_KEYS_RU = ['янв', 'фев', 'мар', 'апр', 'ма', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']


def fmt_date(raw, lang):
    """Tilda dates are inconsistent ('MAY, 17 2018', 'МАЙ, 16 / 2024'); the posts were all written in 2024."""
    low = raw.lower()
    day = re.search(r'\b(\d{1,2})\b', low)
    mi = next((i for i, k in enumerate(MON_KEYS) if k in low), None)
    if mi is None:
        mi = next((i for i, k in enumerate(MON_KEYS_RU) if k in low), None)
    if mi is None or not day:
        return raw
    d = int(day.group(1))
    return f'{d} {MONTHS_RU[mi]} 2024' if lang == 'ru' else f'{MONTHS_EN[mi]} {d}, 2024'


def main():
    only = sys.argv[sys.argv.index('--only') + 1] if '--only' in sys.argv else None
    if only:
        m = importlib.import_module(only)
        for p in m.PAGES:
            print('wrote', write(p['path'], page(**p)))
        for old, new in getattr(m, 'REDIRECTS', []):
            redirect(old, new)
        return
    landing('ru', '/', {'ru': '/', 'en': '/en/', 'vn': '/vn/'})
    landing('en', '/en/', {'ru': '/', 'en': '/en/', 'vn': '/vn/'})
    blog('ru')
    blog('en')
    privacy()
    for mod in sorted(B.glob('pages_*.py')):
        m = importlib.import_module(mod.stem)
        for p in m.PAGES:
            write(p['path'], page(**p))
        for old, new in getattr(m, 'REDIRECTS', []):
            redirect(old, new)
    # old Tilda URLs → new locations
    for old, new in [('/ru/', '/'), ('/page52717369.html', '/en/contact-center/'),
                     ('/page52717473.html', '/ru/callcenter/'), ('/page49110001.html', '/blogen/ai-in-finance/'),
                     ('/page49107819.html', '/blogen/ai-in-transportation/'), ('/page49043229.html', '/blogen/ai-in-education/'),
                     ('/page49041315.html', '/blogen/ai-in-medicine/'), ('/page49036701.html', '/blogen/ai-empowering-businesses/'),
                     ('/page47979465.html', '/blogen/ai-transforming-the-world/'), ('/partners/', '/partners/ru/'),
                     ('/freetrial/', '/freetrial/ru/'), ('/cases/inprogress/', '/cases/'), ('/vn/', '/en/'), ('/partners/vn/', '/partners/en/')]:
        redirect(old, new)
    nf = (hero('Страница не найдена', 'Возможно, она переехала. Начните с главной или посмотрите кейсы.', kicker='404',
               buttons=[('На главную', '/', 'primary'), ('Кейсы', '/cases/', 'ghost'), ('English version', '/en/', 'ghost')]))
    write('/404.html', page(lang='ru', path='/404.html', title='Страница не найдена — Gale AI', body=nf))
    if not (kit.IMG_DIR / 'og.png').exists():
        (kit.IMG_DIR / 'og.png').write_bytes((kit.IMG_DIR / 'logo.png').read_bytes())
    # drop downloaded originals that no page uses (e.g. replaced by resized copies)
    used = set()
    for f in kit.ROOT.rglob('*.html'):
        if '_build' not in f.parts:
            used |= set(re.findall(r'/assets/img/([^"\')\s]+)', f.read_text('utf-8')))
    for f in kit.IMG_DIR.iterdir():
        if f.name not in used and f.name not in ('logo.png', 'og.png'):
            f.unlink()
    print('built:', len(list(kit.ROOT.rglob('index.html'))), 'index pages')


if __name__ == '__main__':
    main()
