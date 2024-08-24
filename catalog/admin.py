from django.contrib import admin

from catalog.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category',)
    list_filter = ('category_id',)
    search_fields = ('product_name', 'product_description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)
    list_filter = ('category_name',)
    search_fields = ('category_name', 'category_description',)
