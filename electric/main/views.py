from django.shortcuts import render
from allmodels.models import *
from allmodels.forms import *



# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form. is_valid():
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
        'Отзывы': 'clients',
        'Контакт': 'contact'
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

    }
    return render(request, 'main/index.html', data)
