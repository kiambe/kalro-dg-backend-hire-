from django.contrib import admin

from .models import Category, Product, ProductImage, ProductColour, ProductSize

admin.site.register(Category)
admin.site.register(ProductColour)
admin.site.register(ProductSize)
admin.site.register(Product)
admin.site.register(ProductImage)