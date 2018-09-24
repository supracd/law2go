# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sitetree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('relative_url', models.CharField(unique=True, max_length=250, editable=False, db_index=True)),
                ('display_order', models.PositiveIntegerField(default=1, help_text=b'Controls order that pages are displayed', db_index=True)),
                ('content', models.TextField(blank=True)),
                ('head_title', models.CharField(default=b'', help_text=b'Page Title for head. Max length 100 characters.', max_length=100, blank=True)),
                ('meta_description', models.CharField(default=b'', help_text=b'Page Meta Description Field. Max length 200 characters.', max_length=200, blank=True)),
                ('header_image', filebrowser.fields.FileBrowseField(help_text=b'Header image for the top of the page.', max_length=200, blank=True)),
                ('is_hidden', models.BooleanField(default=False, help_text=b"Hidden pages do not show up in search or have a valid URL. They are useful for grouping similar pages by a parent page you don't want vislbe on the site")),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('nav_menu', models.ForeignKey(blank=True, to='sitetree.Tree', help_text=b'An Optional navigation menu to display on this page.', null=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='pages.Page', null=True)),
            ],
            options={
                'ordering': ('lft',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Unique Name/ID for a template.', unique=True, max_length=100)),
                ('file_name', models.CharField(help_text=b'Full Path and file name of the template.', max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='page',
            name='template',
            field=models.ForeignKey(blank=True, to='pages.PageTemplate', help_text=b'The template used to display this page. If blank the default template is used.', null=True),
            preserve_default=True,
        ),
    ]
