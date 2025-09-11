from django.contrib import admin
from . import models


# Register your models here.


class ContactUsAdmin(admin.ModelAdmin):
    list_filter = ['title', 'seen_by_admin']
    list_display = ['email', 'title', 'seen_by_admin', 'created_date']


admin.site.register(models.ContactUs)
admin.site.register(models.ContactUsPageInfo)
