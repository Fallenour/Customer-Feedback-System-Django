# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-08 16:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0008_auto_20170608_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2017, 6, 8, 16, 52, 40, 922040, tzinfo=utc)),
        ),
    ]