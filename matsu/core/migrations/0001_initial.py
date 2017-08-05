# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-05 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('tree_path', models.SlugField(max_length=255, verbose_name='Tree path')),
                ('content', models.TextField(blank=True, verbose_name='Content')),
            ],
        ),
    ]
