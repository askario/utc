# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-11 20:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0010_auto_20160912_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direction',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2016, 9, 11, 20, 30, 10, 952958, tzinfo=utc)),
        ),
    ]