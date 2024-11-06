# Generated by Django 5.1.2 on 2024-11-06 04:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0006_remove_homepage_read_page_text_and_more"),
    ]

    operations = [
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
            name="upcoming_event_button_text",
            field=models.TextField(blank=True, default="More Events", null=True),
        ),
    ]
