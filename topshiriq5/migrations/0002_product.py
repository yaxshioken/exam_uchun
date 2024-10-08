# Generated by Django 5.1.1 on 2024-09-24 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("topshiriq5", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("marja", models.DecimalField(decimal_places=2, max_digits=10)),
                ("package_code", models.CharField(max_length=255)),
            ],
        ),
    ]
