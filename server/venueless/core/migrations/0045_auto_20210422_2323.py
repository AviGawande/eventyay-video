# Generated by Django 3.1.8 on 2021-04-22 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0044_auto_20210422_2132"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="plannedusage",
            options={"ordering": ("start",)},
        ),
        migrations.AlterField(
            model_name="roomview",
            name="end",
            field=models.DateTimeField(db_index=True, null=True),
        ),
    ]
