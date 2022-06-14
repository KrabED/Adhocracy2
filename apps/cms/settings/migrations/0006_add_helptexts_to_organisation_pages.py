# Generated by Django 2.2.17 on 2021-02-16 19:33

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('a4_candy_cms_settings', '0005_organisationsettings_platform_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organisationsettings',
            options={'verbose_name': 'Platform settings'},
        ),
        migrations.AlterField(
            model_name='organisationsettings',
            name='address',
            field=wagtail.fields.RichTextField(help_text='The address is published on the contact form.'),
        ),
        migrations.AlterField(
            model_name='organisationsettings',
            name='contacts',
            field=wagtail.fields.RichTextField(help_text='The contacts are published on the contact form.'),
        ),
        migrations.AlterField(
            model_name='organisationsettings',
            name='platform_name',
            field=models.CharField(default='adhocracy+', help_text='This name appears in the footer of all pages and e-mails as well as in the tab of the browser.', max_length=20, verbose_name='Platform name'),
        ),
    ]
