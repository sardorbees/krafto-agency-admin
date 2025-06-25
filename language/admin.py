from django.contrib import admin
from .models import LanguagePreference

@admin.register(LanguagePreference)
class LanguagePreferenceAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'language')
    search_fields = ('session_id',)
    list_filter = ('language',)