# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-11 20:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direction',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 9, 12, 1, 5, 41, 961464)),
        ),
    ]
