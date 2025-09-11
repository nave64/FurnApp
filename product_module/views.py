from django.contrib import messages
from django.db.models import Count
from django.http import HttpRequest, HttpResponse, request
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404

from .forms import ProductCommentForm
from .models import Product, ProductComment, Wishlist
from utils.convertors import group_list
from utils.http_service import get_client_ip
from .models import Product, ProductCategory
from site_module.models import SiteSettings
from .models import ProductListPageSetting
from django.views.generic import ListView
from .models import Product, ProductCategory


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 6  # ✅ Show 3products per page

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True, is_delete=False)
        selected_categories = self.request.GET.getlist('category')

        if selected_categories:
            queryset = queryset.filter(category__url_title__in=selected_categories).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.filter(is_active=True, is_delete=False)
        context['selected_categories'] = self.request.GET.getlist('category')
        context['page_setting'] = ProductListPageSetting.objects.filter(is_active=True).first()
        return context


class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()

        context['comments'] = product.comments.all().order_by('-created_at')
        context['form'] = ProductCommentForm()

        context['trending_products'] = (
            Product.objects
            .filter(category__in=product.category.all(), is_active=True, is_delete=False)
            .exclude(id=product.id)
            .distinct()
            .order_by('-id')[:5]
        )
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ProductCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = self.object
            comment.user = request.user
            comment.save()
            return redirect(self.object.get_absolute_url())
        return self.get(request, *args, **kwargs)


@login_required
def add_product_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        is_verified = product.orders.filter(user=request.user, is_paid=True).exists()  # Example logic
        ProductComment.objects.create(
            product=product,
            user=request.user,
            text=text,
            is_verified_buyer=is_verified
        )
    return redirect(product.get_absolute_url())

class AddToCompareView(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        compare_list = request.session.get('compare_list', [])

        if product_id not in compare_list:
            compare_list.append(product_id)
            request.session['compare_list'] = compare_list
            messages.success(request, 'محصول به لیست مقایسه اضافه شد.')

        return redirect('compare_products')  # ✅ Go to Compare Page


class CompareProductsView(TemplateView):
    template_name = 'product_module/compare_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        compare_list = [int(pid) for pid in self.request.session.get('compare_list', [])]

        compared_products = Product.objects.filter(id__in=compare_list)
        available_products = Product.objects.filter(is_active=True, is_delete=False).exclude(id__in=compare_list)

        context['products'] = compared_products
        context['available_products'] = available_products

        # 🚨 Un-comment below if you want to clear the compare list after showing
        # del self.request.session['compare_list']

        return context


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_active=True, is_delete=False)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect(request.META.get('HTTP_REFERER', reverse('product_detail', args=[product_id])))

@login_required
def wishlist_page(request):
    wishlists = Wishlist.objects.filter(user=request.user).select_related('product')
    return render(request, 'product_module/wishlist_page.html', {'wishlists': wishlists})


class AddProductFavorite(View):
    def post(self, request):
        product_id = request.POST["product_id"]
        product = Product.objects.get(pk=product_id)
        request.session["product_favorite"] = product_id
        return redirect(product.get_absolute_url())


def product_categories_component(request: HttpRequest):
    product_categories = ProductCategory.objects.filter(is_active=True, is_delete=False)

    context = {
        'categories': product_categories,

    }
    return render(request, 'components/product_categories_component.html', context)


def clear_compare_list(request):
    if 'compare_list' in request.session:
        del request.session['compare_list']
    messages.info(request, "لیست مقایسه پاک شد.")
    return redirect('compare_products')



def search(request):
    query = request.GET.get('q', '').strip()
    products = Product.objects.filter(title__icontains=query, is_active=True, is_delete=False)

    return render(request, 'components/search.html', {
        'query': query,
        'products': products  # ✅ this matches your template
    })



