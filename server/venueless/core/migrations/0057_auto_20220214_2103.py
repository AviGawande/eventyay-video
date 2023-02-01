# Generated by Django 3.2.11 on 2022-02-14 20:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0056_announcement"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="announcement",
            name="is_active",
        ),
        migrations.AddField(
            model_name="announcement",
            name="state",
            field=models.CharField(
                choices=[
                    ("draft", "Draft"),
                    ("active", "Active"),
                    ("archived", "Archived"),
                ],
                default="draft",
                max_length=8,
            ),
        ),
    ]
