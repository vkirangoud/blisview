# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-20 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0002_auto_20160418_2048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='graph',
            old_name='path',
            new_name='path_static',
        ),
        migrations.AddField(
            model_name='graph',
            name='path_template',
            field=models.FilePathField(default='graph/images/averaged_performance_chart.png'),
            preserve_default=False,
        ),
    ]
