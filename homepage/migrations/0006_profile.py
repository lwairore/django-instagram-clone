# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-23 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20190623_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default='/home/karangu/Desktop/Instagram\\ clone/media', upload_to='profile_pictures/')),
                ('bio', models.TextField()),
                ('user_id', models.IntegerField(default=0)),
            ],
        ),
    ]
