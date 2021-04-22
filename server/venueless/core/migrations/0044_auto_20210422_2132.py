# Generated by Django 3.1.5 on 2021-04-22 19:32

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0043_user_last_login"),
    ]

    operations = [
        migrations.AlterField(
            model_name="world",
            name="domain",
            field=models.CharField(
                blank=True,
                max_length=250,
                null=True,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(regex="^[a-z0-9-.:]+$")
                ],
            ),
        ),
        migrations.AlterField(
            model_name="world",
            name="id",
            field=models.CharField(
                max_length=50,
                primary_key=True,
                serialize=False,
                validators=[django.core.validators.RegexValidator(regex="^[a-z0-9]+$")],
            ),
        ),
        migrations.AlterField(
            model_name="world",
            name="locale",
            field=models.CharField(
                choices=[("en", "English"), ("de", "German")],
                default="en",
                max_length=100,
            ),
        ),
        migrations.CreateModel(
            name="PlannedUsage",
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
                ("start", models.DateField()),
                ("end", models.DateField()),
                ("attendees", models.PositiveIntegerField()),
                ("notes", models.TextField(blank=True)),
                (
                    "world",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="planned_usages",
                        to="core.world",
                    ),
                ),
            ],
        ),
    ]
