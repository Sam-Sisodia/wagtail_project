# Generated by Django 5.1.2 on 2024-10-30 14:06

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("history", "0002_alter_historypage_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historypage",
            name="body",
            field=wagtail.fields.StreamField(
                [("button", 4)],
                blank=True,
                block_lookup={
                    0: ("wagtail.blocks.CharBlock", (), {}),
                    1: (
                        "wagtail.blocks.ChoiceBlock",
                        [],
                        {
                            "choices": [
                                ("btn-dark", "Dark"),
                                ("btn-light", "Light"),
                                ("btn-link", "Link"),
                                ("btn-primary", "Primary"),
                                ("btn-secondary", "Secondary"),
                            ]
                        },
                    ),
                    2: ("wagtail.blocks.PageChooserBlock", (), {"required": False}),
                    3: (
                        "wagtail.blocks.URLBlock",
                        (),
                        {"label": "URL", "required": False},
                    ),
                    4: (
                        "wagtail.blocks.StructBlock",
                        [[("text", 0), ("type", 1), ("page", 2), ("url", 3)]],
                        {},
                    ),
                },
            ),
        ),
    ]
