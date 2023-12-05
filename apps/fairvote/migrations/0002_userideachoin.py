# Generated by Django 3.2.19 on 2023-11-24 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("a4_candy_ideas", "0002_rename_moderatorfeedback_fields"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("a4_candy_fairvote", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserIdeaChoin",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "choins",
                    models.FloatField(blank=True, default=0, verbose_name="Choins"),
                ),
                (
                    "idea",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="a4_candy_ideas.idea",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "idea")},
                "index_together": {("user", "idea")},
            },
        ),
    ]
