from ckeditor.fields import RichTextField
from django.utils import timezone
from django.db import models
from product_module.models import Product


class HomeVideoSection(models.Model):
    title = models.CharField("عنوان اصلی", max_length=255)
    subtitle = models.CharField("زیرعنوان", max_length=255)
    description = models.TextField("توضیحات")
    video_file = models.FileField("فایل ویدیو", upload_to='home/video/')
    is_active = models.BooleanField("فعال باشد؟", default=True)

    class Meta:
        verbose_name = "بخش ویدیویی صفحه اصلی"
        verbose_name_plural = "بخش‌های ویدیویی صفحه اصلی"

    def __str__(self):
        return self.title


class HotDealProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    priority = models.PositiveIntegerField(default=1, verbose_name="اولویت نمایش")
    countdown_expiry = models.DateTimeField(verbose_name="زمان پایان پیشنهاد", null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="فعال بودن پیشنهاد شگفت‌انگیز")


    class Meta:
        verbose_name = "محصول شگفت‌انگیز"
        verbose_name_plural = "محصولات شگفت‌انگیز"
        ordering = ['priority']

    def is_expired(self):
        return self.countdown_expiry and timezone.now() > self.countdown_expiry

    def __str__(self):
        return f"Hot Deal Active: {'Yes' if self.is_active else 'No'}"



# models.py

class FurnitureMainCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name="نام دسته اصلی", null=True, blank=True)
    order = models.PositiveIntegerField(default=0, verbose_name="ترتیب نمایش", null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="فعال باشد؟")

    class Meta:
        verbose_name = "دسته اصلی مبلمان"
        verbose_name_plural = "دسته‌های اصلی مبلمان"
        ordering = ['order']

    def __str__(self):
        return self.title or "بدون عنوان"


class FurnitureSubCategory(models.Model):
    main_category = models.ForeignKey(
        FurnitureMainCategory,
        on_delete=models.CASCADE,
        related_name='subcategories',
        verbose_name="دسته اصلی",
        null=True,
        blank=True
    )
    name = models.CharField(max_length=100, verbose_name="نام زیر‌دسته")
    products = models.ManyToManyField(
        Product,
        verbose_name="محصولات",
        limit_choices_to={'is_active': True, 'is_delete': False}
    )
    order = models.PositiveIntegerField(default=0, verbose_name="ترتیب")
    is_active = models.BooleanField(default=True, verbose_name="فعال باشد؟")

    class Meta:
        verbose_name = "زیر‌دسته مبلمان"
        verbose_name_plural = "زیر‌دسته‌های مبلمان"
        ordering = ['order']

    def __str__(self):
        if self.main_category and self.main_category.title:
            return f"{self.main_category.title} - {self.name}"
        return self.name


# models.py

from django.db import models
from django.utils.translation import gettext_lazy as _


class DepartmentCard(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="عنوان"
    )
    image = models.ImageField(
        upload_to='department_cards/',
        verbose_name="تصویر"
    )
    category = models.ForeignKey(
        'product_module.ProductCategory',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="دسته‌بندی مرتبط"
    )
    link = models.URLField(
        default='shop.html',
        verbose_name="لینک"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال باشد؟"
    )

    class Meta:
        verbose_name = "بخش"
        verbose_name_plural = "بخش ها"

    def __str__(self):
        return self.title



class RulesPage(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان صفحه")
    content = RichTextField(verbose_name="محتوای قوانین")
    is_active = models.BooleanField(default=True, verbose_name="فعال است؟")

    class Meta:
        verbose_name = "صفحه قوانین"
        verbose_name_plural = "صفحات قوانین"

    def __str__(self):
        return self.title


class PaymentMethodsPage(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان صفحه روش‌های پرداخت")
    content = RichTextField(verbose_name="محتوای صفحه روش‌های پرداخت")
    is_active = models.BooleanField(default=True, verbose_name="فعال است؟")

    class Meta:
        verbose_name = "صفحه روش‌های پرداخت"
        verbose_name_plural = "صفحات روش‌های پرداخت"

    def __str__(self):
        return self.title


class RefundTermsPage(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان صفحه شرایط بازگشت")
    content = RichTextField(verbose_name="محتوای صفحه شرایط بازگشت")
    is_active = models.BooleanField(default=True, verbose_name="فعال است؟")

    class Meta:
        verbose_name = "صفحه شرایط بازگشت"
        verbose_name_plural = "صفحات شرایط بازگشت"

    def __str__(self):
        return self.title



class ShipmentPage(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان صفحه ارسال")
    content = RichTextField(verbose_name="محتوای صفحه ارسال")
    is_active = models.BooleanField(default=True, verbose_name="فعال است؟")

    class Meta:
        verbose_name = "صفحه ارسال"
        verbose_name_plural = "صفحات ارسال"

    def __str__(self):
        return self.title

