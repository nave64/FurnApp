from django.contrib import admin

# Register your models here.
# admin.py
from django.contrib import admin
from .models import UserImageUpload

@admin.register(UserImageUpload)
class UserImageUploadAdmin(admin.ModelAdmin):
    list_display = ('user_username', 'user_full_name', 'user_mobile', 'submitted_at')
    readonly_fields = ('image_1', 'image_2')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'user__mobile')
    list_filter = ('submitted_at',)

    def user_username(self, obj):
        return obj.user.username
    user_username.short_description = 'نام کاربری'

    def user_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    user_full_name.short_description = 'نام کامل'

    def user_mobile(self, obj):
        return obj.user.mobile
    user_mobile.short_description = 'شماره موبایل'

