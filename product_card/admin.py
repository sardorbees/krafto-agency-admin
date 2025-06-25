from django.contrib import admin
from .models import Product, Order, OrderItem
from django.utils.html import format_html


# Отображение товара с миниатюрой
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'image_tag']
    search_fields = ['title']
    list_filter = ['price']
    list_per_page = 20

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 50px;" />', obj.image)
        return "-"
    image_tag.short_description = "Фото"


# Встроенные товары в заказ
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'quantity']


# Отображение заказов
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'total_items']
    readonly_fields = ['created_at']
    inlines = [OrderItemInline]

    def total_items(self, obj):
        return sum(item.quantity for item in obj.items.all())
    total_items.short_description = "Всего товаров"
