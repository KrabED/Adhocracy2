# Generated by Django 3.2.16 on 2023-01-31 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "a4_candy_moderatorfeedback",
            "0002_rename_moderatorstatement_moderatorfeedback",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="moderatorfeedback",
            old_name="statement",
            new_name="feedback_text",
        ),
    ]
