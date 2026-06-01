from django.contrib import admin
from .models import Circular


@admin.register(Circular)
class CircularAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'publish_date',
        'created_at'
    )

    list_filter = (
        'publish_date',
    )

    search_fields = (
        'title',
    )