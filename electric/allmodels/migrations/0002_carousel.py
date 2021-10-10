# Generated by Django 3.2.8 on 2021-10-08 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allmodels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/images', verbose_name='Фото')),
                ('title', models.CharField(max_length=40, verbose_name='Заголовок')),
                ('subtitle', models.TextField(verbose_name='Подзаголовок')),
            ],
            options={
                'verbose_name': 'Карусель',
                'verbose_name_plural': 'Карусели',
            },
        ),
    ]
