# Generated by Django 3.2.13 on 2022-06-02 06:24

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('a4_candy_cms_settings', '0006_add_helptexts_to_organisation_pages'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisationsettings',
            name='support_contact',
            field=wagtail.core.fields.StreamField([('email', wagtail.core.blocks.EmailBlock(help_text='The email is published in captcha helptext and other areas where assistance maybe required'))], blank=True),
        ),
    ]
