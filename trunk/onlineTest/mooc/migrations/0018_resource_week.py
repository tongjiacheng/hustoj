# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-04-18 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0017_auto_20180417_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='week',
            field=models.ManyToManyField(to='mooc.Week', verbose_name='所属周次'),
        ),
    ]
