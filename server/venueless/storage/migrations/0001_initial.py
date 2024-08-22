# Generated by Django 3.0.6 on 2020-07-04 10:58

import uuid

import django.db.models.deletion
from django.db import migrations, models

import venueless.storage.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("core", "0013_remove_world_about"),
    ]

    operations = [
        migrations.CreateModel(
            name="StoredFile",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("expires", models.DateTimeField(blank=True, null=True)),
                ("date", models.DateTimeField(blank=True, null=True)),
                ("filename", models.CharField(max_length=255)),
                ("type", models.CharField(max_length=255)),
                (
                    "file",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=venueless.storage.models.storedfile_name,
                    ),
                ),
                ("public", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="core.User",
                    ),
                ),
                (
                    "world",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="core.World",
                    ),
                ),
            ],
        ),
    ]
