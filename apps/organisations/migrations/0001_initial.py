# Generated by Django 2.2.6 on 2019-10-24 13:07

import adhocracy4.images.fields
import autoslug.fields
import ckeditor.fields
import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('name', models.CharField(max_length=512)),
                ('title', models.CharField(default='Organisation', help_text='The title of your organisation will be shown on the landing page. max. 100 characters', max_length=100, verbose_name='Title of your organisation')),
                ('description', models.CharField(help_text='The description will be displayed on the landing page. max. 400 characters', max_length=400, verbose_name='Short description of your organisation')),
                ('logo', adhocracy4.images.fields.ConfiguredImageField('logo', blank=True, help_text='The Logo representing your organisation. The image must be square and it should be min. 200 pixels wide and 200 pixels tall. Allowed file formats are png, jpeg, gif. The file size should be max. 5 MB.', upload_to='organisations/logos', verbose_name='Logo')),
                ('slogan', models.CharField(blank=True, help_text='The slogan will be shown below the title of your organisation on the landing page. The slogan can provide context or additional information to the title. max. 200 characters', max_length=200, verbose_name='Slogan')),
                ('image', adhocracy4.images.fields.ConfiguredImageField('heroimage', blank=True, help_prefix='The image will be shown as a decorative background image.', upload_to='organisations/backgrounds', verbose_name='Header image')),
                ('information', ckeditor_uploader.fields.RichTextUploadingField(blank=True, help_text='You can provide general information about your participation platform to your visitors. It’s also helpful to name a general person of contact for inquiries. The information will be shown on a separate page that can be reached via the main menu.', verbose_name='Information about your organisation')),
                ('imprint', ckeditor.fields.RichTextField(help_text='Please provide all the legally required information of your imprint. The imprint will be shown on a separate page.', verbose_name='Imprint')),
                ('is_supporting', models.BooleanField(default=False, help_text='For supporting organisations, the banner asking for donations is not displayed on their pages.', verbose_name='is a supporting organisation')),
                ('initiators', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
