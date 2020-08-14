from django.contrib import admin
from .models import UserProfile


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'nickname',
        'history',
    )


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
