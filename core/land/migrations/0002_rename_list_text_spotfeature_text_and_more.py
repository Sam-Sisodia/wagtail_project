# Generated by Django 5.1.2 on 2024-11-11 05:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("land", "0001_initial"),
        ("wagtailimages", "0026_delete_uploadedimage"),
    ]

    operations = [
        migrations.RenameField(
            model_name="spotfeature",
            old_name="list_text",
            new_name="text",
        ),
        migrations.RemoveField(
            model_name="landspot",
            name="heading",
        ),
        migrations.AddField(
            model_name="spotfeature",
            name="image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
        migrations.AlterField(
            model_name="landpage",
            name="button_text",
            field=models.TextField(blank=True, default="Get Assistance", null=True),
        ),
    ]
