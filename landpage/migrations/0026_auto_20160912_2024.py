# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-12 15:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0025_auto_20160912_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approve',
            name='ref',
            field=models.CharField(default='http://placehold.it/100x100', max_length=100, verbose_name='Ссылка на изображение'),
        ),
        migrations.AlterField(
            model_name='direction',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2016, 9, 12, 15, 24, 48, 710770, tzinfo=utc)),
        ),
    ]
