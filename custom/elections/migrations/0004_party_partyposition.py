# Generated by Django 5.1.2 on 2024-11-04 11:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("elections", "0003_singleelectionpage_from_address_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Party",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("party_name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="PartyPosition",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("party_position", models.CharField(max_length=20)),
            ],
        ),
    ]
