# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-10 16:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180210_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='regTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 10, 16, 31, 2, 268444, tzinfo=utc)),
        ),
    ]