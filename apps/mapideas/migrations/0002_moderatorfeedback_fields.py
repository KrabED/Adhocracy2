# Generated by Django 3.2.16 on 2023-01-31 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("a4_candy_mapideas", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="mapidea",
            old_name="moderator_statement",
            new_name="moderator_feedback_text",
        ),
        migrations.RenameField(
            model_name="mapidea",
            old_name="moderator_feedback",
            new_name="moderator_status",
        ),
    ]
