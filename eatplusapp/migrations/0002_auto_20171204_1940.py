# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-04 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eatplusapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='eatplusapp/image/item/'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(blank=True, upload_to='eatplusapp/image/restaurant/'),
        ),
    ]