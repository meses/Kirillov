# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecter', '0006_auto_20161222_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='capacity',
            field=models.CharField(db_index=True, max_length=30, verbose_name='Объём'),
        ),
    ]