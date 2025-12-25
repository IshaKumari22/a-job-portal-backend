from django.contrib import admin
from .models import Resume


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'uploaded_at')
    readonly_fields = ('uploaded_at', 'extracted_text')

    fieldsets = (
        (None, {
            'fields': ('candidate', 'resume_file')
        }),
        ('Extracted Resume Text', {
            'fields': ('extracted_text',),
        }),
        ('Timestamps', {
            'fields': ('uploaded_at',),
        }),
    )
