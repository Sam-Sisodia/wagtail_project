# Generated by Django 5.1.2 on 2024-11-08 10:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("meetings", "0004_meetingspage"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="meetingspage",
            options={
                "verbose_name": "Meetings Page",
                "verbose_name_plural": "Meeting Pages",
            },
        ),
    ]