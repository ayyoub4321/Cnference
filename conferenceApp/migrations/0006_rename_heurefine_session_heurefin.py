# Generated by Django 5.1 on 2024-11-01 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("conferenceApp", "0005_remove_conference_session_session_conference"),
    ]

    operations = [
        migrations.RenameField(
            model_name="session",
            old_name="heureFine",
            new_name="heureFin",
        ),
    ]
