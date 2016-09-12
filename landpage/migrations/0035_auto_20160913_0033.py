# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-12 19:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0034_auto_20160913_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comments_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 9, 12, 19, 33, 30, 77027, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='direction',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2016, 9, 12, 19, 33, 30, 69602, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 9, 12, 19, 33, 30, 76326, tzinfo=utc)),
        ),
    ]
