from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from django.db import models
from django.db.models import Model
from jalali_date import date2jalali
from jalali_date.admin import ModelAdminJalaliMixin
from django.forms import NumberInput
from django import forms
from django.forms import CheckboxInput
from django.forms import NumberInput
from ckeditor.widgets import CKEditorWidget
from .models import Product, ProductImage

from .models import (
    Product,
    ProductCategory,
    ProductListPageSetting,
    ProductComment,
    ProductOptionType,
    ProductOptionValue,
    ProductSelectableOption,
    ProductAddon
)

# ------------------------------------
# CKEditor Integration for Product
# ------------------------------------




class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(), required=False)
    short_description = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'price': NumberInput(attrs={
                'style': 'width: 200px;',
                'class': 'vIntegerField',
                'placeholder': 'قیمت اصلی',
            }),
            'discount_price': NumberInput(attrs={
                'style': 'width: 200px;',
                'class': 'vIntegerField',
                'placeholder': 'قیمت تخفیف (در صورت وجود)',
            }),
            'is_new': CheckboxInput(attrs={
                'style': 'transform: scale(1.3); margin-top: 5px;'
            })
        }


class ProductAddonAdminForm(forms.ModelForm):
    class Meta:
        model = ProductAddon
        fields = '__all__'
        widgets = {
            'additional_cost': NumberInput(attrs={
                'style': 'width: 130px;', 
                'class': 'vIntegerField',
                'placeholder': 'هزینه اضافی (تومان)',
            }),
        }





# ------------------------------------
# Inline: ProductSelectableOption
# ------------------------------------
class ProductSelectableOptionInline(admin.StackedInline):
    model = ProductSelectableOption
    extra = 1
    verbose_name = 'گزینه قابل انتخاب دیگر'
    verbose_name_plural = 'گزینه‌های قابل انتخاب دیگر'
    #filter_horizontal = ['allowed_values']

# ------------------------------------
# Inline: ProductAddon
# ------------------------------------
class ProductAddonInline(admin.TabularInline):
    model = ProductAddon
    form = ProductAddonAdminForm
    extra = 1
    fields = ['name', 'additional_cost', 'is_required', 'is_active', 'sort_order']
    verbose_name = 'افزونه محصول'
    verbose_name_plural = 'افزونه‌های محصول'

# ------------------------------------
# Inline: ProductImageInline
# ------------------------------------
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    max_num = 10
    verbose_name = 'تصویر محصول'
    verbose_name_plural = 'تصاویر محصول'

# ------------------------------------
# Product Admin
# ------------------------------------
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    formfield_overrides = {
        models.IntegerField: {'widget': admin.widgets.AdminTextInputWidget(attrs={'style': 'width: 200px;'})},
    }
    list_filter = ['category', 'is_active']
    list_display = ['title', 'price', 'is_discount_active', 'is_active', 'is_delete', 'has_custom_options']
    list_editable = ['price', 'is_active']
    inlines = [ProductImageInline, ProductSelectableOptionInline, ProductAddonInline]

    def get_inline_instances(self, request, obj=None):
        """
        Only show the inline if the product has has_custom_options=True
        """
        inline_instances = []
        for inline_class in self.inlines:
            if inline_class == ProductSelectableOptionInline:
                # if creating a new product, don't show it
                if obj is None or not obj.has_custom_options:
                    continue
            inline = inline_class(self.model, self.admin_site)
            inline_instances.append(inline)
        return inline_instances

    def save_model(self, request, obj, form, change):
        if not obj.is_discount_active:
            # Optional: clear discount_price if not active
            # obj.discount_price = None
            pass
        super().save_model(request, obj, form, change)



# ------------------------------------
# Product Category Admin
# ------------------------------------
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'is_active', 'is_delete']
    list_editable = ['is_active', 'is_delete']
    search_fields = ['title', 'url_title']


# ------------------------------------
# Product List Page Setting Admin
# ------------------------------------
@admin.register(ProductListPageSetting)
class ProductListPageSettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_editable = ['is_active']


# ------------------------------------
# Product Comment Admin
# ------------------------------------
@admin.register(ProductComment)
class ProductCommentAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['user_full_name', 'user_email', 'product', 'is_verified_buyer', 'created_jalali']
    list_filter = ['is_verified_buyer', 'created_at']
    search_fields = ['user__username', 'user__email', 'product__title', 'text']

    def user_full_name(self, obj):
        return obj.user.get_full_name() or obj.user.username or "نامشخص"
    user_full_name.short_description = "نام کاربر"

    def user_email(self, obj):
        return obj.user.email if obj.user else "ندارد"
    user_email.short_description = "ایمیل"

    def created_jalali(self, obj):
        return date2jalali(obj.created_at).strftime('%Y/%m/%d')
    created_jalali.short_description = "تاریخ ثبت نظر"


# ------------------------------------
# Product Option Types (رنگ نما, گارانتی, ...)
# ------------------------------------
@admin.register(ProductOptionType)
class ProductOptionTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


# ------------------------------------
# Product Option Values (e.g. White, Black)
# ------------------------------------
@admin.register(ProductOptionValue)
class ProductOptionValueAdmin(admin.ModelAdmin):
    list_display = ['option_type', 'value']
    list_filter = ['option_type']
    search_fields = ['value']


# ------------------------------------
# Product Addon Admin
# ------------------------------------
@admin.register(ProductAddon)
class ProductAddonAdmin(admin.ModelAdmin):
    form = ProductAddonAdminForm
    list_display = ['product', 'name', 'additional_cost', 'is_required', 'is_active', 'sort_order']
    list_filter = ['is_active', 'is_required', 'product']
    list_editable = ['additional_cost', 'is_required', 'is_active', 'sort_order']
    search_fields = ['name', 'product__title']
    ordering = ['product', 'sort_order', 'name']
    
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('product', 'name', 'description')
        }),
        ('تنظیمات قیمت و نمایش', {
            'fields': ('additional_cost', 'is_required', 'is_active', 'sort_order')
        }),
    )
