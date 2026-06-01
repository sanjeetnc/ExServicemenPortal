from django.contrib import admin
from .models import TrustActivity


@admin.register(TrustActivity)
class TrustActivityAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'event_date',
        'is_featured'
    )

    list_filter = (
        'event_date',
        'is_featured'
    )

    search_fields = (
        'title',
        'location'
    )