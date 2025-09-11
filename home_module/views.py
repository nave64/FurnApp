from django.db.models import Prefetch, Count, Q
from django.shortcuts import render
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView
from home_module.models import HomeVideoSection, DepartmentCard, RulesPage, ShipmentPage, PaymentMethodsPage, \
    RefundTermsPage
from home_module.models import HotDealProduct, FurnitureSubCategory, FurnitureMainCategory
from product_module.models import Product, ProductCategory
from site_module.models import SiteSettings

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home_module/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # ➤ Latest products
        latest_products = Product.objects.filter(
            is_active=True,
            is_delete=False
        ).order_by('-id')[:4]
        context['latest_products'] = latest_products

        # ➤ Furniture sections: Main categories + subcategories + all products
        main_cats = []
        for cat in FurnitureMainCategory.objects.filter(is_active=True).order_by('order'):
            subcats = FurnitureSubCategory.objects.filter(
                is_active=True,
                main_category=cat
            ).prefetch_related('products')

            all_products = Product.objects.filter(
                furnituresubcategory__in=subcats,
                is_active=True,
                is_delete=False
            ).distinct()

            # Attach data
            cat.subcats = subcats
            cat.all_subcat_products = all_products
            main_cats.append(cat)

        context['furniture_main_categories'] = main_cats

        # ➤ Hot deal section
        hotdeal_setting = HotDealProduct.objects.first()
        context['hotdeal_setting'] = hotdeal_setting

        if hotdeal_setting and hotdeal_setting.is_active:
            hot_deal_entries = HotDealProduct.objects.select_related('product').filter(
                product__is_active=True,
                product__is_delete=False,
                countdown_expiry__gt=timezone.now()
            ).order_by('priority')[:5]
            context['hot_deals'] = hot_deal_entries

            if hot_deal_entries:
                context['hot_deal_expiry'] = hot_deal_entries[0].countdown_expiry
        else:
            context['hot_deals'] = []
            context['hot_deal_expiry'] = None

        # ➤ Home page video section
        context['home_video'] = HomeVideoSection.objects.filter(is_active=True).first()

        # ➤ Product categories for “بررسی همه بخش‌ها” section
        dynamic_categories = ProductCategory.objects.filter(
            is_active=True,
            is_delete=False
        ).annotate(
            product_count=Count(
                'product_categories',
                filter=Q(product_categories__is_active=True, product_categories__is_delete=False)
            )
        )
        context['dynamic_categories'] = dynamic_categories
        context['department_cards'] = DepartmentCard.objects.filter(
            is_active=True
        ).order_by('id')[:4]

        return context


def rules_page(request):
    rule = RulesPage.objects.filter(is_active=True).first()
    return render(request, 'home_module/rules_page.html', {'rule': rule})


def shipment_page(request):
    shipment = ShipmentPage.objects.filter(is_active=True).first()
    return render(request, 'home_module/shipment.html', {'shipment': shipment})


def payment_methods_page(request):
    payment = PaymentMethodsPage.objects.filter(is_active=True).first()
    return render(request, 'home_module/payment_methods.html', {'payment': payment})


def refund_terms_page(request):
    refund = RefundTermsPage.objects.filter(is_active=True).first()
    return render(request, 'home_module/refund_terms_page.html', {'refund': refund})


def site_header_partial(request):
    setting: SiteSettings = SiteSettings.objects.filter(is_main_settings=True).first()
    context = {
        'site_settings': setting
    }
    return render(request, 'shared/site_header_partial.html', context)


def site_footer_partial(request):
    setting: SiteSettings = SiteSettings.objects.filter(is_main_settings=True).first()
    context = {
        'site_settings': setting
    }
    return render(request, 'shared/site_footer_partial.html', context)






