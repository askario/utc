# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-11 20:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0008_auto_20160912_0110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя лектора')),
                ('surname', models.CharField(max_length=30, verbose_name='Фамилия лектора')),
                ('rang', models.TextField()),
            ],
            options={
                'verbose_name': 'Лектор',
                'db_table': 'lectors',
                'verbose_name_plural': 'Лекторы',
            },
        ),
        migrations.AlterField(
            model_name='direction',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2016, 9, 11, 20, 22, 41, 255731, tzinfo=utc)),
        ),
    ]
