# Generated by Django 4.1.3 on 2022-12-24 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0003_alter_product_lowersubcategory"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="producttype",
            options={"ordering": ["id"]},
        ),
    ]
