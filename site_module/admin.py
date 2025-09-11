from django.contrib import admin
from . import models




admin.site.register(models.SiteSettings)
admin.site.site_header = "مدیریت سایت"
admin.site.site_title = "مدیریت سایت"
admin.site.index_title = "به مدیریت سایت خوش آمدید"

