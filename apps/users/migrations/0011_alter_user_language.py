# Generated by Django 4.2.7 on 2024-08-21 10:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("a4_candy_users", "0010_alter_user_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="language",
            field=models.CharField(
                choices=[
                    ("en", "English"),
                    ("de", "German"),
                    ("nl", "Dutch"),
                    ("ky", "Kyrgyz"),
                    ("ru", "Russian"),
                    ("he", "Hebrew"),
                ],
                default="he",
                help_text="Specify your preferred language for the user interface and the notifications of the platform.",
                max_length=4,
                verbose_name="Your preferred language",
            ),
        ),
    ]
