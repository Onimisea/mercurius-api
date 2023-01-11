# Generated by Django 4.1.3 on 2023-01-11 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                    "house_no",
                    models.CharField(max_length=5, verbose_name="House Number"),
                ),
                (
                    "street_name",
                    models.CharField(
                        max_length=500, verbose_name="Street Name"
                    ),
                ),
                (
                    "bus_stop",
                    models.CharField(
                        max_length=60, verbose_name="Nearest Bus Stop"
                    ),
                ),
                ("lga", models.CharField(max_length=60, verbose_name="LGA")),
                (
                    "postal_code",
                    models.IntegerField(
                        blank=True,
                        default=0,
                        null=True,
                        verbose_name="LGA Postal Code",
                    ),
                ),
                (
                    "state",
                    models.CharField(max_length=60, verbose_name="State"),
                ),
                (
                    "country",
                    models.CharField(
                        default="Nigeria", max_length=60, verbose_name="Country"
                    ),
                ),
                ("is_default", models.BooleanField(default=False)),
                ("added_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Address",
                "verbose_name_plural": "Addresses",
                "ordering": ["-added_on"],
            },
        ),
    ]
