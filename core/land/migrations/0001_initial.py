# Generated by Django 5.1.2 on 2024-11-11 05:13

import django.db.models.deletion
import modelcluster.fields
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0094_alter_page_locale"),
        ("wagtailimages", "0026_delete_uploadedimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="LandPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
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
                            2: (
                                "wagtail.blocks.PageChooserBlock",
                                (),
                                {"required": False},
                            ),
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
                ("heading", models.TextField(blank=True, null=True)),
                ("button_text", models.TextField(blank=True, null=True)),
                (
                    "cover_image",
                    models.ForeignKey(
                        blank=True,
                        help_text="Cover image for this page, used in listings and at the top of the page",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
                (
                    "link_page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "verbose_name": "Lands Index Page",
                "verbose_name_plural": "Lands  Index Pages",
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="LandSpot",
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
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                ("title", models.CharField(blank=True, max_length=50, null=True)),
                ("heading", models.TextField(blank=True, null=True)),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="land_spot_info",
                        to="land.landpage",
                    ),
                ),
            ],
            options={
                "verbose_name": "Land Spot Slide",
                "verbose_name_plural": "Land Spots Slides",
            },
        ),
        migrations.CreateModel(
            name="Spotfeature",
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
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                ("list_text", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="land_spot_feature",
                        to="land.landpage",
                    ),
                ),
            ],
            options={
                "verbose_name": "Spot feature",
                "verbose_name_plural": "Spot features",
            },
        ),
    ]
