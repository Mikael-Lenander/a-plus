# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-12 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0037_auto_20180108_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinstance',
            name='language',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]