# Generated by Django 3.2.8 on 2021-10-11 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allmodels', '0009_delete_tictoc_carousel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/images', verbose_name='Фото')),
                ('title', models.CharField(max_length=40, verbose_name='Имя клиента')),
                ('text', models.CharField(max_length=250, verbose_name='Отзыв')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
