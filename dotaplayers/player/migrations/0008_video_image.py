# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-19 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0007_auto_20160515_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.ImageField(default='', upload_to='videocover'),
        ),
    ]