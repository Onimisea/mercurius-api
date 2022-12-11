from django.contrib import admin

from .models import (
    Category,
    Media,
    Product,
    ProductAttribute,
    ProductAttributeValue,
    ProductType,
    Stock,
    Subcategory,
    LowerSubcategory,
    FlashsaleCtrl,
)

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "category"]
    prepopulated_fields = {"slug": ("name",)}

@admin.register(LowerSubcategory)
class LowerSubcategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "subcategory"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "category",
        "subcategory",
        "price",
        "is_onFlashsale",
        "slug",
    ]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = [
        "category",
        "subcategory",
        "in_stock",
        "is_onFlashsale",
        "is_active",
    ]

admin.site.register(ProductType)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
  list_display = ['product', 'alt_text', 'is_feature']
  list_filter = ['product']


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
  list_display = ['product', 'units', 'units_sold']
  list_filter = ['product', 'last_checked']

@admin.register(FlashsaleCtrl)
class FlashsaleCtrlAdmin(admin.ModelAdmin):
    list_display = ['name', 'when']
    list_filter = ['name', 'when']