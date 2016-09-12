# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-12 19:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0036_auto_20160913_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comments_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 9, 12, 19, 37, 41, 212607, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='direction',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2016, 9, 12, 19, 37, 41, 204732, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 9, 12, 19, 37, 41, 211523, tzinfo=utc)),
        ),
    ]
