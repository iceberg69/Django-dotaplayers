# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-21 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0011_auto_20160521_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='home_display',
            field=models.BooleanField(default=False, verbose_name='首页显示'),
        ),
        migrations.AddField(
            model_name='player',
            name='home_display',
            field=models.BooleanField(default=False, verbose_name='首页显示'),
        ),
        migrations.AddField(
            model_name='video',
            name='home_display',
            field=models.BooleanField(default=False, verbose_name='首页显示'),
        ),
    ]