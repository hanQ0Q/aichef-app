# Generated by Django 4.2.5 on 2023-09-23 03:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0003_alter_recipe_recipe_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="recipe_date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 9, 23, 3, 13, 29, 636496, tzinfo=datetime.timezone.utc
                ),
                verbose_name="date",
            ),
        ),
    ]