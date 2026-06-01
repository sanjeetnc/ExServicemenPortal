from django.contrib import admin
from .models import Enquiry

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'mobile',
        'category',
        'subject',
        'status',
        'created_at'
    )

    list_filter = (
        'category',
        'status'
    )

    search_fields = (
        'full_name',
        'mobile',
        'subject'
    )