"""Contact-center product pages: /ru/callcenter/, /en/contact-center/, /vn/.

Content rebuilt from the old Tilda pages (_build/data/page52717473, page52717369, vn).
"""
from kit import *  # noqa
from kit import ROOT, IMG_DIR

T = 'https://static.tildacdn.info/'


def R(url, w=1400):
    """img() + a resized .webp copy for heavy raster images (falls back to the original)."""
    p = img(url)
    if p.lower().endswith('.svg'):
        return p
    try:
        from PIL import Image
    except ImportError:
        return p
    src = ROOT / p.lstrip('/')
    out = src.with_name(f'{src.stem}-w{w}.webp')
    if out.exists():
        return '/assets/img/' + out.name
    if src.stat().st_size < 250_000:
        return p
    im = Image.open(src)
    if im.mode not in ('RGB', 'RGBA'):
        im = im.convert('RGBA')
    im.thumbnail((w, 10_000))
    im.save(out, 'WEBP', quality=85)
    return '/assets/img/' + out.name


# ------------------------------------------------------------------ images
PHOTO = T + 'tild6439-3665-4665-b132-306530663663/IMG_8369.PNG'
GAUGES = [T + 'tild3631-6364-4830-b461-386430636231/noroot.png',   # 60%
          T + 'tild3766-3439-4036-b936-366166656130/noroot.png',   # 73%
          T + 'tild3735-6138-4135-b062-663835306133/noroot.png']   # 68%
KRY = T + 'tild3038-6366-4565-b661-386465336465/KRY.svg'                       # top mistakes (EN)
TOPICS_EN = T + 'tild3337-6434-4235-b736-626434303365/_eng.svg'                # topics / insights (EN)
EN_IMG = dict(dash=T + 'tild6634-6662-4866-b639-363731303537/Conversational-Intel.png',
              team=T + 'tild6335-3131-4263-a435-633936396436/team-performance.png',
              reasons=T + 'tild3564-6266-4332-b936-353139373430/Screenshot_2024-04-3.png')
VN_IMG = dict(dash=T + 'tild3563-6461-4361-a261-353437386438/Conversational_4444.png',
              team=T + 'tild6436-6435-4332-b138-383133366533/team-performance123.png',
              reasons=T + 'tild3337-3931-4636-a639-643363383462/ffvnnnn.png')
RU_SHOT = lambda h: T + h + '/Screenshot_2024-07-0.png'  # noqa: E731

STYLE = '''<style>
.cc-photo{background:var(--accent-soft);border-radius:24px;overflow:hidden;display:flex;justify-content:center;align-items:flex-end;padding:28px 24px 0}
.hero-aside .cc-photo img{border:0;border-radius:0;max-height:520px;width:auto}
.cc-gauges{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:24px;display:grid;gap:20px;grid-template-columns:repeat(3,minmax(0,1fr))}
.sec-white .cc-gauges{background:var(--bg);border-color:transparent}
.cc-gauges figure{display:flex;flex-direction:column;align-items:center;gap:10px;text-align:center}
.cc-gauges img{width:100%;max-width:220px}
.cc-gauges figcaption{margin:0;font-weight:600;color:var(--ink);font-size:clamp(13px,1.4vw,15px);line-height:1.3}
.cc-panel{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:24px;display:flex;flex-direction:column;gap:14px}
.sec-white .cc-panel{background:var(--bg);border-color:transparent}
.cc-panel h3{font-size:20px;line-height:1.3}
.cc-panel p{color:var(--ink-2)}
.cc-panel img{width:100%;border-radius:12px;margin-top:auto}
.cc-tiles{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(min(100%,var(--min,260px)),1fr));align-items:start}
.cc-tiles .shot img{width:100%}
.cc-way{display:flex;flex-direction:column;gap:28px}
.cc-way + .cc-way{border-top:1px solid var(--line);padding-top:64px}
.cc-feat{list-style:none;padding:0;margin:0;display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr))}
.cc-feat li{background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px 18px;display:flex;flex-wrap:wrap;gap:8px 12px;align-items:center;font-weight:500;line-height:1.35}
.sec-white .cc-feat li{background:var(--bg);border-color:transparent}
.cc-feat svg{color:var(--ok);flex:none}
.cc-feat li > span:not(.soon){flex:1 1 150px;min-width:0}
.cc-feat .soon{margin-left:auto;flex:none;font-size:12px;font-weight:600;letter-spacing:.03em;text-transform:uppercase;color:var(--accent);background:var(--accent-soft);padding:4px 8px;border-radius:999px}
.cc-vs{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(min(100%,380px),1fr))}
.cc-vs .card{gap:18px}
.cc-vs .big{font-family:var(--font-head);font-size:clamp(44px,6vw,72px);line-height:1;font-weight:700;letter-spacing:-0.03em;color:var(--dark-accent)}
.cc-vs .old .big{color:#FF8A8A}
.cc-vs .card ul{padding-left:20px;color:var(--dark-text);gap:8px}
.cc-vs .card h3{color:#fff}
.cc-vs .cc-lbl{font-size:14px;font-weight:600;color:var(--dark-text);text-transform:uppercase;letter-spacing:.04em}
.cc-chart{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:clamp(18px,3vw,32px);display:flex;flex-direction:column;gap:14px}
.sec-white .cc-chart{background:var(--bg);border-color:transparent}
.cc-chart svg{width:100%;height:auto;display:block}
.cc-legend{display:flex;flex-wrap:wrap;gap:10px 24px;font-size:15px;font-weight:500;color:var(--ink-2)}
.cc-legend span{display:inline-flex;align-items:center;gap:8px}
.cc-legend i{width:22px;height:4px;border-radius:2px;display:inline-block}
.cc-ind{display:flex;flex-wrap:wrap;gap:12px;list-style:none;padding:0;margin:0}
.cc-ind li{display:inline-flex;align-items:center;gap:12px;background:#fff;border:1px solid var(--line);border-radius:14px;padding:12px 20px 12px 12px;font-weight:600;font-size:17px}
.cc-ind .icon{width:40px;height:40px;border-radius:10px;background:var(--accent-soft);color:var(--accent);display:flex;align-items:center;justify-content:center;flex:none}
@media (max-width:640px){.cc-feat{gap:8px}.cc-feat li{padding:10px 14px;font-size:15px}}
</style>'''


# ------------------------------------------------------------------ helpers
def photo_aside():
    return f'<div class="cc-photo"><img src="{R(PHOTO, 900)}" alt="" loading="eager"></div>'


def gauges(labels):
    return '<div class="cc-gauges">' + ''.join(
        f'<figure><img src="{img(u)}" alt="" loading="lazy"><figcaption>{txt(l)}</figcaption></figure>'
        for u, l in zip(GAUGES, labels)) + '</div>'


def panel(title, image, text=None, alt=''):
    t = f'<p>{txt(text)}</p>' if text else ''
    return f'<div class="cc-panel"><h3>{txt(title)}</h3>{t}<img src="{R(image)}" alt="{esc(alt or title)}" loading="lazy"></div>'


def tiles(items, min=260):
    """items: (url, alt)"""
    return f'<div class="cc-tiles" style="--min:{min}px">' + ''.join(
        f'<div class="shot"><img src="{R(u)}" alt="{esc(a)}" loading="lazy"></div>' for u, a in items) + '</div>'


def features(items, soon_label):
    """items: label or (label, True) for coming soon."""
    out = []
    for it in items:
        label, soon = (it, False) if isinstance(it, str) else it
        s = f'<span class="soon">{esc(soon_label)}</span>' if soon else ''
        out.append(f'<li>{icon("check", 20)}<span>{txt(label)}</span>{s}</li>')
    return '<ul class="cc-feat">' + ''.join(out) + '</ul>'


def versus(old, new):
    """old/new: dict(label, big, title, bullets)."""
    def c(d, cls):
        return (f'<div class="card {cls}"><span class="cc-lbl">{txt(d["label"])}</span>'
                f'<b class="big">{txt(d["big"])}</b><h3>{txt(d["title"])}</h3>'
                '<ul>' + ''.join(f'<li>{txt(b)}</li>' for b in d['bullets']) + '</ul></div>')
    return f'<div class="cc-vs">{c(old, "old")}{c(new, "new")}</div>'


def way(num, title, text, media, side=None):
    head = (f'<div class="sec-head"><span class="kicker">{esc(num)}</span>'
            f'<h3 class="h2" style="font-size:clamp(26px,3vw,36px)">{txt(title)}</h3>'
            f'<p class="lead">{txt(text)}</p></div>')
    if side is not None:
        return f'<div class="cc-way">{split(head + side, media)}</div>'
    return f'<div class="cc-way">{head}{media}</div>'


def growth_chart(with_label, without_label, axis_label):
    # Illustrative chart, redrawn from the original Tilda graphic (no numbers in the source).
    base = [(40, 282), (117, 260), (195, 268), (272, 235), (350, 232)]
    w = base + [(428, 207), (505, 165), (583, 83), (660, 13)]
    wo = base + [(428, 212), (505, 210), (583, 187), (660, 177)]
    pts = lambda p: ' '.join(f'{x},{y + 10}' for x, y in p)  # noqa: E731
    dots_ = ''.join(f'<circle cx="{x}" cy="{y + 10}" r="5" fill="#2747F5"/>' for x, y in w[5:])
    dots_ += ''.join(f'<circle cx="{x}" cy="{y + 10}" r="5" fill="#9AA3B2"/>' for x, y in wo[5:])
    dots_ += ''.join(f'<circle cx="{x}" cy="{y + 10}" r="5" fill="#0B1220"/>' for x, y in base)
    svg = (f'<svg viewBox="0 0 700 320" role="img" aria-label="{esc(axis_label)}: {esc(with_label)} / {esc(without_label)}">'
           '<line x1="20" y1="300" x2="690" y2="300" stroke="#CBD1DC" stroke-width="2"/>'
           '<line x1="20" y1="10" x2="20" y2="300" stroke="#CBD1DC" stroke-width="2"/>'
           '<line x1="350" y1="10" x2="350" y2="300" stroke="#E3E6EC" stroke-width="2" stroke-dasharray="6 6"/>'
           f'<polyline points="{pts(wo[4:])}" fill="none" stroke="#9AA3B2" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>'
           f'<polyline points="{pts(w[4:])}" fill="none" stroke="#2747F5" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>'
           f'<polyline points="{pts(base)}" fill="none" stroke="#0B1220" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>'
           f'{dots_}</svg>')
    legend = (f'<div class="cc-legend"><span><i style="background:#2747F5"></i>{esc(with_label)}</span>'
              f'<span><i style="background:#9AA3B2"></i>{esc(without_label)}</span></div>')
    head = (f'<span style="display:flex;gap:8px;align-items:center;font-weight:600;color:var(--ink)">'
            f'<span style="display:inline-flex;color:var(--accent)">{icon("trend", 20)}</span>{esc(axis_label)}</span>')
    return f'<div class="cc-chart">{head}{svg}{legend}</div>'


# ================================================================== RU
def ru_body():
    hero_ = hero('ИИ-платформа для усиления колл-центра',
                 text='Получите 100% контроль над каждым звонком и каждым сотрудником, который общается '
                      'с клиентами, не тратя сотни часов на ручное прослушивание.',
                 kicker='Gale AI для колл-центра',
                 buttons=[('Хочу демо', CALENDLY), ('Как выглядит платформа', '#platform', 'ghost')],
                 aside=photo_aside(), h1_accent='колл-центра')

    problems = section(cards([
        dict(icon='users', title='Слабая дисциплина у сотрудников'),
        dict(icon='search', title='Непонятно, что происходит в звонках'),
        dict(icon='money', title='Контролировать операторов дорого и сложно'),
    ], min=280), title='Знакомы эти проблемы?', tone='dark')

    solution = section(cards([
        dict(icon='search', title='100% видимость того, что происходит в звонках',
             text='Клиенты — главный источник инсайтов, способных растить выручку. '
                  'Получите полную картину того, о чём говорят ваши клиенты.'),
        dict(icon='shield', title='100% контроль каждого менеджера и каждого звонка',
             text='Больше не нужно тратить ресурсы на прослушивание звонков — платформа сделает это '
                  'быстрее, точнее и дешевле!'),
        dict(icon='heart', title='Мотивированная команда',
             text='Полный контроль над деятельностью операторов повысит их мотивацию работать усерднее! :)'),
    ], min=280), title='У нас есть решение!',
        lead='Платформа с помощью искусственного интеллекта анализирует 100% коммуникаций с клиентами '
             'и даёт полную видимость того, что происходит в звонках, чатах, отзывах и zoom-встречах.')

    s = RU_SHOT
    platform = section(
        split(text_block('Панель мониторинга с ключевыми показателями',
                         'Удобный дашборд наглядно показывает, что происходит в коммуникациях с клиентами '
                         'и как работает каждый сотрудник.\nВы сами решаете, какие показатели отображать и в каком '
                         'виде, — продукт полностью кастомизируется.'),
              shot(s('tild3632-6464-4938-a131-633161643261'), 'Дашборд Gale AI: средний балл, CSAT, темы и эмоции звонков'))
        + tiles([(s('tild3334-6537-4263-b736-646561653231'), 'Средний балл звонка'),
                 (s('tild3335-3963-4363-a236-333235306439'), 'Средняя удовлетворённость клиента'),
                 (s('tild3032-3839-4733-a436-653434633661'), 'Средний процент речи клиента')], min=240)
        + gauges(['Соответствие скрипту', 'Звонков без ошибок', 'Уровень вовлечённости'])
        + tiles([(s('tild6431-3333-4534-b535-303839383063'), 'Тема звонка'),
                 (s('tild6539-6131-4130-b233-326331343436'), 'Настроение клиентов'),
                 (T + 'tild3064-6334-4165-a138-333363326665/photo.svg', 'Темы звонков, инсайты и боли клиентов')], min=260)
        + tiles([(s('tild6632-6639-4038-b636-363936663133'), 'Типы возражений'),
                 (s('tild3866-3865-4666-a164-373238346634'), 'Основные моменты диалога')], min=420)
        + '<div class="grid" style="--min:420px">'
        + panel('ТОП ошибок у операторов', T + 'tild3838-3434-4339-b336-656664386635/5__.svg')
        + panel('Сравнение по ключевым показателям', s('tild3161-3266-4536-b032-653439646431'),
                'Выберите показатели, по которым сравнивать сотрудников. Теперь вы будете знать, '
                'кому дать премию, а с кем провести беседу.')
        + '</div>'
        + split(text_block('Детальный отчёт по каждому звонку',
                           'Изучайте подробно интересующий вас звонок, не тратя много времени.\n'
                           'Резюме звонка и транскрибированный текст диалога помогут за секунды понять, '
                           'что происходило в звонке.'),
                shot(s('tild6636-6137-4261-b065-306132323737'), 'Резюме звонка'), reverse=True)
        + tiles([(s('tild3139-6666-4138-a265-663761376436'), 'Транскрипт диалога с аудиозаписью'),
                 (s('tild3037-6639-4836-b361-313337336337'), 'Соблюдение блоков скрипта, возражения, ключевые моменты')], min=420),
        title='Как выглядит платформа?', lead='Пример интерфейса, данные условные.', tone='white', id='platform')

    feats = section(features([
        'Перевод аудио в текст', 'Резюме звонка и результат звонка',
        'Категоризация звонков по темам и результатам', 'Определение основных моментов диалога',
        'Проверка выполнения пунктов чек-листа / скрипта', 'Определение возражений и способов их отработки',
        'Определение ошибок менеджера по продажам', 'Формирование выводов и рекомендаций',
        'Определение настроения клиента и менеджера', 'Определение удовлетворённости клиента',
        'Коэффициент речи клиента к оператору', 'Выделение слов-паразитов и мата',
        'Персонализированные рекомендации для оператора', 'Отслеживание любых кастомных метрик и параметров',
        'Анализ чатов, отзывов, видеоконференций', 'И многое другое…',
    ], 'Скоро'), title='Функционал платформы', kicker='На июль 2024')

    trial = section(cards([
        dict(icon='clock', title='Быстро',
             text='На проведение теста уйдёт до 2 недель — не нужно ждать результатов месяцами. '
                  'Пилот сразу покажет, где именно бизнес теряет деньги или упускает выгоду.'),
        dict(icon='check', title='Удобно',
             text='Мы сами всё настроим, помощь вашего разработчика не понадобится. Достаточно передать нам '
                  'записи звонков — например, на Google Drive или Яндекс Диске.'),
        dict(icon='chart', title='Наглядно',
             text='Все результаты аналитики вы увидите в красивых и удобных графиках.'),
        dict(icon='money', title='Бесплатно',
             text='Проведение теста абсолютно бесплатно и ни к чему вас не обязывает.'),
    ], min=240) + btns(('Протестировать бесплатно', CALENDLY), ('Хочу демо', CALENDLY, 'ghost')),
        title='Протестируйте бесплатно',
        lead='Начните с пилотного проекта (до 1000 звонков), чтобы познакомиться с возможностями платформы '
             'и увидеть, какие выгоды она может принести именно вашему бизнесу.', tone='white')

    return STYLE + hero_ + problems + solution + platform + feats + trial + cta('ru')


# ================================================================== EN / VN (same structure)
L = {
    'en': dict(
        h1='The AI platform that empowers your contact center', accent='contact center',
        kicker='Gale AI for contact centers',
        sub='Put customer conversations at the center of your business and unlock revenue potential.',
        demo='Book a demo', how='How it works',
        ind_title='Which industries need Gale AI',
        industries=[('heart', 'Medical practice'), ('spark', 'IT services'), ('phone', 'Telecommunications'),
                    ('building', 'Real estate'), ('money', 'Retail')],
        vs_title='Manual call listening vs. Gale AI call analytics', vs_lead=None,
        old=dict(label='Traditional approach — manual call listening', big='Up to 5%',
                 title='of calls are analyzed by managers',
                 bullets=['Up to 5% of calls analyzed', 'No control over operators', 'Random assessment',
                          'No understanding of what happens in communications',
                          'Expensive to scale: as the contact center / sales department grows, more quality '
                          'control managers need to be hired',
                          'Weak discipline among employees, because they know their calls aren’t being monitored']),
        new=dict(label='Innovative approach — Gale AI call analytics', big='100%',
                 title='of calls are analyzed by the platform',
                 bullets=['100% of calls analyzed', 'Full control over operators', 'No random assessments',
                          'Complete understanding of what happens in customer communications',
                          'Reduction in personnel costs',
                          'High discipline among employees, as they know every call is monitored and analyzed',
                          'Increased efficiency of each employee']),
        ben_title='What does the innovative approach bring to business?',
        benefits=[('money', 'Reduction in operational costs'), ('book', 'Faster onboarding of newcomers'),
                  ('trend', 'Revenue growth')],
        ways_title='3 ways Gale helps you drive revenue',
        control=('Control', 'With advanced AI call analytics you can track key metrics for each operator, '
                            'saving dozens of hours.'),
        gauges=['Script compliance', 'Error-free calls', 'Engagement level'],
        train=('Train', 'With access to error analysis and personalized recommendations for each operator, managers '
                        'can train more effectively, significantly reducing the time it takes employees to reach '
                        'full productivity.'),
        mistakes='Top mistakes by operators', team='Team performance analytics',
        explore=('Explore', 'Customers are the main source of insights for every business, so stay informed about '
                            'what your customers are saying. Use Gale AI to classify conversations by topic and '
                            'highlight key insights — and direct your efforts to where they will generate the '
                            'greatest revenue.'),
        reasons='Conversation reasons', topics='Call topics, insights and customer pains',
        dash='Gale AI dashboard: total conversations, automation type, conversation trend',
        curve='Stay ahead of the curve with Gale AI', with_='With Gale AI', without='Without Gale AI',
        growth='Revenue growth',
        feat_title='Gale AI features', soon='Coming soon',
        features=['Transcription of audio to text', 'Emotional tone of the customer’s and operator’s speech',
                  'Script adherence', 'Highlighting operator errors', 'Talk-to-listen ratio',
                  'Call categorization by topic', 'Determining customer satisfaction', 'Overall call score',
                  'Highlighting filler words and profanity', 'Personalized recommendations for the operator',
                  ('Real-time recommendations for operators', True),
                  ('Custom metrics for tracking', True), ('Email and chat analysis', True)],
        cta_title='Get a free trial to see the magic in action',
        cta_text='Free trial — up to 500 minutes. Do you want to see how to unlock new revenue?',
    ),
    'vn': dict(
        h1='Nền tảng AI để tăng cường trung tâm liên hệ', accent='trung tâm liên hệ',
        kicker='Gale AI cho trung tâm liên hệ',
        sub='Đặt cuộc trò chuyện của khách hàng vào trung tâm của doanh nghiệp bạn và mở khóa tiềm năng doanh thu.',
        demo='Đặt lịch trình diễn', how='Cách hoạt động',
        ind_title=None, industries=None,
        vs_title='Bạn đã sẵn sàng khám phá những kho báu ẩn giấu trong doanh thu của mình chưa?', vs_lead=None,
        old=dict(label='Cách tiếp cận truyền thống — nghe cuộc gọi thủ công', big='5%',
                 title='Chỉ có tới 5% cuộc gọi được các quản lý đánh giá',
                 bullets=['Chỉ phân tích tới 5% cuộc gọi', 'Không kiểm soát được các nhân viên điều hành',
                          'Đánh giá ngẫu nhiên', 'Không hiểu biết gì về những gì đang xảy ra trong giao tiếp',
                          'Tốn kém để mở rộng: với sự phát triển của bộ phận trung tâm liên hệ/bán hàng, cần phải '
                          'thuê thêm nhiều quản lý kiểm soát chất lượng',
                          'Kỷ luật yếu kém ở nhân viên, vì họ biết rằng không ai nghe những cuộc gọi của họ']),
        new=dict(label='Cách tiếp cận sáng tạo — phân tích cuộc gọi Gale AI', big='100%',
                 title='100% cuộc gọi được nền tảng đánh giá',
                 bullets=['Phân tích 100% cuộc gọi', 'Kiểm soát đầy đủ đối với các nhân viên điều hành',
                          'Không có đánh giá ngẫu nhiên',
                          'Hiểu biết đầy đủ về những gì đang xảy ra trong giao tiếp với khách hàng',
                          'Giảm chi phí nhân sự',
                          'Kỷ luật cao ở nhân viên, vì họ biết mỗi cuộc gọi đều được nghe và phân tích',
                          'Tăng hiệu quả công việc của mỗi nhân viên']),
        ben_title='Cách tiếp cận sáng tạo mang lại điều gì cho doanh nghiệp?',
        benefits=[('money', 'Giảm chi phí hoạt động'), ('book', 'Đào tạo nhân viên mới nhanh hơn'),
                  ('trend', 'Tăng trưởng doanh thu')],
        ways_title='3 cách Gale giúp bạn tăng doanh thu',
        control=('Kiểm soát', 'Với phân tích cuộc gọi AI tiên tiến, bạn có thể theo dõi các chỉ số quan trọng cho '
                              'mỗi nhân viên điều hành, tiết kiệm hàng chục giờ.'),
        gauges=['Tuân thủ kịch bản', 'Cuộc gọi không có lỗi', 'Mức độ tương tác'],
        train=('Đào tạo', 'Với quyền truy cập vào phân tích lỗi và khuyến nghị cá nhân hóa cho mỗi nhân viên điều '
                          'hành, các quản lý có thể đào tạo hiệu quả hơn, giảm đáng kể thời gian để đạt được năng '
                          'suất làm việc đầy đủ của nhân viên.'),
        mistakes='Lỗi phổ biến nhất của nhân viên điều hành', team='Phân tích hiệu suất nhóm',
        explore=('Khám phá', 'Vì khách hàng là nguồn thông tin quan trọng nhất cho mọi doanh nghiệp, hãy luôn cập '
                             'nhật những gì khách hàng của bạn nói. Bằng cách sử dụng Gale AI để phân loại cuộc trò '
                             'chuyện theo chủ đề và làm nổi bật những thông tin quan trọng, bạn có thể hướng nỗ lực '
                             'của mình vào những nơi sẽ sinh lợi nhuận cao nhất.'),
        reasons='Lý do trò chuyện', topics='Chủ đề cuộc gọi, thông tin chi tiết và vấn đề của khách hàng',
        dash='Bảng điều khiển Gale AI', curve='Hãy luôn đi trước một bước', with_='Với Gale AI',
        without='Không có Gale AI', growth='Tăng trưởng doanh thu',
        feat_title='Các tính năng của Gale AI', soon='Sắp ra mắt',
        features=['Chuyển đổi âm thanh thành văn bản', 'Tông giọng cảm xúc của khách hàng và người điều hành',
                  'Tuân thủ kịch bản', 'Nhấn mạnh lỗi của người điều hành', 'Talk-to-listen ratio',
                  'Phân loại cuộc gọi theo chủ đề', 'Xác định sự hài lòng của khách hàng',
                  'Điểm số cuộc gọi tổng thể', 'Nhấn mạnh các từ lấp và từ tục',
                  'Đề xuất cá nhân hóa cho người điều hành',
                  ('Đề xuất thời gian thực cho người điều hành', True),
                  ('Chức năng của các chỉ số tùy chỉnh để theo dõi', True), ('Phân tích email, trò chuyện', True)],
        cta_title='Nhận thử nghiệm miễn phí để thấy phép màu trong hành động',
        cta_text='Dùng thử miễn phí — lên đến 500 phút. Mở khóa tiềm năng doanh thu ngay hôm nay!',
    ),
}


def intl_body(lang):
    c = L[lang]
    im = EN_IMG if lang == 'en' else VN_IMG
    out = STYLE + hero(c['h1'], text=c['sub'], kicker=c['kicker'],
                       buttons=[(c['demo'], CALENDLY), (c['how'], '#platform', 'ghost')],
                       aside=photo_aside(), h1_accent=c['accent'])
    if c['industries']:
        out += section('<ul class="cc-ind">' + ''.join(
            f'<li><span class="icon">{icon(i, 22)}</span>{txt(t)}</li>' for i, t in c['industries']) + '</ul>',
            title=c['ind_title'], tight=True)
    out += section(versus(c['old'], c['new']), title=c['vs_title'], tone='dark')
    out += section(cards([dict(icon=i, title=t) for i, t in c['benefits']], min=240),
                   title=c['ben_title'], tone='white', tight=True)
    ways = (
        way('01', c['control'][0], c['control'][1],
            shot(im['dash'], c['dash']), side=gauges(c['gauges']))
        + way('02', c['train'][0], c['train'][1],
              '<div class="grid" style="--min:400px">' + panel(c['mistakes'], KRY) + panel(c['team'], im['team'])
              + '</div>')
        + way('03', c['explore'][0], c['explore'][1],
              '<div class="grid" style="--min:400px">' + panel(c['reasons'], im['reasons'])
              + panel(c['topics'], TOPICS_EN) + '</div>')
    )
    out += section(ways, title=c['ways_title'], id='platform')
    out += section(growth_chart(c['with_'], c['without'], c['growth']), title=c['curve'], tone='white')
    out += section(features(c['features'], c['soon']), title=c['feat_title'])
    out += cta(lang, title=c['cta_title'], text=c['cta_text'])
    return out


CC_ALTS = {'ru': '/ru/callcenter/', 'en': '/en/contact-center/', 'vn': '/vn/'}

PAGES = [
    dict(lang='ru', path='/ru/callcenter/',
         title='Gale AI для колл-центра — 100% контроль каждого звонка',
         description='ИИ-платформа для усиления колл-центра: 100% контроль над каждым звонком и каждым сотрудником '
                     'без сотен часов ручного прослушивания. Бесплатный пилот до 1000 звонков.',
         body=ru_body(), alts=CC_ALTS),
    dict(lang='en', path='/en/contact-center/',
         title='Gale AI for contact centers — AI call analytics for 100% of calls',
         description='The AI platform that empowers your contact center: analyze 100% of calls, control and train '
                     'operators, and unlock revenue potential from customer conversations.',
         body=intl_body('en'), alts=CC_ALTS),
]
