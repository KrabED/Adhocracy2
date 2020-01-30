# Generated by Django 2.2.9 on 2020-01-30 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a4_candy_organisations', '0005_organisation_short_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='facebook_handle',
            field=models.CharField(blank=True, max_length=100, verbose_name='Facebook handle'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='instagram_handle',
            field=models.CharField(blank=True, max_length=100, verbose_name='Instagram handle'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='twitter_handle',
            field=models.CharField(blank=True, max_length=100, verbose_name='Twitter handle'),
        ),
    ]
