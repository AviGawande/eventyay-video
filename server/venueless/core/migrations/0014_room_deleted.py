# Generated by Django 3.0.6 on 2020-07-05 10:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0013_remove_world_about"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="deleted",
            field=models.BooleanField(default=False),
        ),
    ]
