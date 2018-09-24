# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('sub_heading', models.CharField(help_text=b'An optional sub heading / short teaser', max_length=250, blank=True)),
                ('image', filebrowser.fields.FileBrowseField(help_text=b'Banner image. This will be cropped to fit the size needed for the banner group', max_length=200)),
                ('url', models.CharField(help_text=b'Optional URL that the banner can link to', max_length=250, blank=True)),
                ('url_name', models.CharField(help_text=b'Optional display text to be used for the link. May not be used in all banner groups.', max_length=50, blank=True)),
                ('display_order', models.PositiveIntegerField(default=1, help_text=b'Controls the order that banners are displayed', db_index=True)),
            ],
            options={
                'ordering': ('display_order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BannerGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(help_text=b'Unique Identifier for a group of banners', unique=True)),
                ('description', models.TextField(help_text=b'Optional description to know what this group is used for', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='banner',
            name='groups',
            field=models.ManyToManyField(help_text=b'The groups that this banner belongs to. This decides where a banner shows up  on the site and how it is displayed.', to='promotions.BannerGroup', null=True, blank=True),
            preserve_default=True,
        ),
    ]
