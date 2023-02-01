# Generated by Django 3.0.6 on 2020-05-16 10:25

import django.contrib.postgres.fields.jsonb
import django.db.models.deletion
from django.db import migrations, models

import venueless.core.models.room
import venueless.core.models.world
import venueless.core.utils.json


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_auto_20200430_2018"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="room",
            options={"ordering": ("sorting_priority", "name")},
        ),
        migrations.RemoveField(
            model_name="room",
            name="permission_config",
        ),
        migrations.RemoveField(
            model_name="world",
            name="permission_config",
        ),
        migrations.AddField(
            model_name="room",
            name="trait_grants",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True, default=venueless.core.models.room.default_grants, null=True
            ),
        ),
        migrations.AddField(
            model_name="world",
            name="roles",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True,
                default=venueless.core.models.world.default_roles,
                encoder=venueless.core.utils.json.CustomJSONEncoder,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="world",
            name="trait_grants",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True,
                default=venueless.core.models.world.default_grants,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="channel",
            name="room",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="channel",
                to="core.Room",
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="module_config",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                default=venueless.core.models.room.empty_module_config, null=True
            ),
        ),
        migrations.CreateModel(
            name="WorldGrant",
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
                ("role", models.CharField(max_length=200)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="world_grants",
                        to="core.User",
                    ),
                ),
                (
                    "world",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="world_grants",
                        to="core.World",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RoomGrant",
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
                ("role", models.CharField(max_length=200)),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="role_grants",
                        to="core.Room",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="room_grants",
                        to="core.User",
                    ),
                ),
                (
                    "world",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="room_grants",
                        to="core.World",
                    ),
                ),
            ],
        ),
    ]
