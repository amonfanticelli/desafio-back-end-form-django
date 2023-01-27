# Generated by Django 4.1.5 on 2023-01-24 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Form",
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
                ("Type", models.CharField(max_length=100)),
                ("Date", models.DateField(max_length=8)),
                ("Value", models.IntegerField(max_length=10)),
                ("CPF", models.CharField(max_length=11)),
                ("CreditCard", models.CharField(max_length=12)),
                ("Time", models.TimeField(max_length=6)),
                ("StoreOwner", models.CharField(max_length=14)),
                ("StoreName", models.CharField(max_length=19)),
            ],
        ),
    ]