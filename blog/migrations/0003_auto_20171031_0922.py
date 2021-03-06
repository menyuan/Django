# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 01:22
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171030_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='home_display',
            field=models.BooleanField(default=False, verbose_name='\u9996\u9875\u663e\u793a'),
        ),
        migrations.AddField(
            model_name='column',
            name='nav_display',
            field=models.BooleanField(default=False, verbose_name='\u5bfc\u822a\u663e\u793a'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='\u5185\u5bb9'),
        ),

    ]
