# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-21 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0003_auto_20180921_0913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentinfo',
            name='group',
        ),
        migrations.AddField(
            model_name='documentinfogroup',
            name='questions',
            field=models.ManyToManyField(to='legal.DocumentInfo'),
        ),
    ]
