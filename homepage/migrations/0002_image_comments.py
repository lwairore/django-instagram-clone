# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-23 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='comments',
            field=models.CharField(default='Not comments yet', max_length=1000),
        ),
    ]
