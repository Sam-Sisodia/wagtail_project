# Generated by Django 5.1.2 on 2024-11-11 04:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "business",
            "0003_rename_growth_data_numbes_one_businesspage_growth_data_number_one_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="businesspage",
            name="button_text",
        ),
        migrations.RemoveField(
            model_name="businesspage",
            name="link_page",
        ),
        migrations.RemoveField(
            model_name="businesspage",
            name="location_heading",
        ),
        migrations.AlterField(
            model_name="businesspage",
            name="resource_heading",
            field=models.TextField(blank=True, default="Helpful Resources", null=True),
        ),
    ]