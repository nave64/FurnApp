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
    list_display = ['id', 'get_user_display', 'amount', 'status', 'ref_id', 'created_at', 'payment_date']
    list_filter = ['status', 'created_at', 'payment_date']
    search_fields = ['user__username', 'user__email', 'user__first_name', 'user__last_name', 'ref_id', 'authority']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    
    def get_user_display(self, obj):
        """Display user information in a more readable format"""
        if obj.user:
            if obj.user.get_full_name():
                return f"{obj.user.get_full_name()} ({obj.user.username})"
            else:
                return obj.user.username
        return "کاربر نامشخص"
    
    get_user_display.short_description = 'کاربر'
    get_user_display.admin_order_field = 'user__username'
