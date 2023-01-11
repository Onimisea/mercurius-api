# Generated by Django 4.1.3 on 2023-01-11 11:55

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                        help_text="format: required, max_length=100",
                        max_length=100,
                        unique=True,
                        verbose_name="Category Name",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="format: required, letters, numbers, underscore, or hyphens",
                        max_length=100,
                        unique=True,
                        verbose_name="Category URL",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="format: optional",
                        null=True,
                        verbose_name="Category Description",
                    ),
                ),
                (
                    "category_image",
                    cloudinary.models.CloudinaryField(
                        max_length=255, verbose_name="Category Banner Image"
                    ),
                ),
                (
                    "category_nav_image",
                    cloudinary.models.CloudinaryField(
                        default="",
                        max_length=255,
                        verbose_name="Category Nav Image",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="FlashsaleCtrl",
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
                        help_text="format: required, max_length-100",
                        max_length=100,
                        verbose_name="Flashsale Name",
                    ),
                ),
                ("when", models.DateTimeField()),
                (
                    "is_active",
                    models.BooleanField(
                        default=False,
                        help_text="format: default=false, true = flashsale is active",
                        verbose_name="Active Flashsale",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LowerSubcategory",
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
                        help_text="format: required, max_length=100",
                        max_length=100,
                        verbose_name="Lower Subcategory Name",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="format: required, letters, numbers, underscore, or hyphens",
                        max_length=100,
                        verbose_name="Lower Subcategory URL",
                    ),
                ),
                (
                    "lowersubcategory_icon",
                    cloudinary.models.CloudinaryField(
                        default="",
                        max_length=255,
                        verbose_name="Lower Subcategory Icon",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Lower Subcategory",
                "verbose_name_plural": "Lower Subcategories",
                "ordering": ["created_at"],
            },
        ),
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
                (
                    "name",
                    models.CharField(
                        help_text="format: required, max=100",
                        max_length=255,
                        verbose_name="Product Name",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="format: required, letters, numbers, underscore, or hyphens",
                        max_length=255,
                        unique=True,
                        verbose_name="Product URL",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="format: required",
                        null=True,
                        verbose_name="Product Description",
                    ),
                ),
                (
                    "flashsale",
                    models.IntegerField(
                        default=0,
                        help_text="format: how many percent off the  regular price of product",
                        verbose_name="Percentage Off",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        help_text="format: regular price of product",
                        verbose_name="Regular Price",
                    ),
                ),
                (
                    "weight",
                    models.FloatField(
                        blank=True,
                        help_text="Weight in Kilogram (Kg)",
                        null=True,
                        verbose_name="Product Weight",
                    ),
                ),
                (
                    "is_onFlashsale",
                    models.BooleanField(
                        default=False,
                        help_text="format: true = product is on flashsale",
                        verbose_name="Flashsale",
                    ),
                ),
                (
                    "in_stock",
                    models.BooleanField(
                        default=True,
                        help_text="format: true = product is available",
                        verbose_name="product availability",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=False,
                        help_text="format: true = product visible",
                        verbose_name="Product Visibility",
                    ),
                ),
                (
                    "added_on",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="Date product was added",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="Date product was last updated",
                    ),
                ),
                (
                    "meta_keywords",
                    models.CharField(
                        blank=True,
                        help_text="SEO Keywords separated by comma",
                        max_length=255,
                        null=True,
                        verbose_name="SEO Keywords",
                    ),
                ),
                (
                    "meta_description",
                    models.CharField(
                        blank=True,
                        help_text="content for description meta tag",
                        max_length=255,
                        null=True,
                        verbose_name="Meta Description",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
                "ordering": ["-added_on", "-is_onFlashsale"],
            },
        ),
        migrations.CreateModel(
            name="ProductAttribute",
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
                        help_text="format: required, unique, max_length-100",
                        max_length=100,
                        verbose_name="Product Attribute Name",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductType",
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
                        help_text="format: required, unique, max_length-100",
                        max_length=100,
                        unique=True,
                        verbose_name="Product Type",
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Subcategory",
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
                        help_text="format: required, max_length=100",
                        max_length=100,
                        verbose_name="Subcategory Name",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="format: optional",
                        null=True,
                        verbose_name="Subcategory Description",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="format: required, letters, numbers, underscore, or hyphens",
                        max_length=100,
                        verbose_name="Subcategory URL",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="subcategories",
                        to="inventory.category",
                        verbose_name="Main Category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Subcategory",
                "verbose_name_plural": "Subcategories",
                "ordering": ["created_at"],
            },
        ),
        migrations.CreateModel(
            name="Stock",
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
                    "last_checked",
                    models.DateTimeField(
                        blank=True,
                        help_text="format: Y-m-d H:M:S, null-true, blank-true",
                        null=True,
                        verbose_name="inventory stock check date",
                    ),
                ),
                (
                    "units",
                    models.IntegerField(
                        default=0,
                        help_text="format: required, default-0",
                        verbose_name="units/qty of stock",
                    ),
                ),
                (
                    "units_sold",
                    models.IntegerField(
                        default=0,
                        help_text="format: required, default-0",
                        verbose_name="units sold to date",
                    ),
                ),
                (
                    "product",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="product_stock",
                        to="inventory.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductAttributeValue",
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
                    "value",
                    models.CharField(
                        help_text="format: required, max_length-255",
                        max_length=50,
                        verbose_name="Product Type Attribute Value",
                    ),
                ),
                (
                    "attribute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="product_attribute",
                        to="inventory.productattribute",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="productattribute",
            name="product_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="product_type_attribute",
                to="inventory.producttype",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="attribute_value",
            field=models.ManyToManyField(
                blank=True,
                related_name="product_attribute_value",
                to="inventory.productattributevalue",
                verbose_name="Product Attribute Values",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="category",
                to="inventory.category",
                verbose_name="Category",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="lowersubcategory",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="lowersubcategory",
                to="inventory.lowersubcategory",
                verbose_name="Lower Subcategory",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="product_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="product_type",
                to="inventory.producttype",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="subcategory",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="subcategory",
                to="inventory.subcategory",
                verbose_name="Subcategory",
            ),
        ),
        migrations.CreateModel(
            name="Media",
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
                    "product_images",
                    cloudinary.models.CloudinaryField(
                        max_length=255, verbose_name="Image"
                    ),
                ),
                (
                    "alt_text",
                    models.CharField(
                        help_text="format: required, max_length-255",
                        max_length=255,
                        verbose_name="Alternative Text",
                    ),
                ),
                (
                    "is_feature",
                    models.BooleanField(
                        default=False,
                        help_text="format: default=false, true = default image",
                        verbose_name="Default Image",
                    ),
                ),
                (
                    "added_on",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="Date Added",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="product_images",
                        to="inventory.product",
                        verbose_name="Product Image",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Image",
                "verbose_name_plural": "Product Images",
            },
        ),
        migrations.AddField(
            model_name="lowersubcategory",
            name="subcategory",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="lowersubcategories",
                to="inventory.subcategory",
                verbose_name="Main Subcategory",
            ),
        ),
    ]
