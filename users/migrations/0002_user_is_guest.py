# Generated by Django 4.2.5 on 2023-10-07 20:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_guest",
            field=models.BooleanField(default=False, verbose_name="is guest"),
        ),
    ]
