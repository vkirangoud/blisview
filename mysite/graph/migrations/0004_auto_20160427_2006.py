# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-27 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0003_auto_20160420_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='options',
            name='votes',
        ),
        migrations.AddField(
            model_name='options',
            name='test_input',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
