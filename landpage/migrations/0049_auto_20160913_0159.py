# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-12 20:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0048_auto_20160913_0159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comments_from',
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 9, 12, 20, 59, 55, 340015, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='direction',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2016, 9, 12, 20, 59, 55, 333567, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 9, 12, 20, 59, 55, 339326, tzinfo=utc)),
        ),
    ]