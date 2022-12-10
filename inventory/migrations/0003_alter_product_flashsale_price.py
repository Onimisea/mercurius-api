# Generated by Django 4.1.3 on 2022-12-06 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0002_alter_productattribute_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="flashsale_price",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="format: flashsale price of product",
                max_digits=12,
                null=True,
                verbose_name="Flashsale Price",
            ),
        ),
    ]
