# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-12 20:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0047_auto_20160913_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='adres',
            field=models.CharField(max_length=140, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='about',
            name='phone',
            field=models.CharField(default='+7(347)-xxx-xxx', max_length=20, verbose_name='Телефоны для контактов'),
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='approve',
            name='imp',
            field=models.CharField(choices=[('Лицензии', 'Лицензии'), ('Свидетельства', 'Свидетельства'), ('Аттестаты', 'Аттестаты'), ('Свидетельства', 'Сертификаты')], max_length=20, verbose_name='Тип документа'),
        ),
        migrations.AlterField(
            model_name='approve',
            name='name',
            field=models.TextField(verbose_name='Описание докумета'),
        ),
        migrations.AlterField(
            model_name='approve',
            name='ref',
            field=models.CharField(default='http://placehold.it/100x100', max_length=100, verbose_name='Ссылка на изображение'),
        ),
        migrations.AlterField(
            model_name='client',
            name='image',
            field=models.CharField(default='http://placehold.it/200x50', max_length=100, verbose_name='Ссылка на лого фирмы-клиента'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название фирмы-клиента'),
        ),
        migrations.AlterField(
            model_name='client',
            name='ref',
            field=models.CharField(default='/', max_length=50, verbose_name='Ссылка на сайт фирмы-клиента'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 9, 12, 20, 59, 24, 981747, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments_text',
            field=models.TextField(verbose_name='Текст комментария'),
        ),
        migrations.AlterField(
            model_name='direction',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2016, 9, 12, 20, 59, 24, 974053, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='direction',
            name='image',
            field=models.CharField(default='http://placehold.it/500x500', max_length=100, verbose_name='Ссылка на картинку'),
        ),
        migrations.AlterField(
            model_name='direction',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Название направления'),
        ),
        migrations.AlterField(
            model_name='direction',
            name='ref_video',
            field=models.CharField(default='https://youtube.com/', max_length=100, verbose_name='Ссылка на видео на youtube.com'),
        ),
        migrations.AlterField(
            model_name='direction',
            name='text',
            field=models.TextField(verbose_name='Описание курса'),
        ),
        migrations.AlterField(
            model_name='header',
            name='image',
            field=models.CharField(default='http://placehold.it/64x64', max_length=100, verbose_name='Иконка'),
        ),
        migrations.AlterField(
            model_name='header',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='header',
            name='text',
            field=models.TextField(verbose_name='Текст заголовка'),
        ),
        migrations.AlterField(
            model_name='lector',
            name='image',
            field=models.CharField(default='http://placehold.it/250x250', max_length=100, verbose_name='Ссылка на картинку'),
        ),
        migrations.AlterField(
            model_name='lector',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Имя лектора'),
        ),
        migrations.AlterField(
            model_name='lector',
            name='rang',
            field=models.TextField(verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='lector',
            name='surname',
            field=models.CharField(max_length=30, verbose_name='Фамилия лектора'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 9, 12, 20, 59, 24, 980840, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_text',
            field=models.TextField(verbose_name='Текст новости'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_title',
            field=models.CharField(max_length=30, verbose_name='Заголовок'),
        ),
    ]
