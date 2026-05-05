from django.contrib import admin
from .models import Service, Project, GalleryImage

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1
    fields = ('image', 'title', 'description', 'order', 'is_active')
    ordering = ('order', 'created_at')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'order', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    ordering = ('order', 'title')
    list_editable = ('is_active', 'order')

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'image')
        }),
        ('Settings', {
            'fields': ('order', 'is_active'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'is_featured', 'is_active', 'order', 'created_at', 'gallery_image_count')
    list_filter = ('is_featured', 'is_active', 'tag', 'created_at')
    search_fields = ('title', 'description', 'tag')
    ordering = ('order', 'title')
    list_editable = ('is_featured', 'is_active', 'order')
    inlines = [GalleryImageInline]

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'tag', 'image')
        }),
        ('Links & Settings', {
            'fields': ('link_url', 'order', 'is_featured', 'is_active'),
            'classes': ('collapse',)
        }),
    )

    def gallery_image_count(self, obj):
        return obj.gallery_images.filter(is_active=True).count()
    gallery_image_count.short_description = "Gallery Images"

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'title', 'is_active', 'order', 'created_at')
    list_filter = ('is_active', 'created_at', 'project')
    search_fields = ('title', 'description', 'project__title')
    ordering = ('project', 'order', 'created_at')
    list_editable = ('is_active', 'order')

    fieldsets = (
        ('Project Association', {
            'fields': ('project',)
        }),
        ('Image Details', {
            'fields': ('image', 'title', 'description')
        }),
        ('Settings', {
            'fields': ('order', 'is_active'),
            'classes': ('collapse',)
        }),
    )
