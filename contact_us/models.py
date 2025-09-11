from django.db import models


# Create your models here.

# contact_us/models.py

class ContactUs(models.Model):
    full_name = models.CharField(max_length=50, verbose_name='نام و نام خانوادگی')
    mobile = models.CharField(max_length=20, verbose_name='شماره موبایل',null=True)  # ✅ NEW FIELD
    title = models.CharField(max_length=300, verbose_name='عنوان')
    message = models.TextField(verbose_name='متن پیام')
    created_date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    seen_by_admin = models.BooleanField(verbose_name='خوانده شده توسط ادمین', null=True)

    class Meta:
        verbose_name = 'تماس با ما '
        verbose_name_plural = 'لیست تماس با ما  '

    def __str__(self):
        return self.title





class ContactUsPageInfo(models.Model):
    info_description = models.CharField(max_length=300, verbose_name='توضیحات مربوط به صفحه تماس با ما ')
    address_info = models.CharField(max_length=100, verbose_name='آدرس مربوط به صفحه تماس با ما ')
    phone_info = models.CharField(max_length=100, verbose_name='شماره تماس مربوط به صفحه تماس با ما ')
    email_info = models.CharField(max_length=100, verbose_name='ایمیل مربوط به صفحه تماس با ما ')

    class Meta:
        verbose_name = 'اطلاعات تماس با ما  '
        verbose_name_plural = 'اطلاعات کنار صفحه تماس با ما   '

    def __str__(self):
        return self.info_description


class UserProfile(models.Model):
    image = models.ImageField(upload_to='images')