# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarea', '0002_auto_20170830_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='fecha_terminado',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]