# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-06 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produk',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]
