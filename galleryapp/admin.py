from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import GalleryItem

@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'uploaded_by', 'is_approved', 'uploaded_at')
    list_filter = ('is_approved', 'media_type', 'uploaded_at')
    search_fields = ('title', 'description', 'uploaded_by__username')
