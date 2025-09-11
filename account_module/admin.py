from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminForm
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserAdminForm

    fieldsets = BaseUserAdmin.fieldsets + (
        ('خرید چکی', {
            'fields': ('has_check_purchase_permission', 'check_purchase_credit'),
        }),
    )

    def formatted_credit(self, obj):
        return f"{obj.check_purchase_credit:,}"  # Adds commas

    formatted_credit.short_description = 'اعتبار خرید چکی'  # Persian label
    formatted_credit.admin_order_field = 'check_purchase_credit'

    list_display = BaseUserAdmin.list_display + ('has_check_purchase_permission', 'formatted_credit')

    class Media:
        css = {
            'all': ('yourapp/css/admin_custom.css',)
        }

