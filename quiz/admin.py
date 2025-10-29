from django.contrib import admin
from .models import Banner, Instruction, Content


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title_english', 'subtitle_english', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['title_english']
    ordering = ['-created_at']

class ContentInline(admin.TabularInline):  # or use admin.StackedInline for vertical layout
    model = Content
    extra = 1

@admin.register(Instruction)
class InstructionTitleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']
    inlines = [ContentInline]


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'ins_title', 'content']
    search_fields = ['content']
    list_filter = ['ins_title']



