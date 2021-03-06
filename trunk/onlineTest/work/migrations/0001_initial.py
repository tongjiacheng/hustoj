# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-10-18 21:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('judge', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BanJi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40, verbose_name='班级名称')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('courser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='judge.ClassName')),
                ('students', models.ManyToManyField(related_name='banJi_students', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banJi_teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HomeWork',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
                ('problem_ids', models.CharField(max_length=200, verbose_name='编程题列表id列表')),
                ('choice_problem_ids', models.CharField(blank=True, max_length=200, null=True, verbose_name='选择题id列表')),
                ('gaicuo_problem_ids', models.CharField(max_length=200, null=True, verbose_name='改错题列表id列表')),
                ('tiankong_problem_ids', models.CharField(max_length=200, null=True, verbose_name='填空题列表id列表')),
                ('problem_info', models.TextField()),
                ('choice_problem_info', models.TextField()),
                ('tiankong_problem_info', models.TextField(null=True)),
                ('gaicuo_problem_info', models.TextField(null=True)),
                ('allowed_languages', models.CharField(max_length=50)),
                ('work_kind', models.CharField(default='作业', max_length=20, verbose_name='作业类型')),
                ('total_score', models.IntegerField()),
                ('courser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.ClassName', verbose_name='所属课程')),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
            ],
        ),
        migrations.CreateModel(
            name='HomeworkAnswer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('wrong_choice_problems', models.CharField(default='', max_length=200, verbose_name='错误的选择题')),
                ('wrong_choice_problems_info', models.CharField(default='', max_length=200, verbose_name='错误的选择题保留信息')),
                ('score', models.IntegerField(default=0, verbose_name='总成绩')),
                ('choice_problem_score', models.IntegerField(default=0, verbose_name='选择题成绩')),
                ('problem_score', models.IntegerField(default=0, verbose_name='编程题成绩')),
                ('tiankong_score', models.IntegerField(default=0, verbose_name='程序填空题成绩')),
                ('gaicuo_score', models.IntegerField(default=0, verbose_name='程序改错题成绩')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='答题时间')),
                ('judged', models.BooleanField(default=False, verbose_name='是否已经判分？')),
                ('summary', models.TextField(null=True, verbose_name='实验小结')),
                ('teacher_comment', models.TextField(null=True, verbose_name='教师评语')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='答题者')),
            ],
        ),
        migrations.CreateModel(
            name='MyHomework',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
                ('problem_ids', models.CharField(blank=True, max_length=200, null=True, verbose_name='编程题列表id列表')),
                ('choice_problem_ids', models.CharField(blank=True, max_length=200, null=True, verbose_name='选择题id列表')),
                ('gaicuo_problem_ids', models.CharField(max_length=200, null=True, verbose_name='改错题列表id列表')),
                ('tiankong_problem_ids', models.CharField(max_length=200, null=True, verbose_name='填空题列表id列表')),
                ('problem_info', models.TextField(blank=True, null=True)),
                ('choice_problem_info', models.TextField(blank=True, null=True)),
                ('gaicuo_problem_info', models.TextField(blank=True, null=True)),
                ('tiankong_problem_info', models.TextField(blank=True, null=True)),
                ('allowed_languages', models.CharField(max_length=50)),
                ('allow_resubmit', models.BooleanField(default=False, verbose_name='是否允许重复提交作业？')),
                ('work_kind', models.CharField(default='作业', max_length=20, verbose_name='作业类型')),
                ('total_score', models.IntegerField()),
                ('banji', models.ManyToManyField(to='work.BanJi')),
                ('courser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.ClassName', verbose_name='所属课程')),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('finished_students', models.ManyToManyField(blank=True, related_name='finished_students', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TempHomeworkAnswer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.TextField(null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.MyHomework')),
            ],
        ),
        migrations.AddField(
            model_name='homeworkanswer',
            name='homework',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='work.MyHomework', verbose_name='作业'),
        ),
    ]
