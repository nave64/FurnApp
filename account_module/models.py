
import secrets
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models



# Create your models here.


class User(AbstractUser):
    mobile = models.CharField(max_length=11, verbose_name='تلفن همراه', unique=True)
    username = models.CharField(max_length=100, verbose_name='اسم کاربر', null=True, unique=True)
    postal_code = models.CharField(max_length=10, verbose_name='کدپستی کاربر ',null=True)
    email_active_code = models.IntegerField(verbose_name='کد فعالسازی موبایل',null=True)
    address = models.TextField(verbose_name='آدرس', null=True, blank=True)

    # ✅ New fields for check-based buying
    has_check_purchase_permission = models.BooleanField(
        default=False,
        verbose_name='دارای مجوز خرید چکی؟'
    )
    check_purchase_credit = models.PositiveIntegerField(
        default=0,
        verbose_name='اعتبار خرید چکی (تومان)'
    )

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=15)
