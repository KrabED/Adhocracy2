# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-02 11:44
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('a4_candy_cms_pages', '0007_rename_body_to_body_de'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body_en',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
