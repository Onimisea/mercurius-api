# Generated by Django 4.1.3 on 2022-12-19 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0009_alter_product_attribute_value"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="attribute_value",
            field=models.ManyToManyField(
                blank=True,
                related_name="product_attribute_value",
                to="inventory.productattributevalue",
                verbose_name="Product Attribute Values",
            ),
        ),
    ]
