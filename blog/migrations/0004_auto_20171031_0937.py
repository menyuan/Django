# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171031_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(max_length=256, verbose_name='\u7f51\u5740'),
        ),
    ]
