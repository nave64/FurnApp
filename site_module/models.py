from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField(
        max_length=200,
        verbose_name='نام سایت',
        null=True,
        blank=True
    )
    site_url = models.CharField(
        max_length=200,
        verbose_name='دامنه سایت',
        null=True,
        blank=True
    )
    site_logo = models.ImageField(
        upload_to='images/site-settings/',
        verbose_name='لوگو سایت',
        null=True,
        blank=True
    )
    instagram_address = models.CharField(
        max_length=200,
        verbose_name='آدرس پیج اینستاگرام',
        null=True,
        blank=True
    )
    whatsapp_number = models.CharField(
        max_length=20,
        verbose_name='شماره واتساپ',
        null=True,
        blank=True
    )
    telegram_link = models.CharField(
        max_length=200,
        verbose_name='لینک تلگرام',
        null=True,
        blank=True
    )
    phone = models.CharField(
        max_length=200,
        verbose_name='شماره تماس',
        null=True,
        blank=True
    )
    email = models.CharField(
        max_length=200,
        verbose_name='ایمیل',
        null=True,
        blank=True
    )
    business_address = models.CharField(
        max_length=200,
        verbose_name='آدرس کسب‌وکار',
        null=True,
        blank=True
    )
    copyright = models.TextField(
        verbose_name='متن کپی رایت',
        null=True,
        blank=True
    )

    is_main_settings = models.BooleanField(
        verbose_name='تنظیمات اصلی',
        default=False
    )

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.site_name or "Site Settings"
