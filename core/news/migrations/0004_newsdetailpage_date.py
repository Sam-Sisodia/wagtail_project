# Generated by Django 5.1.2 on 2024-11-06 03:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0003_alter_newsdetailpage_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="newsdetailpage",
            name="date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
