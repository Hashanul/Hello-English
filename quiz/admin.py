from django.contrib import admin
from .models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['title']
    ordering = ['-created_at']




