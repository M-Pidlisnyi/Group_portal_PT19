from django.contrib import admin
from .models import Material

# Register your models here.
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'material_type', 'uploaded_by', 'created_at')
    list_filter = ('material_type', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')