# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Max 250 characters', max_length=250)),
                ('slug', models.SlugField(help_text=b'Suggested value automatically generated from title.', unique=True)),
                ('description', models.TextField(help_text=b'Optional description for the cagegory', blank=True)),
            ],
            options={
                'ordering': ('slug',),
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'Max 250 characters', max_length=250)),
                ('slug', models.SlugField(help_text=b'Suggested value automatically generated from title. Must be unique for publish date.', unique_for_date=b'publish_date')),
                ('excerpt', models.TextField(help_text=b'A short summary. Optional', blank=True)),
                ('content', models.TextField()),
                ('publish_date', models.DateTimeField(default=datetime.datetime.now, db_index=True)),
                ('is_featured', models.BooleanField(default=False, help_text=b'Lets you feature a blog post. Typically the most recent featured blog post will show up different', db_index=True)),
                ('status', models.IntegerField(default=1, help_text=b"Only entries with 'Published' status are publicly displayed", db_index=True, choices=[(0, b'Published'), (1, b'Draft')])),
                ('thumbnail', filebrowser.fields.FileBrowseField(help_text=b'An optional thumbnail for the listing page', max_length=200, blank=True)),
                ('categories', models.ManyToManyField(help_text=b'The categories for the Blog Post', related_name='posts', to='blog.Category', blank=True)),
            ],
            options={
                'ordering': ('is_featured', '-publish_date', 'slug'),
                'verbose_name': 'Blog Post',
                'verbose_name_plural': 'Blog Posts',
            },
        ),
    ]
