from django.contrib import admin
from .models import ApplicationForm

@admin.register(ApplicationForm)
class ApplicationFormAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'email', 'service_type', 'created_at')
    search_fields = ('full_name', 'phone_number', 'email', 'service_type')
    list_filter = ('service_type', 'tariff', 'created_at')
    ordering = ('-created_at',)

    class Media:
        js = ('../staticfiles/js/admin_sound.js',) 
