# Generated by Django 5.1 on 2024-10-31 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("conferenceApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="role",
            name="role",
            field=models.CharField(
                choices=[("USER", "USER"), ("ADMIN", "ADMIN"), ("GEST", "GEST")],
                max_length=5,
                unique=True,
            ),
        ),
    ]
