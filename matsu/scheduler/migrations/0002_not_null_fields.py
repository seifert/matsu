# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-02 12:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='repeat',
            field=models.IntegerField(choices=[(1, 'Do not repeat'), (2, 'Daily'), (3, 'Weekly'), (4, 'Bi-weekly'), (5, 'Monthly'), (6, 'Yearly')], default=1, verbose_name='Repeat'),
        ),
        migrations.AlterField(
            model_name='event',
            name='stop',
            field=models.TimeField(default=datetime.time(23, 59, 59, 999999), verbose_name='Stop'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='valid_until',
            field=models.DateField(db_index=True, default=datetime.date(9999, 12, 31), verbose_name='Valid until'),
            preserve_default=False,
        ),
    ]
