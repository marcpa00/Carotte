# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-12-06 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20181206_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='brand',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='specie',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
