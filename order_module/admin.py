from django.contrib import admin
from .models import Order, OrderDetail, Payment

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'is_paid', 'payment_date', 'calculate_total_price']
    list_filter = ['is_paid', 'payment_date']
    search_fields = ['user__username', 'user__email']
    readonly_fields = ['calculate_total_price']

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'count', 'final_price']
    list_filter = ['order__is_paid']
    search_fields = ['product__title', 'order__user__username']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'status', 'ref_id', 'created_at', 'payment_date']
    list_filter = ['status', 'created_at', 'payment_date']
    search_fields = ['user__username', 'user__email', 'ref_id', 'authority']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
