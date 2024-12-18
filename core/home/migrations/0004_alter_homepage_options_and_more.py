# Generated by Django 5.1.2 on 2024-11-12 03:28

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_alter_homepagelinks_options_homepage_history_heading_and_more"),
        ("wagtailimages", "0026_delete_uploadedimage"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="homepage",
            options={"verbose_name": "Home Page", "verbose_name_plural": "Home Pages"},
        ),
        migrations.RenameField(
            model_name="homepage",
            old_name="home_image",
            new_name="hero_section_image",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="history_page_text",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="read_page_text",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="team_page_text",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="upcoming_event_text",
        ),
        migrations.AddField(
            model_name="homepage",
            name="event_heading",
            field=models.CharField(
                blank=True, default="Upcoming Events", max_length=200, null=True
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="history_bg_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="history_page_button_text",
            field=models.CharField(
                blank=True, default="Get the History", max_length=200, null=True
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="img_gallery",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="news_button_text",
            field=models.CharField(
                blank=True, default="Read more", max_length=200, null=True
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="news_heading",
            field=models.CharField(
                blank=True, default="Latest News", max_length=200, null=True
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="park_bgimage",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="team_page_button_text",
            field=models.CharField(
                blank=True, default="See Officials", max_length=200, null=True
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="upcoming_event_button_text",
            field=models.TextField(blank=True, default="More Events", null=True),
        ),
        migrations.CreateModel(
            name="HeroImages",
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
                        related_name="home_hero_images",
                        to="home.homepage",
                    ),
                ),
            ],
            options={
                "verbose_name": "Hero Image",
                "verbose_name_plural": "Hero Images",
            },
        ),
        migrations.CreateModel(
            name="ParksList",
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
                ("text", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="home_parks",
                        to="home.homepage",
                    ),
                ),
            ],
            options={
                "verbose_name": "Park List",
                "verbose_name_plural": "Parks List",
            },
        ),
    ]
