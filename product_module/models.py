from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from account_module.models import User
from django.utils.text import slugify

from django.utils.text import slugify


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url', blank=True, editable=False)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True, verbose_name='تصویر دسته‌بندی')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def save(self, *args, **kwargs):
        if not self.url_title:
            self.url_title = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'( {self.title} - {self.url_title} )'

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'



# models.py

from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام محصول')
    product_quantity = models.BooleanField(verbose_name='موجودی محصول', default=True, null=True)
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='تصویر محصول')
    category = models.ManyToManyField(ProductCategory, related_name='product_categories', verbose_name='دسته بندی ها')
    discount_price = models.IntegerField(verbose_name='قیمت تخفیف', null=True)
    price = models.IntegerField(verbose_name='قیمت اصلی')
    cheque_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت چکی') 
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True, verbose_name='عنوان در url', allow_unicode=True)
    short_description = RichTextField(null=True, blank=True, verbose_name='توضیح کوتاه')
    description = RichTextField(null=True, blank=True, verbose_name='توضیح کامل')
    badge_text = models.CharField(max_length=50, null=True, blank=True, verbose_name='متن بج (نشان)')
    is_new = models.BooleanField(
        default=False,
        verbose_name='محصول جدید؟',
        help_text='اگر این تیک فعال باشد، بج "جدید" زیر بج اصلی نمایش داده می‌شود.'
    )
    is_discount_active = models.BooleanField(verbose_name='تخفیف فعال است؟', default=False, help_text='اگر مایل به نمایش این تخفیف در سایت هستید این تیک را بزنید.')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')
    has_custom_options = models.BooleanField(
        default=False,
        verbose_name='آیا این محصول نیاز به مشخصات انتخابی دارد؟'
    )

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title, allow_unicode=True)
            slug = base_slug
            num = 1
            while Product.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def discount_percent(self):
        if self.is_discount_active and self.price and self.discount_price:
            try:
                discount = 100 - int((self.discount_price / self.price) * 100)
                return discount
            except ZeroDivisionError:
                return 0
        return None

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/products/gallery/')
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.product.title} - {self.id}"

class ProductOptionType(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام گزینه (مثل رنگ نما)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "نوع گزینه"
        verbose_name_plural = "انواع گزینه‌ها"


class ProductOptionValue(models.Model):
    option_type = models.ForeignKey(ProductOptionType, on_delete=models.CASCADE, related_name='values')
    value = models.CharField(max_length=100, verbose_name="مقدار گزینه")

    def __str__(self):
        return f"{self.option_type.name} - {self.value}"

    class Meta:
        verbose_name = "مقدار گزینه"
        verbose_name_plural = "مقادیر گزینه‌ها"


class ProductSelectableOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='selectable_options')
    option_type = models.ForeignKey(ProductOptionType, on_delete=models.CASCADE, verbose_name="نوع گزینه")
    allowed_values = models.ManyToManyField(ProductOptionValue, verbose_name="مقادیر مجاز")

    def __str__(self):
        return f"{self.product.title} - {self.option_type.name}"

    class Meta:
        verbose_name = "گزینه انتخابی محصول"
        verbose_name_plural = "گزینه‌های انتخابی محصول"

class ProductComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name='محصول')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    text = models.TextField(verbose_name='متن نظر')
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified_buyer = models.BooleanField(default=False, verbose_name='خریدار تایید شده؟')

    def __str__(self):
        return f"Comment by {self.user.username if self.user else 'Unknown'} on {self.product.title}"

    class Meta:
        verbose_name = 'نظر محصول'
        verbose_name_plural = 'نظرات محصولات'



class ProductListPageSetting(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان صفحه")
    background_image = models.ImageField(upload_to='product-list-bg/', verbose_name="تصویر پس‌زمینه")
    is_active = models.BooleanField(default=True, verbose_name="فعال باشد؟")

    class Meta:
        verbose_name = "تنظیمات صفحه لیست محصولات"
        verbose_name_plural = "تنظیمات صفحه لیست محصولات"

    def __str__(self):
        return self.title


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlists')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlisted_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'علاقه‌مندی'
        verbose_name_plural = 'لیست علاقه‌مندی‌ها'
        unique_together = ('user', 'product')  # هر محصول فقط یکبار توسط یک کاربر قابل ثبت است

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"


class ProductAddon(models.Model):
    """
    Model for product add-ons that increase the cost when selected by users
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='addons', verbose_name='محصول')
    name = models.CharField(max_length=200, verbose_name='نام افزونه')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')
    additional_cost = models.PositiveIntegerField(verbose_name='هزینه اضافی')
    is_required = models.BooleanField(default=False, verbose_name='اجباری است؟')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    sort_order = models.PositiveIntegerField(default=0, verbose_name='ترتیب نمایش')
    
    class Meta:
        verbose_name = 'افزونه محصول'
        verbose_name_plural = 'افزونه‌های محصولات'
        ordering = ['sort_order', 'name']
    
    def __str__(self):
        return f"{self.product.title} - {self.name} (+{self.additional_cost:,} ریال)"