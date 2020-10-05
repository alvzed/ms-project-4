from django.contrib import admin
from .models import Category, Video, Review


class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'title',
        'description',
        'pg',
        'video_link',
        'views',
    )

    ordering = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'clicks',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'video',
        'rating',
        'description',
        'thumbsup',
        'thumbsdown',
    )


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Review, ReviewAdmin)
