# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-13 12:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='p2_telephone',
        ),
    ]
