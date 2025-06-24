from django.contrib import admin
from django.utils.safestring import mark_safe

from shop.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")
    list_display_links = ("title",)


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("title",)


@admin.register(ProductTags)
class ProductTagsAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("title",)


class ProductImageTabularInline(admin.TabularInline):
    fk_name = 'product'
    model = ProductImage
    extra = 5


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "sale",
                    "discount_percent", "created_at",
                    "category", 'get_image')
    list_display_links = ("title",)
    inlines = [ProductImageTabularInline]

    def get_image(self, obj):
        if obj.product_images:
            try:
                return mark_safe(f"<img src='{obj.product_images.all()[0].image.url}' width='50'>")
            except:
                return '-'
        else:
            return '-'


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product')
    list_display_links = ('id',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "product")


@admin.register(FavoriteProduct)
class FavoriteProductAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product")
