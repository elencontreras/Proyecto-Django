# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarea', '0005_auto_20170902_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='descripcion',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
    ]