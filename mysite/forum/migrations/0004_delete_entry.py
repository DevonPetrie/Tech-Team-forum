# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 17:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20171210_1719'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
