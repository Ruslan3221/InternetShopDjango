from django.contrib import admin
from .models import Product,ProductImage


class ImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)


# Register your models here.
