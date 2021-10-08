from django.db import models


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
