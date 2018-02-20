# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-04 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eatplusapp', '0002_auto_20171204_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='avatar',
        ),
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(default=None, upload_to='eatplusapp/image/item/'),
            preserve_default=False,
        ),
    ]