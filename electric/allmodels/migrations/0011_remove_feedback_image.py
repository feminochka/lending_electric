# Generated by Django 3.2.8 on 2021-10-12 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allmodels', '0010_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='image',
        ),
    ]
