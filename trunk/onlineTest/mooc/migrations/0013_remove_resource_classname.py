# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-04-16 21:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0012_resource_classname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='classname',
        ),
    ]
