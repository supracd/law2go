# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='groups',
            field=models.ManyToManyField(help_text=b'The groups that this banner belongs to. This decides where a banner shows up  on the site and how it is displayed.', to='promotions.BannerGroup', blank=True),
        ),
    ]
