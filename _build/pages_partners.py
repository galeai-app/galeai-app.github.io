"""Partner program pages: /partners/ru/, /partners/en/, /partners/vn/.

Content comes from the old Tilda pages (_build/data/partners_*.txt), lightly copy-edited.
The Tilda application form is gone, so "Become a partner" opens a pre-filled email,
with WhatsApp / Telegram as the secondary channel.
"""
from urllib.parse import quote

from kit import (EMAIL, PHONE, TELEGRAM, WHATSAPP, btn, cards, esc, hero, section,
                 stats, steps, txt)

ALTS = {'ru': '/partners/ru/', 'en': '/partners/en/', 'vn': '/partners/vn/'}
ZALO_PHONE = '+84 8 9822 5072'          # contact listed on the old EN/VN pages
ZALO = 'https://zalo.me/84898225072'


def mailto(subject):
    return f'mailto:{EMAIL}?subject={quote(subject)}'


C = {
    'ru': dict(
        title='Партнёрская программа Gale AI — до 25% от платежей клиентов',
        description='Получайте до 25% от всех платежей привлечённых клиентов: предлагайте Gale AI своим клиентам и зарабатывайте комиссию.',
        kicker='Партнёрская программа',
        h1='Присоединяйтесь к партнёрской программе Gale AI',
        lead='Предлагайте Gale AI своим клиентам и зарабатывайте комиссию. Предлагая Gale AI, вы не только получаете '
             'новый источник дохода, но и усиливаете своё преимущество на рынке за счёт инновационного продукта.',
        apply='Стать партнёром', subject='Партнёрская программа Gale AI',
        wa='Написать в WhatsApp',
        more=('Узнать больше о продукте', '/'),
        stats=[('25%', 'Партнёрская комиссия до 25% от платежей — выплачивается, пока клиент пользуется продуктом'),
               ('180 000 ₽', 'Средний заработок на комиссиях с одного клиента за год. Чем больше компания, '
                              'тем выше тариф и, соответственно, ваша комиссия')],
        reasons_title='6 причин работать с нами',
        reasons=[('Новый источник дохода',
                  'Зарабатывайте комиссию с каждой транзакции и увеличьте доход компании с инновационным продуктом.'),
                 ('Технологическое преимущество',
                  'Имея в арсенале ИИ-технологии, вы улучшаете предложение своей компании и выделяетесь на рынке.'),
                 ('Повышение клиентской лояльности',
                  'Предлагая инновационные решения, вы не только удовлетворяете потребности клиентов, '
                  'но и усиливаете их лояльность к вашему бренду.'),
                 ('Маркетинговая и техническая поддержка',
                  'Вы получите полную поддержку от нашей команды, включая маркетинговые материалы и решение технических вопросов.'),
                 ('Для юр. лиц и физ. лиц', 'Вы можете привлекать клиентов, даже если у вас нет компании.'),
                 ('Клиент закреплён за партнёром',
                  'Приведённые вами клиенты закрепляются за вами и продолжают приносить вам доход долгое время.')],
        fit=dict(title='Продукт подходит для любого бизнеса, где есть звонки с клиентами',
                 groups=[('building', 'Для различных сегментов рынка',
                          ['Ритейл', 'Автомобильный бизнес', 'Строительство и недвижимость', 'Финансовый сектор',
                           'Телекоммуникации', 'Транспортно-логистические компании', 'Страховые компании',
                           'Туризм (отели, авиа, ЖД, круизы)', 'И другие']),
                         ('users', 'Для разных отделов внутри компаний',
                          ['Отдел продаж', 'Отдел клиентской поддержки', 'Отдел технической поддержки',
                           'Отдел маркетинга'])]),
        steps_title='Начать очень просто',
        steps=[('Оставьте заявку', 'Напишите на hello@galeapp.co или в Telegram / WhatsApp, чтобы принять участие в программе.'),
               ('Встреча', 'Проведём встречу, где всё расскажем и покажем, ответим на вопросы.'),
               ('Заключение договора', 'Закрепим все условия сотрудничества.'),
               ('Начало работы', 'Предлагайте наш продукт и зарабатывайте комиссионные!')],
        end=dict(title='Станьте партнёром Gale AI',
                 text='Напишите нам — расскажем об условиях программы, проведём встречу и ответим на вопросы.',
                 q='Есть вопросы?', box='Заявка на участие',
                 box_text='Тема письма уже заполнена — просто отправьте его, и мы свяжемся с вами.'),
        zalo=False,
    ),
    'en': dict(
        title='Gale AI Partner Program — up to 50% commission',
        description='Earn up to 50% commission selling Gale AI: offer the platform to your clients and get paid for as long as they pay.',
        kicker='Partner program',
        h1='Join the Gale AI Partner Program',
        lead='Offer the Gale AI platform to your clients and get commission. By offering our cutting-edge product, '
             'you will not only expand your advantage on the market but also significantly increase your income.',
        apply='Become a partner', subject='Gale AI Partner Program application',
        wa='Message us on WhatsApp',
        more=('Learn more about the product', '/en/'),
        stats=[('50%', 'Partner commission up to 50%, paid as long as the client pays'),
               ('$3,000', 'Average earnings per client per year. The larger the company, the more expensive '
                          'our solution and the higher your commission')],
        reasons_title='6 reasons to work with us',
        reasons=[('New source of income',
                  'Earn substantial commissions on each transaction, expanding your business with a new, in-demand product.'),
                 ('Technological advantage',
                  "Gain access to cutting-edge AI technologies that will improve your company's offerings and distinguish you in the market."),
                 ('Enhancing client loyalty',
                  'By offering innovative solutions, you will not only meet the needs of your clients but also '
                  'strengthen their trust and loyalty to your brand.'),
                 ('Marketing and technical support',
                  'Receive full support from our team, including marketing materials and technical assistance, '
                  'which will facilitate implementation and sales.'),
                 ('For both companies and individuals', "You can attract clients even if you don't have a company."),
                 ('Clients stay assigned to you',
                  'All your referred clients are registered under you, ensuring you a continuous income from each '
                  'of their transactions in the future.')],
        fit=None,
        steps_title='Getting started is easy',
        steps=[('Apply', 'Send us your partnership application by email or via WhatsApp / Telegram.'),
               ('Get access', 'Gain access to our resources.'),
               ('Start earning', 'Begin offering Gale AI to your clients and earn commissions.')],
        end=dict(title='Become a Gale AI partner',
                 text='Send us your application and we’ll get you started with our resources.',
                 q='Have a question?', box='Partnership application',
                 box_text='The email subject is already filled in — just hit send and we’ll get back to you.'),
        zalo=True,
    ),
    'vn': dict(
        title='Chương trình đối tác Gale AI — hoa hồng lên đến 50%',
        description='Nhận hoa hồng lên đến 50% khi chào bán Gale AI cho khách hàng của bạn, được thanh toán miễn là khách hàng vẫn thanh toán.',
        kicker='Chương trình đối tác',
        h1='Tham gia Chương trình Đối tác của Gale AI',
        lead='Chào bán Nền tảng Gale AI cho khách hàng của bạn và nhận hoa hồng. Bằng cách cung cấp sản phẩm tiên tiến '
             'của chúng tôi, bạn không chỉ mở rộng lợi thế của mình trên thị trường mà còn tăng đáng kể thu nhập của mình.',
        apply='Trở thành đối tác', subject='Đăng ký đối tác Gale AI',
        wa='Nhắn tin qua WhatsApp',
        more=('Tìm hiểu thêm về sản phẩm', '/vn/'),
        stats=[('50%', 'Hoa hồng đối tác lên đến 50%, được thanh toán miễn là khách hàng vẫn thanh toán'),
               ('$3,000', 'Thu nhập trung bình $3000 từ mỗi khách hàng mỗi năm, công ty càng lớn thì giải pháp '
                          'của chúng tôi càng đắt và hoa hồng của bạn càng cao')],
        reasons_title='6 lý do để làm việc với chúng tôi',
        reasons=[('Nguồn thu nhập mới',
                  'Kiếm được hoa hồng đáng kể trên mỗi giao dịch, mở rộng kinh doanh của bạn với sản phẩm mới, '
                  'đáp ứng nhu cầu thị trường.'),
                 ('Lợi thế công nghệ',
                  'Truy cập vào các công nghệ AI tiên tiến sẽ cải thiện các sản phẩm của công ty bạn và làm nổi bật '
                  'bạn trên thị trường.'),
                 ('Tăng cường sự trung thành của khách hàng',
                  'Bằng cách cung cấp các giải pháp sáng tạo, bạn không chỉ đáp ứng nhu cầu của khách hàng mà còn '
                  'tăng cường sự tin tưởng và lòng trung thành của họ đối với thương hiệu của bạn.'),
                 ('Hỗ trợ tiếp thị và kỹ thuật',
                  'Nhận được sự hỗ trợ đầy đủ từ đội ngũ của chúng tôi, bao gồm tài liệu tiếp thị và hỗ trợ kỹ thuật, '
                  'giúp dễ dàng triển khai và bán hàng.'),
                 ('Chúng tôi làm việc với cả doanh nghiệp và cá nhân',
                  'Bạn có thể thu hút khách hàng, ngay cả khi bạn không có công ty.'),
                 ('Giữ khách hàng bởi đối tác',
                  'Tất cả khách hàng bạn giới thiệu sẽ được đăng ký dưới tên bạn, đảm bảo thu nhập liên tục từ mỗi '
                  'giao dịch của họ trong tương lai.')],
        fit=None,
        steps_title='Bắt đầu rất đơn giản',
        steps=[('Đăng ký', 'Gửi đơn đăng ký đối tác cho chúng tôi qua email, Zalo hoặc WhatsApp / Telegram.'),
               ('Truy cập nguồn lực', 'Truy cập vào các nguồn lực của chúng tôi và bắt đầu đào tạo.'),
               ('Kiếm hoa hồng', 'Bắt đầu cung cấp Gale AI cho khách hàng của bạn và kiếm hoa hồng.')],
        end=dict(title='Trở thành đối tác Gale AI',
                 text='Gửi đơn đăng ký cho chúng tôi để truy cập vào các nguồn lực và bắt đầu đào tạo.',
                 q='Còn câu hỏi?', box='Đơn đăng ký đối tác',
                 box_text='Tiêu đề email đã được điền sẵn — chỉ cần gửi đi, chúng tôi sẽ liên hệ lại với bạn.'),
        zalo=True,
    ),
}
# EN step 1 also mentioned Zalo on the old page's contacts
C['en']['steps'][0] = ('Apply', 'Send us your partnership application by email, Zalo or WhatsApp / Telegram.')

STYLE = '''<style>
.pp-stats .stats{grid-template-columns:1fr}
.pp-more{color:var(--accent);font-weight:600;font-size:16px}
.pp-cta .contacts a{word-break:break-word}
@media (max-width:640px){.pp-cta .cta{padding:32px 20px}.pp-cta .cta-box{padding:22px 18px}}
</style>'''


def final(lang, c):
    e = c['end']
    lines = [f'<span>{esc(e["q"])}</span>',
             f'<span>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></span>',
             f'<span>Telegram: <a href="{TELEGRAM}" target="_blank" rel="noopener">{PHONE}</a></span>',
             f'<span>WhatsApp: <a href="{WHATSAPP}" target="_blank" rel="noopener">{PHONE}</a></span>']
    if c['zalo']:
        lines.append(f'<span>Zalo: <a href="{ZALO}" target="_blank" rel="noopener">{ZALO_PHONE}</a></span>')
    return f'''<section class="sec pp-cta" id="contact"><div class="wrap"><div class="cta">
<div><h2 class="h2">{txt(e['title'])}</h2><p>{txt(e['text'])}</p>
<div class="contacts">{''.join(lines)}</div></div>
<div class="cta-box"><p style="font-family:var(--font-head);font-size:22px;font-weight:600;color:var(--ink)">{esc(e['box'])}</p>
<p>{esc(e['box_text'])}</p>{btn(c['apply'], mailto(c['subject']), 'primary')}{btn('WhatsApp', WHATSAPP, 'ghost')}{btn('Telegram', TELEGRAM, 'ghost')}</div>
</div></div></section>'''


def build(lang):
    c = C[lang]
    path = ALTS[lang]
    more_label, more_href = c['more']
    top = hero(
        c['h1'], c['lead'], kicker=c['kicker'], h1_accent='Gale AI',
        buttons=[(c['apply'], mailto(c['subject']), 'primary'), (c['wa'], WHATSAPP, 'ghost')],
        aside=f'<div class="pp-stats">{stats(c["stats"])}</div>')
    top = top.replace('</div><div class="hero-aside">',
                      f'<a class="pp-more" href="{more_href}">{esc(more_label)} →</a></div><div class="hero-aside">', 1)
    body = STYLE + top
    body += section(cards([{'num': i + 1, 'title': t, 'text': x} for i, (t, x) in enumerate(c['reasons'])], min=300),
                    title=c['reasons_title'], tone='dark')
    if c['fit']:
        f = c['fit']
        body += section(cards([{'icon': ic, 'title': t, 'bullets': b} for ic, t, b in f['groups']], min=320),
                        title=f['title'], tone='white')
        body += section(steps(c['steps']), title=c['steps_title'])
    else:
        body += section(steps(c['steps']), title=c['steps_title'], tone='white')
    body += final(lang, c)
    return dict(lang=lang, path=path, title=c['title'], description=c['description'], body=body, alts=ALTS)


PAGES = [build(l) for l in ('ru', 'en')]  # VN version removed on request
