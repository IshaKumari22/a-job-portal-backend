from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display=('title','recruiter','location','experience_required')
    list_filter=('location','experience_required')
    search_fields=('title','skills')
