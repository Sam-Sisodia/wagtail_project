# Generated by Django 5.1.2 on 2024-11-14 03:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("conf", "0009_alter_navigationsettings_footer"),
    ]

    operations = [
        migrations.AddField(
            model_name="navigationsettings",
            name="office_address",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="navigationsettings",
            name="phone_number",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
