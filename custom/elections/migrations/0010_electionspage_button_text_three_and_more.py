# Generated by Django 5.1.2 on 2024-11-07 03:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("elections", "0009_electionpageperson_re_election_designation"),
        ("wagtailcore", "0094_alter_page_locale"),
    ]

    operations = [
        migrations.AddField(
            model_name="electionspage",
            name="button_text_three",
            field=models.TextField(blank=True, default="Get on Ballot", null=True),
        ),
        migrations.AddField(
            model_name="electionspage",
            name="link_page_three",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
            ),
        ),
        migrations.AlterField(
            model_name="electionspage",
            name="button_text_two",
            field=models.TextField(blank=True, default="Run for Position", null=True),
        ),
    ]
