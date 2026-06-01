from django.contrib import admin
from .models import WelfareScheme


@admin.register(WelfareScheme)
class WelfareSchemeAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'is_featured',
        'created_at'
    )

    list_filter = (
        'is_featured',
        'created_at'
    )

    prepopulated_fields = {
        'slug': ('title',)
    }

    search_fields = (
        'title',
    )