# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 08:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selecter', '0003_auto_20161222_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='capacity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='interface',
        ),
    ]