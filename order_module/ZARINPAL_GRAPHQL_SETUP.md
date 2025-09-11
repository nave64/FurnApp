# راهنمای راه‌اندازی Zarinpal GraphQL API

## مقدمه

زرین‌پال از نسخه جدید خود، یک API مبتنی بر GraphQL و OAuth 2.0 ارائه داده است. این راهنما نحوه راه‌اندازی و استفاده از این API را توضیح می‌دهد.

## مراحل راه‌اندازی

### 1. دریافت Access Token

برای استفاده از API جدید، ابتدا باید یک Access Token دریافت کنید:

1. به پنل زرین‌پال وارد شوید
2. بخش API را پیدا کنید
3. مراحل احراز هویت OAuth 2.0 را طی کنید
4. Access Token خود را دریافت کنید

### 2. تنظیمات پروژه

در فایل `settings.py` تنظیمات زیر را اضافه کنید:

```python
# Zarinpal Payment Gateway Configuration
ZARINPAL_MERCHANT_ID = 'YOUR_MERCHANT_ID'  # شناسه مرچنت شما
ZARINPAL_ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'  # توکن دسترسی OAuth 2.0
ZARINPAL_SANDBOX = True  # برای تست True، برای تولید False
ZARINPAL_CALLBACK_URL = 'https://yourdomain.com/order/payment-verify/'
ZARINPAL_MOCK_MODE = False  # برای تست True، برای تولید False
```

### 3. GraphQL Endpoint

API جدید از آدرس زیر استفاده می‌کند:
```
https://next.zarinpal.com/api/v4/graphql/
```

### 4. نمونه درخواست

```bash
curl 'https://next.zarinpal.com/api/v4/graphql/' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  --data-binary '{"query":"mutation CreatePaymentRequest($input: PaymentRequestInput!) { createPaymentRequest(input: $input) { success data { authority paymentUrl } errors { message code } } }","variables":{"input":{"merchantId":"YOUR_MERCHANT_ID","amount":100000,"description":"Test Payment","callbackUrl":"https://yourdomain.com/callback"}}}'
```

## ویژگی‌های جدید

### 1. GraphQL Queries

سیستم از GraphQL queries استفاده می‌کند:

#### ایجاد درخواست پرداخت:
```graphql
mutation CreatePaymentRequest($input: PaymentRequestInput!) {
  createPaymentRequest(input: $input) {
    success
    data {
      authority
      paymentUrl
    }
    errors {
      message
      code
    }
  }
}
```

#### تأیید پرداخت:
```graphql
mutation VerifyPayment($input: PaymentVerifyInput!) {
  verifyPayment(input: $input) {
    success
    data {
      refId
      amount
    }
    errors {
      message
      code
    }
  }
}
```

### 2. مزایای GraphQL

- **یک Endpoint**: تمام عملیات از یک آدرس انجام می‌شود
- **انعطاف‌پذیری**: فقط فیلدهای مورد نیاز را دریافت کنید
- **کارایی**: چندین query در یک درخواست
- **Schema**: مستندات کامل API

## حالت Mock برای تست

برای تست سیستم بدون نیاز به Access Token واقعی:

```python
ZARINPAL_MOCK_MODE = True
```

این حالت:
- درخواست‌های پرداخت را شبیه‌سازی می‌کند
- صفحه تست زیبا ارائه می‌دهد
- تمام سناریوهای پرداخت را پشتیبانی می‌کند

## عیب‌یابی

### خطاهای رایج

1. **401 Unauthorized**: Access Token نامعتبر
2. **400 Bad Request**: پارامترهای نادرست
3. **404 Not Found**: Query یا mutation نادرست

### لاگ‌ها

سیستم لاگ‌های کاملی از درخواست‌ها و پاسخ‌ها ارائه می‌دهد:

```python
print(f"GraphQL Response: {response}")
```

## مهاجرت از API قدیمی

### تغییرات اصلی:

1. **REST → GraphQL**: تغییر از REST API به GraphQL
2. **OAuth 2.0**: نیاز به Access Token
3. **Endpoint جدید**: آدرس API تغییر کرده
4. **ساختار پاسخ**: فرمت پاسخ‌ها متفاوت است

### کد قدیمی:
```python
response = requests.post('https://api.zarinpal.com/pg/v4/request.json', json=data)
```

### کد جدید:
```python
response = make_zarinpal_graphql_request(ZP_PAYMENT_REQUEST_QUERY, variables)
```

## پشتیبانی

برای پشتیبانی و راهنمایی بیشتر:
- مستندات رسمی زرین‌پال
- تیم پشتیبانی فنی
- انجمن‌های توسعه‌دهندگان

## نکات مهم

1. **امنیت**: Access Token را محرمانه نگه دارید
2. **تست**: همیشه در محیط تست آزمایش کنید
3. **لاگ‌ها**: لاگ‌ها را برای عیب‌یابی بررسی کنید
4. **بروزرسانی**: از آخرین نسخه API استفاده کنید
