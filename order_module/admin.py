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
    list_display = ['id', 'order', 'product', 'count', 'final_price', 'get_addons_display', 'get_options_display']
    list_filter = ['order__is_paid']
    search_fields = ['product__title', 'order__user__username']
    readonly_fields = ['get_order_display', 'get_addons_display', 'get_options_display']
    fields = ['product', 'get_order_display', 'final_price', 'count', 'get_addons_display', 'get_options_display']
    
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }
    
    def get_order_display(self, obj):
        """Display order information in a more readable format"""
        if obj.order:
            status = "پرداخت شده" if obj.order.is_paid else "در انتظار پرداخت"
            total_amount = obj.order.calculate_total_price()
            # Format the amount with Persian numbers
            from polls.templatetags.poll_extras import three_digits_currency
            formatted_amount = three_digits_currency(total_amount)
            return f"سفارش #{obj.order.id} - {obj.order.user.username} ({status}) - مجموع: {formatted_amount}"
        return "سفارش نامشخص"
    
    get_order_display.short_description = 'سبد خرید'
    get_order_display.admin_order_field = 'order__id'
    
    def get_addons_display(self, obj):
        """Display user-friendly addons text"""
        return obj.get_addons_display()
    
    get_addons_display.short_description = 'افزونه‌های انتخاب شده'
    get_addons_display.admin_order_field = 'selected_addons'
    
    def get_options_display(self, obj):
        """Display user-friendly options text"""
        return obj.get_options_display()
    
    get_options_display.short_description = 'گزینه‌های انتخاب شده'
    get_options_display.admin_order_field = 'selected_options'

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
