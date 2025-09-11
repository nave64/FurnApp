from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpRequest, JsonResponse, Http404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from django.views import View
from django.contrib.auth import logout
from account_module.models import User
from order_module.models import Order, OrderDetail
from .forms import EditProfileModelForm, ChangePasswordForm, UserImageUploadForm
from django.utils.decorators import method_decorator
from product_module.models import Product
# from .models import Transportation
from django.utils import timezone

# Create your views here.


@method_decorator(login_required, name='dispatch')
class UserPanelDashboardPage(TemplateView):
    template_name = 'user_panel_module/user_panel_menu_component.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context



@method_decorator(login_required, name='dispatch')
class EditUserProfilePage(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(instance=current_user)
        context = {
            'form': edit_form
        }
        return render(request, 'user_panel_module/edit_user_page.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)
        context = {
            'form': edit_form
        }

        # Inside post() method
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, '✅ اطلاعات شما با موفقیت ذخیره شد.')
            return redirect('edit-user-profile_urls')  # Redirect back to the form page

        return render(request, 'user_panel_module/edit_user_page.html', context)


from django.contrib import messages


@method_decorator(login_required, name='dispatch')
class ChangePasswordPage(View):
    def get(self, request: HttpRequest):
        success_message = request.session.pop('password_change_success', None)
        context = {
            'form': ChangePasswordForm(),
            'success_message': success_message
        }
        return render(request, 'change_password_page.html', context)

    def post(self, request: HttpRequest):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_user: User = User.objects.filter(id=request.user.id).first()
            if current_user.check_password(form.cleaned_data.get('current_password')):
                current_user.set_password(form.cleaned_data.get('password'))
                current_user.save()

                # Store success message in session before logout
                request.session['password_change_success'] = 'رمز عبور با موفقیت تغییر یافت. لطفاً مجدداً وارد شوید.'

                logout(request)
                return redirect(reverse('login_page'))
            else:
                form.add_error('password', 'کلمه عبور فعلی اشتباه است.')

        context = {
            'form': form
        }
        return render(request, 'change_password_page.html', context)


@method_decorator(login_required, name='dispatch')
class MyShoppingsView(ListView):
    model = Order
    template_name = 'user_panel_module/user_shoppings.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        request: HttpRequest = self.request
        queryset = queryset.filter(user_id = request.user.id, is_paid = True)
        return queryset


@login_required
def user_basket(request: HttpRequest):
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False, user_id=request.user.id)

    if request.method == 'POST':
        for detail in current_order.orderdetail_set.all():
            input_name = f'count_{detail.id}'
            new_count = int(request.POST.get(input_name, detail.count))

            if new_count <= 0:
                detail.delete()
            else:
                detail.count = new_count
                detail.save()

        return redirect('user_basket_page')

    total_amount = current_order.calculate_total_price()

    context = {
        'order': current_order,
        'sum': total_amount
    }
    return render(request, 'user_panel_module/user_basket.html', context)


def confirm_payment(order):
    order.is_paid = True
    order.payment_date = timezone.now()

    for order_detail in order.orderdetail_set.all():
        if order_detail.final_price is None:
            order_detail.final_price = order_detail.product.price
        order_detail.save()

    order.save()





@login_required
def remove_order_detail(request):
    detail_id = request.GET.get('detail_id')
    if detail_id is None:
        return JsonResponse({
            'status': 'not_found_detail_id'
        })

    # current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
    # detail = current_order.orderdetail_set.filter(id=detail_id).first()
    deleted_count, deleted_dict = OrderDetail.objects.filter(id=detail_id, order__is_paid=False,
                                                             order__user_id=request.user.id).delete()
    if deleted_count == 0:
        return JsonResponse({
            'status': 'detail_not_found'
        })
    # detail.delete()

    current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
    total_amount = current_order.calculate_total_price()
    
    # Debug logging
    print(f"DEBUG REMOVE: Order ID: {current_order.id}")
    print(f"DEBUG REMOVE: Total amount calculated: {total_amount}")
    print(f"DEBUG REMOVE: Order details count: {current_order.orderdetail_set.count()}")

    context = {
        'order': current_order,
        'sum': total_amount
    }

    return JsonResponse({
        'status': 'success',
        'body': render_to_string('user_panel_module/user_basket_content.html', context)
    })


@login_required
def change_order_detail_count(request: HttpRequest):
    detail_id = request.GET.get('detail_id')
    state = request.GET.get('state')
    if detail_id is None or state is None:
        return JsonResponse({
            'status': 'not_found_detail_or_state'
        })

    order_detail = OrderDetail.objects.filter(id=detail_id, order__user_id=request.user.id,
                                              order__is_paid=False).first()

    if order_detail is None:
        return JsonResponse({
            'status': 'detail_not_found'
        })

    if state == 'increase':
        order_detail.count += 1
        order_detail.save()
    elif state == 'decrease':
        if order_detail.count == 1:
            order_detail.delete()
        else:
            order_detail.count -= 1
            order_detail.save()
    else:
        return JsonResponse({
            'status': 'state_invalid'
        })

    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                             user_id=request.user.id)
    total_amount = current_order.calculate_total_price()
    
    # Debug logging
    print(f"DEBUG: Order ID: {current_order.id}")
    print(f"DEBUG: Total amount calculated: {total_amount}")
    print(f"DEBUG: Order details count: {current_order.orderdetail_set.count()}")
    for detail in current_order.orderdetail_set.all():
        print(f"DEBUG: Detail {detail.id}: {detail.product.title}, Count: {detail.count}, Price: {detail.final_price}, Subtotal: {detail.count * detail.final_price}")

    context = {
        'order': current_order,
        'sum': total_amount
    }
    return JsonResponse({
        'status': 'success',
        'body': render_to_string('user_panel_module/user_basket_content.html', context)
    })


def my_shopping_detail(request: HttpRequest, order_id):
    order = Order.objects.prefetch_related('orderdetail_set').filter(id=order_id, user_id=request.user.id).first()
    if order is None:
        raise Http404('سبد خرید مورد نظر یافت نشد ')
    return render(request, 'user_panel_module/my_shopping_detail.html',{
        'order':order
    })


@method_decorator(login_required, name='dispatch')
class UserImageUploadView(View):
    def get(self, request):
        form = UserImageUploadForm()
        return render(request, 'user_panel_module/user_upload_img.html', {'form': form})

    def post(self, request):
        form = UserImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, "تصاویر شما با موفقیت ارسال شدند.")
            return redirect('user_panel_urls')  # Redirect to dashboard
        return render(request, 'user_panel_module/user_upload_img.html', {'form': form})


@login_required
def get_cart_count(request):
    """Get the count of items in user's cart"""
    try:
        current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
        count = current_order.orderdetail_set.count()
        return JsonResponse({
            'status': 'success',
            'count': count
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'count': 0
        })
