# Generated by Django 5.1.2 on 2024-11-14 03:54

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("conf", "0012_alter_navigationsettings_social_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="navigationsettings",
            name="social_link",
            field=wagtail.fields.StreamField(
                [("element", 2)],
                blank=True,
                block_lookup={
                    0: ("wagtail.blocks.CharBlock", (), {}),
                    1: (
                        "wagtail.blocks.URLBlock",
                        (),
                        {"label": "URL", "required": False},
                    ),
                    2: ("wagtail.blocks.StructBlock", [[("icon", 0), ("url", 1)]], {}),
                },
                null=True,
            ),
        ),
    ]