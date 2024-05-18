from django.contrib import admin
from .models import Product,ProductImage,Message,Order


class ImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Message)
admin.site.register(Order)

# Register your models here.
