# Generated by Django 5.1.2 on 2024-11-06 10:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("elections", "0007_electionspage_sub_heading_two"),
    ]

    operations = [
        migrations.RenameField(
            model_name="electionspage",
            old_name="party_name",
            new_name="page_name",
        ),
    ]
