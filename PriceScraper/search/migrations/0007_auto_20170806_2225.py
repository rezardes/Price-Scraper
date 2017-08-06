# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-06 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_auto_20170806_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='LProduk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('price', models.IntegerField(default=0)),
                ('imageURL', models.URLField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Produk',
            new_name='BProduk',
        ),
    ]