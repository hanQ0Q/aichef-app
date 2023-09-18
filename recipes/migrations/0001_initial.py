# Generated by Django 4.2.5 on 2023-09-18 21:28

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Equipment",
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
                    "equipment_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("ST", "Stove"),
                            ("OV", "Oven"),
                            ("MW", "Microwave"),
                            ("ST", "Stove"),
                            ("BL", "Blender"),
                            ("SE", "Steamer"),
                        ],
                        max_length=100,
                        null=True,
                        verbose_name="name",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Recipe",
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
                    "name",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="name"
                    ),
                ),
                (
                    "recipe_date",
                    models.DateField(blank=True, null=True, verbose_name="date"),
                ),
                (
                    "calorie",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="calorie"
                    ),
                ),
                (
                    "protein",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="protein"
                    ),
                ),
                (
                    "meal_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("BR", "breakfast"),
                            ("LC", "lunch"),
                            ("DN", "dinner"),
                        ],
                        max_length=4,
                        null=True,
                        verbose_name="meal type",
                    ),
                ),
                (
                    "instruction",
                    models.TextField(blank=True, null=True, verbose_name="instruction"),
                ),
            ],
        ),
    ]
