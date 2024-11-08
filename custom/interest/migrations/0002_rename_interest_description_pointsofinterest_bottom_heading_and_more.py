# Generated by Django 5.1.2 on 2024-11-08 05:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("interest", "0001_initial"),
        ("wagtailcore", "0094_alter_page_locale"),
        ("wagtailimages", "0026_delete_uploadedimage"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pointsofinterest",
            old_name="interest_description",
            new_name="bottom_heading",
        ),
        migrations.RenameField(
            model_name="pointsofinterest",
            old_name="interest_image",
            new_name="bottom_image_one",
        ),
        migrations.RemoveField(
            model_name="pointsofinterest",
            name="interest_heading",
        ),
        migrations.AddField(
            model_name="pointsofinterest",
            name="bottom_button_text",
            field=models.TextField(blank=True, default="Contact us", null=True),
        ),
        migrations.AddField(
            model_name="pointsofinterest",
            name="bottom_image_two",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
        migrations.AddField(
            model_name="pointsofinterest",
            name="bottom_link_page",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
            ),
        ),
        migrations.AlterField(
            model_name="pointsofinterest",
            name="text",
            field=models.TextField(
                blank=True, default="Drop the pin to see location", null=True
            ),
        ),
    ]
