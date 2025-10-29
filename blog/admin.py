from django.contrib import admin
from .models import Post, Category
from django.utils.safestring import mark_safe
from .models import Comment

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author", "created_at", "published", "image_preview")
    list_filter = ("published", "created_at", "author", "category")
    search_fields = ("title", "content")
    
    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="height: 50px;">')
        return "-"
    image_preview.short_description = 'Image'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'content', 'created_at', 'approved')
    list_filter = ('approved', 'created_at')
    search_fields = ('content', 'user__username')
