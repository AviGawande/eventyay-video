# Generated by Django 3.0.5 on 2020-06-04 10:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0009_world_locale"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="moderation_state",
            field=models.CharField(
                choices=[("", "None"), ("silenced", "Silenced"), ("banned", "Banned")],
                default="",
                max_length=8,
            ),
        ),
    ]
