# Generated by Django 5.1 on 2024-11-02 00:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("conferenceApp", "0008_remove_session_intervenant_session_intervenant"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="session",
            name="intervenant",
        ),
        migrations.AddField(
            model_name="session",
            name="intervenants",
            field=models.ManyToManyField(
                related_name="sessions", to="conferenceApp.user1"
            ),
        ),
        migrations.AlterField(
            model_name="session",
            name="conference",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="conference",
                to="conferenceApp.conference",
            ),
        ),
    ]
