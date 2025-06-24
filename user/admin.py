from django.contrib import admin

from user.models import *


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "phone_number")
    list_display_links = ("username",)


admin.site.register(Cart)
admin.site.register(CartItem)

