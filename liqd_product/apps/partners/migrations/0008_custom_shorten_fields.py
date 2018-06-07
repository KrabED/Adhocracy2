# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-06 13:18
from __future__ import unicode_literals

from django.db import migrations


def shorten_fields(apps, schema_editor):
    Partner = apps.get_model("liqd_product_partners", "Partner")
    for partner in Partner.objects.all():
        partner.name = partner.name[0:100]
        partner.title = partner.title[0:100]
        partner.description = partner.description[0:400]
        partner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('liqd_product_partners', '0007_partner_title'),
    ]

    operations = [
        migrations.RunPython(shorten_fields)
    ]
