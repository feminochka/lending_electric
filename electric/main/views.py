from django.shortcuts import render
from allmodels.models import *
from allmodels.forms import *


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    form = ContactForm()
    feedback = Feedback.objects.all()
    choise = Choise.objects.all()
    portfolio = Portfolio.objects.all()
    carousel = Carousel.objects.all()
    about = About.objects.all()

    menu_nav = {
        'O нас': 'about',
        'Услуги': 'services',
        'Портфолио': 'gallery',
        'Видео': 'clients',
        'Отзывы': 'team',
        'Контакт': 'contact',
    }

    data = {
        'about': about,
        'count1': 6,
        'count2': 1.5,
        'count3': 100,
        'count4': 6,
        'title_count1': "ОПЫТ РАБОТЫ",
        'title_count2': "ОПЫТ В СТРАНАХ ЕВРОПЫ",
        'title_count3': "ВЫПОЛНЕННЫХ ОБЪЕКТОВ",
        'title_count4': "КВАЛИФИЦИРОВАННЫЙ ПЕРСОНАЛ",
        'menu_nav': menu_nav,
        'carousel': carousel,
        'portfolio': portfolio,
        'choise': choise,
        'feedback': feedback,
        'form': form,
        'time_work': '7:00 - 24:00',
        'address': 'г.Минск, ул.Белецкого 4',
        'phone': '+375(29)134 07 49',
        'email': 'electricmanby@yandex.by',
        'site': 'http://electricman.by',
        'map': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2353.214535121841!2d27.46472051582663!3d53.85683298008917!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46dbda7ff6ae3c61%3A0x939289a9c11b22d8!2z0YPQuy4g0JHQtdC70LXRhtC60L7Qs9C-IDQsINCc0LjQvdGB0LosINCR0LXQu9Cw0YDRg9GB0Yw!5e0!3m2!1sru!2ses!4v1634154513679!5m2!1sru!2ses',
        'icon_instagram': 'https://pngicon.ru/file/uploads/instagram-1-50x50.png',
        'instagram': 'https://instagram.com/anton.prymerau?utm_medium=copy_link',
        'icon_tiktok': 'https://pngicon.ru/file/uploads/tiktok-50x50.png',
        'tiktok': 'https://www.tiktok.com/@cardinal_mvp?_d=secCgYIASAHKAESPgo8czUNPR8UgRYQIWUi4dkAGoKjMHJDwUXza5Ko1hmEO8cH0GNWzi73URANnlLfO6EhrZeLYgHF1o9r7%2B5RGgA%3D&checksum=bc1ddd95e6452429461e7ec81c424bae6219256cc3755bd7bc935aba5a020a7d&language=ru&preview_pb=0&sec_user_id=MS4wLjABAAAADjl8D45NOKe4Ba9jvBeSjTtuybZyNQhqaBOro0sDvz3LnzzePmmPZUDEsddJ4_1u&share_app_id=1233&share_item_id=6995189294046498054&share_link_id=1b813440-904d-4588-b998-d363fd80914a&source=h5_m&timestamp=1633780299&u_code=dd80hg6ie20535&user_id=6845017196608930822&utm_campaign=client_share&utm_medium=android&utm_source=copy&_r=1&is_copy_url=1&is_from_webapp=v1',
        'icon_vk': 'https://pngicon.ru/file/uploads/vkontakte-50x50.png',
        'vk': 'https://m.vk.com/cardinalmvp?act=info',
        'footer_about': '«Да будет свет!» — сказал электрик и перерезал провода. Работа электриком требует спокойствия, взвешенных решений, повышенного внимания к мелочам. Эта профессия не изобилует творчеством и яркими красками. Это серьезная техническая работа.',


    }
    return render(request, 'main/index.html', data)
