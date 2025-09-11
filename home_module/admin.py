from django.contrib import admin
from .models import HomeVideoSection, DepartmentCard, ShipmentPage, PaymentMethodsPage, RefundTermsPage
from django.core.exceptions import ValidationError
from django.contrib import admin
from .models import HotDealProduct
from django.contrib import admin
from django.contrib import admin
from .models import FurnitureSubCategory
from .models import FurnitureMainCategory, FurnitureSubCategory


@admin.register(HomeVideoSection)
class HomeVideoSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']


class HotDealProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'priority']

    def save_model(self, request, obj, form, change):
        if not change and HotDealProduct.objects.count() >= 5:
            raise ValidationError("حداکثر ۵ محصول می‌توانند به عنوان پیشنهاد شگفت‌انگیز انتخاب شوند.")
        super().save_model(request, obj, form, change)



# admin.py


class FurnitureSubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'is_active']
    filter_horizontal = ['products']  # Easier UI for selecting products



# admin.py


# admin.py


@admin.register(DepartmentCard)
class DepartmentCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active')
    list_filter = ('category', 'is_active')




# home_module/admin.py
from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import RulesPage

class RulesPageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = RulesPage
        fields = '__all__'

@admin.register(RulesPage)
class RulesPageAdmin(admin.ModelAdmin):
    form = RulesPageAdminForm
    list_display = ['title', 'is_active']
    list_editable = ['is_active']


class ShipmentPageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = ShipmentPage
        fields = '__all__'



class PaymentMethodsPageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = PaymentMethodsPage
        fields = '__all__'


@admin.register(PaymentMethodsPage)
class PaymentMethodsPageAdmin(admin.ModelAdmin):
    form = PaymentMethodsPageAdminForm
    list_display = ['title', 'is_active']
    list_editable = ['is_active']


class RefundTermsPageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = RefundTermsPage
        fields = '__all__'


@admin.register(RefundTermsPage)
class RefundTermsPageAdmin(admin.ModelAdmin):
    form = RefundTermsPageAdminForm
    list_display = ['title', 'is_active']
    list_editable = ['is_active']
@admin.register(ShipmentPage)
class ShipmentPageAdmin(admin.ModelAdmin):
    form = ShipmentPageAdminForm
    list_display = ['title', 'is_active']
    list_editable = ['is_active']

admin.site.register(FurnitureMainCategory)
admin.site.register(FurnitureSubCategory)
admin.site.register(HotDealProduct, HotDealProductAdmin)



