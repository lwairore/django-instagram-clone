# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-23 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='image_id',
            field=models.IntegerField(default=0),
        ),
    ]
