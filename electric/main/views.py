from django.shortcuts import render
from allmodels.models import *


# Create your views here.
def index(request):
    portfolio = Portfolio.objects.all()
    carousel = Carousel.objects.all()
    about = About.objects.all()

    menu_nav = {
        'Home': 'home',
        'About': 'about',
        'Service': 'services',
        'Gallery': 'gallery',
        'Clients': 'clients',
        'Contact': 'contact'
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
    }
    return render(request, 'main/index.html', data)
