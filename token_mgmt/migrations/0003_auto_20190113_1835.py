# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-01-13 23:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('token_mgmt', '0002_auto_20190113_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification_token',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 13, 18, 35, 16, 640000)),
        ),
        migrations.AlterField(
            model_name='verification_token',
            name='utilized_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]