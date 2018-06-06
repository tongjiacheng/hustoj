# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-04-16 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0008_resource_classname'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassName',
            fields=[
                ('name', models.CharField(max_length=30, verbose_name='课程名称')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'class_name',
                'verbose_name': '课程名称',
                'verbose_name_plural': '课程名称',
            },
        ),
        migrations.RemoveField(
            model_name='resource',
            name='classname',
        ),
    ]