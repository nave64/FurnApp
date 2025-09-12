from django.db import models
from account_module.models import User
from product_module.models import Product
from django.utils import timezone
# from user_panel_module.models import Transportation
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name='نهایی شده / نشده')
    payment_date = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')

    def __str__(self):
        status = "پرداخت شده" if self.is_paid else "در انتظار پرداخت"
        return f"سفارش #{self.id} - {self.user.username} ({status})"

    def calculate_total_price(self):
        total_amount = 0
        for order_detail in self.orderdetail_set.all():
            # Base price + addon costs, multiplied by quantity
            item_total = order_detail.get_final_price_with_addons() * order_detail.count
            total_amount += item_total
        return total_amount

    class Meta:
        verbose_name = 'سبد خرید '
        verbose_name_plural = ' سبدهای خرید کاربران '



class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    final_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی محصول تکی ')
    count = models.IntegerField(verbose_name='تعداد')
    selected_addons = models.JSONField(default=list, blank=True, verbose_name='افزونه‌های انتخاب شده')
    selected_options = models.JSONField(default=dict, blank=True, verbose_name='گزینه‌های انتخاب شده')

    def __str__(self):
        return f"Order ID: {self.order.id}, Product: {self.product.title}, Count: {self.count}"

    def get_total_addon_cost(self):
        """Calculate total cost of selected add-ons"""
        from product_module.models import ProductAddon
        total_cost = 0
        for addon_id in self.selected_addons:
            try:
                # Convert to int if it's a string
                addon_id_int = int(addon_id) if isinstance(addon_id, str) else addon_id
                addon = ProductAddon.objects.get(id=addon_id_int, is_active=True)
                total_cost += addon.additional_cost
            except (ProductAddon.DoesNotExist, ValueError):
                continue
        return total_cost

    def get_final_price_with_addons(self):
        """Get final price including add-ons"""
        base_price = self.final_price or self.product.price
        return base_price + self.get_total_addon_cost()

    def get_addons_display(self):
        """Get user-friendly display of selected addons"""
        from product_module.models import ProductAddon
        addon_names = []
        for addon_id in self.selected_addons:
            try:
                addon_id_int = int(addon_id) if isinstance(addon_id, str) else addon_id
                addon = ProductAddon.objects.get(id=addon_id_int, is_active=True)
                addon_names.append(addon.name)
            except (ProductAddon.DoesNotExist, ValueError):
                continue
        return " | ".join(addon_names) if addon_names else "هیچ افزونه‌ای انتخاب نشده"

    def get_options_display(self):
        """Get user-friendly display of selected options"""
        option_texts = []
        for option_name, option_value_id in self.selected_options.items():
            for option_type in self.product.selectable_options.all():
                if option_name == f"option_{option_type.option_type.id}":
                    for value in option_type.allowed_values.all():
                        if str(value.id) == str(option_value_id):
                            option_texts.append(f"{option_type.option_type.name}: {value.value}")
                            break
                    break
        return " | ".join(option_texts) if option_texts else "هیچ گزینه‌ای انتخاب نشده"

    class Meta:
        verbose_name = 'جزئیات سبد خرید '
        verbose_name_plural = ' لیست جزئیات سبدهای خرید کاربران '


class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'در انتظار پرداخت'),
        ('success', 'پرداخت موفق'),
        ('failed', 'پرداخت ناموفق'),
        ('cancelled', 'لغو شده'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سفارش', null=True, blank=True)
    amount = models.PositiveIntegerField(verbose_name='مبلغ (ریال)')
    authority = models.CharField(max_length=100, verbose_name='کد مرجع', null=True, blank=True)
    ref_id = models.CharField(max_length=100, verbose_name='شماره پیگیری', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='وضعیت')
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    payment_date = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ پرداخت')

    def __str__(self):
        if self.user:
            user_name = self.user.get_full_name() or self.user.username
            return f"پرداخت {self.id} - {user_name} - {self.amount} ریال"
        else:
            return f"پرداخت {self.id} - کاربر نامشخص - {self.amount} ریال"

    class Meta:
        verbose_name = 'پرداخت'
        verbose_name_plural = 'پرداخت‌ها'
        ordering = ['-created_at']



