from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class About(models.Model):
    title1 = models.CharField('О нас', max_length=60)
    title2 = models.CharField('Что делаем', max_length=60)
    text = models.TextField('Описание')
    service1 = models.CharField('Услуга1', max_length=60)
    service2 = models.CharField('Услуга2', max_length=60)
    service3 = models.CharField('Услуга3', max_length=60)
    service4 = models.CharField('Услуга4', max_length=60)
    image = models.ImageField('Картинка', upload_to='static/images')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title1


class Carousel(models.Model):
    image1 = models.ImageField('Фото1', upload_to='static/images')
    image2 = models.ImageField('Фото2', upload_to='static/images')
    image3 = models.ImageField('Фото3', upload_to='static/images')
    title1 = models.CharField('Заголовок1', max_length=40)
    title2 = models.CharField('Заголовок2', max_length=40)
    title3 = models.CharField('Заголовок3', max_length=40)
    subtitle1 = models.TextField('Описание1')
    subtitle2 = models.TextField('Описание2')
    subtitle3 = models.TextField('Описание3')

    class Meta:
        verbose_name = 'Карусель'
        verbose_name_plural = 'Карусели'

    def __str__(self):
        return self.title1


class Portfolio(models.Model):
    image_small = models.ImageField('Фото мал', upload_to='static/images')
    image_big = models.ImageField('Фото бол', upload_to='static/images')
    title = models.CharField('Надпись', max_length=40)

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'

    def __str__(self):
        return self.title


class Choise(models.Model):
    title = models.CharField('Заголовок', max_length=40)
    subtitle = models.TextField('Описание')

    class Meta:
        verbose_name = 'Выбор'
        verbose_name_plural = 'Выбор'

    def __str__(self):
        return self.title


class Feedback(models.Model):
    title1 = models.CharField('Имя клиента1', max_length=40)
    title2 = models.CharField('Имя клиента2', max_length=40)
    title3 = models.CharField('Имя клиента3', max_length=40)
    title4 = models.CharField('Имя клиента4', max_length=40)
    text1 = models.CharField('Отзыв1', max_length=250)
    text2 = models.CharField('Отзыв2', max_length=250)
    text3 = models.CharField('Отзыв3', max_length=250)
    text4 = models.CharField('Отзыв4', max_length=250)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.title1


class Contact(models.Model):
    name = models.CharField('Имя', max_length=30)
    l_name = models.CharField('Фамилия', max_length=30)
    email = models.EmailField('Почта')
    tel = PhoneNumberField(verbose_name='Телефон')
    message = models.TextField('Сообщение')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.email
