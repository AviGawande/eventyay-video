# Generated by Django 3.0.11 on 2020-11-09 12:32

import django.db.models.deletion
from django.db import migrations, models

import venueless.core.models.auth


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0033_exhibitor_highlighted_room"),
    ]

    operations = [
        migrations.CreateModel(
            name="ShortToken",
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
                ("expires", models.DateTimeField()),
                (
                    "short_token",
                    models.CharField(
                        db_index=True,
                        default=venueless.core.models.auth.generate_short_token,
                        max_length=150,
                        unique=True,
                    ),
                ),
                ("long_token", models.TextField()),
                (
                    "world",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="short_tokens",
                        to="core.World",
                    ),
                ),
            ],
        ),
    ]
