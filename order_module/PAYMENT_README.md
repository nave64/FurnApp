# سیستم پرداخت زرین‌پال

این سیستم پرداخت بر اساس API زرین‌پال پیاده‌سازی شده است و شامل قابلیت‌های زیر می‌باشد:

## ویژگی‌ها

- پرداخت مستقیم با مبلغ دلخواه
- پرداخت سفارشات
- تاریخچه پرداخت‌ها
- مدیریت وضعیت پرداخت
- رابط کاربری فارسی و ریسپانسیو

## تنظیمات

### 1. تنظیمات در settings.py

```python
# Zarinpal Payment Gateway Configuration
ZARINPAL_MERCHANT_ID = 'YOUR_MERCHANT_ID'  # کد مرچنت خود را وارد کنید
ZARINPAL_SANDBOX = True  # برای تست True، برای تولید False
ZARINPAL_CALLBACK_URL = 'https://yourdomain.com/order/payment-verify/'  # آدرس کالبک خود را وارد کنید
```

### 2. نصب وابستگی‌ها

```bash
pip install requests
```

## URL های موجود

- `/order/payment/` - فرم پرداخت مستقیم
- `/order/order-payment/` - پرداخت سفارش
- `/order/payment-verify/` - تأیید پرداخت (کالبک)
- `/order/payment-history/` - تاریخچه پرداخت‌ها

## استفاده

### 1. پرداخت مستقیم

```python
# در ویو خود
from django.shortcuts import redirect
from django.urls import reverse

def my_view(request):
    # هدایت به فرم پرداخت
    return redirect(reverse('payment_form'))
```

### 2. پرداخت سفارش

```python
# در ویو خود
from django.shortcuts import redirect
from django.urls import reverse

def pay_order(request):
    # هدایت به پرداخت سفارش
    return redirect(reverse('order_payment_new'))
```

### 3. استفاده در تمپلیت

```html
<!-- لینک پرداخت مستقیم -->
<a href="{% url 'payment_form' %}" class="btn btn-primary">
    پرداخت مستقیم
</a>

<!-- لینک پرداخت سفارش -->
<a href="{% url 'order_payment_new' %}" class="btn btn-success">
    پرداخت سفارش
</a>

<!-- لینک تاریخچه پرداخت‌ها -->
<a href="{% url 'payment_history' %}" class="btn btn-info">
    تاریخچه پرداخت‌ها
</a>
```

## مدل‌های دیتابیس

### Payment Model

```python
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.PositiveIntegerField()  # مبلغ به ریال
    authority = models.CharField(max_length=100)  # کد مرجع
    ref_id = models.CharField(max_length=100)  # شماره پیگیری
    status = models.CharField(max_length=20)  # وضعیت پرداخت
    description = models.TextField()  # توضیحات
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    payment_date = models.DateTimeField(null=True, blank=True)
```

## وضعیت‌های پرداخت

- `pending` - در انتظار پرداخت
- `success` - پرداخت موفق
- `failed` - پرداخت ناموفق
- `cancelled` - لغو شده

## تست سیستم

### 1. حالت تست (Sandbox)

برای تست سیستم، `ZARINPAL_SANDBOX = True` را در settings.py تنظیم کنید.

### 2. کارت‌های تست زرین‌پال

- شماره کارت: 6037-9970-0000-0000
- CVV2: 123
- رمز دوم: 123456

## امنیت

- تمام درخواست‌ها با HTTPS انجام می‌شود
- کدهای مرجع منحصر به فرد هستند
- تأیید پرداخت از طریق API رسمی زرین‌پال انجام می‌شود

## عیب‌یابی

### خطاهای رایج

1. **خطا در ایجاد درخواست پرداخت**
   - بررسی کنید کد مرچنت صحیح باشد
   - اتصال اینترنت را بررسی کنید

2. **خطا در تأیید پرداخت**
   - مبلغ پرداخت را بررسی کنید
   - کد مرجع را بررسی کنید

3. **خطای کالبک**
   - آدرس کالبک را در settings.py بررسی کنید
   - URL patterns را بررسی کنید

## پشتیبانی

برای پشتیبانی و راهنمایی بیشتر، با تیم توسعه تماس بگیرید.
