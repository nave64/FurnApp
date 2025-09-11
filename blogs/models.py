from django.db import models
from django.utils import timezone
from jalali_date import datetime2jalali

class Blog(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='عنوان'
    )
    short_description = models.TextField(
        verbose_name='توضیح کوتاه'
    )
    full_description = models.TextField(
        verbose_name='توضیح کامل'
    )
    image = models.ImageField(
        upload_to='blogs/',
        verbose_name='تصویر'
    )
    published_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='تاریخ انتشار'
    )

    class Meta:
        verbose_name = 'وبلاگ'
        verbose_name_plural = 'وبلاگ‌ها'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    def get_jalali_date(self):
        return datetime2jalali(self.published_at).strftime('%d %b %Y')
