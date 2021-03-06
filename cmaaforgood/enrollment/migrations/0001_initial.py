# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-13 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p1_firstname', models.CharField(max_length=45)),
                ('p1_lastname', models.CharField(max_length=45)),
                ('p2_firstname', models.CharField(max_length=45)),
                ('p2_lastname', models.CharField(max_length=45)),
                ('p1_telephone', models.CharField(max_length=45)),
                ('p2_telephone', models.CharField(max_length=45)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='parent',
            unique_together=set([('p1_firstname', 'p1_lastname', 'p1_telephone')]),
        ),
    ]
