# Generated by Django 5.1.1 on 2024-09-24 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("topshiriq1", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="phone",
            field=models.CharField(max_length=128),
        ),
    ]
