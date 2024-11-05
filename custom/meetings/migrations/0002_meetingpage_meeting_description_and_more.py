# Generated by Django 5.1.2 on 2024-10-30 07:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meetings", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="meetingpage",
            name="meeting_description",
            field=models.TextField(
                blank=True, null=True, verbose_name="Enter meeting AGENDAn"
            ),
        ),
        migrations.AddField(
            model_name="meetingpage",
            name="meeting_end_time",
            field=models.TimeField(blank=True, null=True, verbose_name="End Time"),
        ),
        migrations.AddField(
            model_name="meetingpage",
            name="meeting_start_time",
            field=models.TimeField(blank=True, null=True, verbose_name="Start Time"),
        ),
        migrations.AlterField(
            model_name="meetingpage",
            name="meeting_date",
            field=models.DateField(blank=True, null=True, verbose_name="Meeting Date"),
        ),
    ]