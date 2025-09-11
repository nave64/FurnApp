import os
import requests
import json
from datetime import time
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse, HttpResponse, request
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib import messages
from product_module.models import Product
from user_panel_module.views import confirm_payment
from .models import Order, OrderDetail, Payment
from .forms import PaymentForm
from django.conf import settings
from django.db import models

def make_zarinpal_graphql_request(query, variables=None):
    """
    Make a GraphQL request to Zarinpal API
    """
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {settings.ZARINPAL_ACCESS_TOKEN}'
    }
    
    data = {
        'query': query,
        'variables': variables or {}
    }
    
    try:
        response = requests.post(ZP_GRAPHQL_ENDPOINT, json=data, headers=headers)
        return response.json()
    except Exception as e:
        return {
            'success': False,
            'errors': [{'message': f'Request failed: {str(e)}'}]
        }

# Zarinpal API URLs - Updated to use new GraphQL API
ZP_GRAPHQL_ENDPOINT = "https://next.zarinpal.com/api/v4/graphql/"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"

# GraphQL Queries for Zarinpal API
ZP_PAYMENT_REQUEST_QUERY = """
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
"""

ZP_PAYMENT_VERIFY_QUERY = """
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
"""

# Create your views here
description = 'پرداخت اصفهان ابزار '
callback_url = 'https://abzaresf.ir/order/verify/'


def add_product_to_order(request: HttpRequest):
    # Handle both GET and POST requests
    if request.method == 'POST':
        product_id = int(request.POST.get('product_id'))
        count = int(request.POST.get('count'))
        selected_addons_json = request.POST.get('selected_addons', '[]')
        
        try:
            selected_addons = json.loads(selected_addons_json)
            # Convert string IDs to integers
            selected_addons = [int(addon_id) for addon_id in selected_addons if str(addon_id).isdigit()]
        except (json.JSONDecodeError, ValueError):
            selected_addons = []
    else:
        product_id = int(request.GET.get('product_id'))
        count = int(request.GET.get('count'))
        selected_addons_json = request.GET.get('selected_addons', '[]')
        
        try:
            selected_addons = json.loads(selected_addons_json)
            # Convert string IDs to integers
            selected_addons = [int(addon_id) for addon_id in selected_addons if str(addon_id).isdigit()]
        except (json.JSONDecodeError, ValueError):
            selected_addons = []

    if count < 1:
        return JsonResponse({
            'status': 'invalid_count',
            'text': 'مقدار وارد شده معتبر نمی باشد',
            'confirm_button_text': 'مرسی از شما',
            'icon': 'warning'
        })

    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()

        if product is not None:
            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            
            # Check if there's already an order detail with the same product and add-ons
            existing_details = current_order.orderdetail_set.filter(product_id=product_id)
            current_order_detail = None
            
            # Find matching order detail with same add-ons
            for detail in existing_details:
                if set(detail.selected_addons) == set(selected_addons):
                    current_order_detail = detail
                    break
            
            # Debug logging
            print(f"DEBUG: Product ID: {product_id}")
            print(f"DEBUG: Selected addons: {selected_addons}")
            print(f"DEBUG: Selected addons type: {type(selected_addons)}")

            # Calculate the final price (discounted price if available, otherwise the original price)
            final_price = product.discount_price if product.is_discount_active and product.discount_price else product.price

            if current_order_detail is not None:
                current_order_detail.count += count
                current_order_detail.final_price = final_price
                current_order_detail.save()
            else:
                new_detail = OrderDetail(
                    order_id=current_order.id,
                    product_id=product_id,
                    count=count,
                    final_price=final_price,
                    selected_addons=selected_addons
                )
                new_detail.save()
                print(f"DEBUG: Created new OrderDetail with selected_addons: {new_detail.selected_addons}")

            # Calculate cart count for response
            cart_count = current_order.orderdetail_set.aggregate(
                total_count=models.Sum('count')
            )['total_count'] or 0

            return JsonResponse({
                'status': 'success',
                'text': 'محصول مورد نظر با موفقیت به سبد خرید شما اضافه شد',
                'confirm_button_text': 'باشه ممنونم',
                'icon': 'success',
                'success': True,
                'cart_count': cart_count
            })
        else:
            return JsonResponse({
                'status': 'not_found',
                'text': 'محصول مورد نظر یافت نشد',
                'confirm_button_text': 'مرسییییی',
                'icon': 'error',
                'success': False,
                'message': 'محصول یافت نشد'
            })
    else:
        return JsonResponse({
            'status': 'not_auth',
            'text': 'برای افزودن محصول به سبد خرید ابتدا می بایست وارد سایت شوید',
            'confirm_button_text': 'ورود به سایت',
            'icon': 'error',
            'success': False,
            'message': 'احراز هویت مورد نیاز است'
        })


@login_required
def confirm_payment_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if request.method == 'POST':
        # Simulate payment success
        confirm_payment(order)
        return redirect('order_success')  # Redirect to a success page

    context = {
        'order': order,
        'total_amount': order.calculate_total_price()
    }
    return render(request, 'payment_result.html', context)


# New Zarinpal Payment Views
@method_decorator(login_required, name='dispatch')
class PaymentView(View):
    """View for displaying payment form and processing payment requests"""
    
    def get(self, request):
        form = PaymentForm()
        return render(request, 'order_module/payment_form.html', {'form': form})
    
    def post(self, request):
        form = PaymentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount'] * 10  # Convert from Toman to Rials
            description = form.cleaned_data['description'] or 'پرداخت از طریق درگاه زرین‌پال'
            
            # Create payment record
            payment = Payment.objects.create(
                user=request.user,
                amount=amount,
                description=description,
                status='pending'
            )
            
            # Check if mock mode is enabled
            if getattr(settings, 'ZARINPAL_MOCK_MODE', False):
                print("Mock Mode: Simulating payment request")
                # Simulate successful payment request
                mock_authority = f"mock_authority_{int(timezone.now().timestamp())}"
                payment.authority = mock_authority
                payment.save()
                
                # Simulate redirect to payment page
                return render(request, 'order_module/mock_payment.html', {
                    'authority': mock_authority,
                    'amount': amount,
                    'payment': payment
                })
            
            # Use new GraphQL API
            try:
                variables = {
                    'input': {
                        'merchantId': settings.ZARINPAL_MERCHANT_ID,
                        'amount': amount,
                        'description': description,
                        'callbackUrl': request.build_absolute_uri(reverse('payment_verify'))
                    }
                }
                
                response = make_zarinpal_graphql_request(ZP_PAYMENT_REQUEST_QUERY, variables)
                print(f"GraphQL Response: {response}")
                
                if response.get('data', {}).get('createPaymentRequest', {}).get('success'):
                    payment_data = response['data']['createPaymentRequest']['data']
                    authority = payment_data['authority']
                    payment_url = payment_data['paymentUrl']
                    
                    payment.authority = authority
                    payment.save()
                    
                    return redirect(payment_url)
                else:
                    errors = response.get('data', {}).get('createPaymentRequest', {}).get('errors', [])
                    error_msg = errors[0]['message'] if errors else 'Unknown error'
                    messages.error(request, f'خطا در ایجاد درخواست پرداخت: {error_msg}')
                    payment.status = 'failed'
                    payment.save()
                    
            except Exception as e:
                print(f"Exception: {str(e)}")
                messages.error(request, f'خطا در ارتباط با درگاه پرداخت: {str(e)}')
                payment.status = 'failed'
                payment.save()
        
        return render(request, 'order_module/payment_form.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class OrderPaymentView(View):
    """View for processing order payments"""
    
    def get(self, request):
        current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
        total_price = current_order.calculate_total_price() * 10  # Convert from Toman to Rials
        
        if total_price == 0:
            messages.warning(request, 'سبد خرید شما خالی است.')
            return redirect(reverse('user_basket_page'))

        # Create payment record for order
        payment = Payment.objects.create(
            user=request.user,
            order=current_order,
            amount=total_price,
            description=f'پرداخت سفارش شماره {current_order.id}',
            status='pending'
        )

        # Check if mock mode is enabled
        if getattr(settings, 'ZARINPAL_MOCK_MODE', False):
            print("Mock Mode: Simulating payment request")
            # Simulate successful payment request
            mock_authority = f"mock_authority_{int(timezone.now().timestamp())}"
            payment.authority = mock_authority
            payment.save()
            
            # Simulate redirect to payment page
            return render(request, 'order_module/mock_payment.html', {
                'authority': mock_authority,
                'amount': total_price,
                'payment': payment
            })
        
        # Use new GraphQL API
        try:
            variables = {
                'input': {
                    'merchantId': settings.ZARINPAL_MERCHANT_ID,
                    'amount': total_price,
                    'description': f'پرداخت سفارش شماره {current_order.id}',
                    'callbackUrl': request.build_absolute_uri(reverse('payment_verify'))
                }
            }
            
            response = make_zarinpal_graphql_request(ZP_PAYMENT_REQUEST_QUERY, variables)
            print(f"GraphQL Response: {response}")
            
            if response.get('data', {}).get('createPaymentRequest', {}).get('success'):
                payment_data = response['data']['createPaymentRequest']['data']
                authority = payment_data['authority']
                payment_url = payment_data['paymentUrl']
                
                payment.authority = authority
                payment.save()
                
                return redirect(payment_url)
            else:
                errors = response.get('data', {}).get('createPaymentRequest', {}).get('errors', [])
                error_msg = errors[0]['message'] if errors else 'Unknown error'
                messages.error(request, f'خطا در ایجاد درخواست پرداخت: {error_msg}')
                payment.status = 'failed'
                payment.save()
                return redirect(reverse('user_basket_page'))
                
        except Exception as e:
            print(f"Exception: {str(e)}")
            messages.error(request, f'خطا در ارتباط با درگاه پرداخت: {str(e)}')
            payment.status = 'failed'
            payment.save()
            return redirect(reverse('user_basket_page'))


class PaymentVerifyView(View):
    """View for verifying payment after callback from Zarinpal"""
    
    def get(self, request):
        authority = request.GET.get('Authority')
        status = request.GET.get('Status')
        
        print(f"PaymentVerifyView - Authority: {authority}, Status: {status}")
        
        if not authority:
            messages.error(request, 'کد مرجع پرداخت یافت نشد.')
            return render(request, 'order_module/payment_result_failed.html')
        
        # Check if this is a mock payment first
        if authority.startswith('mock_authority_'):
            try:
                payment = Payment.objects.get(authority=authority, status='pending')
                return self.handle_mock_payment(request, payment, status)
            except Payment.DoesNotExist:
                messages.error(request, 'پرداخت آزمایشی یافت نشد.')
                return render(request, 'order_module/payment_result_failed.html')
        
        try:
            payment = Payment.objects.get(authority=authority, status='pending')
        except Payment.DoesNotExist:
            messages.error(request, 'پرداخت یافت نشد.')
            return render(request, 'order_module/payment_result_failed.html')
        
        if status == 'OK':
            # Verify payment with Zarinpal using GraphQL
            try:
                variables = {
                    'input': {
                        'merchantId': settings.ZARINPAL_MERCHANT_ID,
                        'amount': payment.amount,
                        'authority': authority
                    }
                }
                
                response = make_zarinpal_graphql_request(ZP_PAYMENT_VERIFY_QUERY, variables)
                print(f"GraphQL Verify Response: {response}")
                
                if response.get('data', {}).get('verifyPayment', {}).get('success'):
                    # Payment successful
                    verify_data = response['data']['verifyPayment']['data']
                    payment.status = 'success'
                    payment.ref_id = verify_data['refId']
                    payment.payment_date = timezone.now()
                    payment.save()
                    
                    # If payment is for an order, mark it as paid
                    if payment.order:
                        payment.order.is_paid = True
                        payment.order.payment_date = timezone.now().date()
                        payment.order.save()
                    
                    messages.success(request, 'پرداخت با موفقیت انجام شد.')
                    return render(request, 'order_module/payment_result.html', {
                        'payment': payment,
                        'status': 'success'
                    })
                else:
                    # Payment verification failed
                    errors = response.get('data', {}).get('verifyPayment', {}).get('errors', [])
                    error_msg = errors[0]['message'] if errors else 'Verification failed'
                    payment.status = 'failed'
                    payment.save()
                    messages.error(request, f'تأیید پرداخت ناموفق بود: {error_msg}')
                    return render(request, 'order_module/payment_result_failed.html', {
                        'payment': payment,
                        'status': 'verification_failed'
                    })
                    
            except Exception as e:
                payment.status = 'failed'
                payment.save()
                messages.error(request, f'خطا در تأیید پرداخت: {str(e)}')
                return render(request, 'order_module/payment_result_failed.html', {
                    'payment': payment,
                    'status': 'verification_error'
                })
        else:
            # Payment cancelled or failed
            payment.status = 'cancelled'
            payment.save()
            messages.warning(request, 'پرداخت لغو شد.')
            return render(request, 'order_module/payment_result_cancelled.html', {
                'payment': payment,
                'status': 'cancelled'
            })
    
    def handle_mock_payment(self, request, payment, status):
        """Handle mock payment verification"""
        print(f"handle_mock_payment - Status: {status}")
        
        if status == 'OK':
            # Mock successful payment
            payment.status = 'success'
            payment.ref_id = f"MOCK_{int(timezone.now().timestamp())}"
            payment.payment_date = timezone.now()
            payment.save()
            
            # If payment is for an order, mark it as paid
            if payment.order:
                payment.order.is_paid = True
                payment.order.payment_date = timezone.now().date()
                payment.order.save()
            
            messages.success(request, 'پرداخت آزمایشی با موفقیت انجام شد!')
            return render(request, 'order_module/payment_result.html', {
                'payment': payment,
                'status': 'success'
            })
        elif status == 'NOK':
            # Mock failed payment
            payment.status = 'failed'
            payment.save()
            messages.error(request, 'پرداخت آزمایشی ناموفق بود.')
            return render(request, 'order_module/payment_result_failed.html', {
                'payment': payment,
                'status': 'failed'
            })
        elif status == 'CANCELLED':
            # Mock cancelled payment
            payment.status = 'cancelled'
            payment.save()
            messages.warning(request, 'پرداخت آزمایشی لغو شد.')
            return render(request, 'order_module/payment_result_cancelled.html', {
                'payment': payment,
                'status': 'cancelled'
            })
        else:
            # Default to failed for unknown status
            payment.status = 'failed'
            payment.save()
            messages.error(request, f'وضعیت نامشخص پرداخت: {status}')
            return render(request, 'order_module/payment_result_failed.html', {
                'payment': payment,
                'status': 'failed'
            })


class PaymentHistoryView(View):
    """View for displaying user's payment history"""
    
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        
        payments = Payment.objects.filter(user=request.user).order_by('-created_at')
        return render(request, 'order_module/payment_history.html', {'payments': payments})


# Legacy views for backward compatibility
@method_decorator(login_required, name='dispatch')
class OrderPayView(View):
    def get(self, request):
        current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
        total_price = current_order.calculate_total_price() * 10  # Convert from Toman to Rials
        if total_price == 0:
            return redirect(reverse('user_basket_page'))

        description = "Your payment description"  # Add a description for the payment
        callback_url = request.build_absolute_uri(reverse('payment_callback'))  # Use the correct name here

        data = {
            'MerchantID': settings.ZARINPAL_MERCHANT_ID,
            'Amount': total_price,
            'Description': description,
            'CallbackURL': callback_url,
        }
        data_json = json.dumps(data)
        headers = {'content-type': 'application/json', 'content-length': str(len(data_json))}
        
        # Debug information
        print(f"Payment Request Data: {data}")
        print(f"Merchant ID: {settings.ZARINPAL_MERCHANT_ID}")
        print(f"Amount: {total_price}")
        
        # Check if mock mode is enabled
        if getattr(settings, 'ZARINPAL_MOCK_MODE', False):
            print("Mock Mode: Simulating payment request")
            # Simulate successful payment request
            mock_authority = f"mock_authority_{int(timezone.now().timestamp())}"
            
            # Create payment record
            payment = Payment.objects.create(
                user=request.user,
                order=current_order,
                amount=total_price,
                authority=mock_authority,
                description=description,
                status='pending'
            )
            
            # Simulate redirect to payment page
            return render(request, 'order_module/mock_payment.html', {
                'authority': mock_authority,
                'amount': total_price,
                'payment': payment
            })
        
        # Use new GraphQL API
        try:
            variables = {
                'input': {
                    'merchantId': settings.ZARINPAL_MERCHANT_ID,
                    'amount': total_price,
                    'description': description,
                    'callbackUrl': callback_url
                }
            }
            
            response = make_zarinpal_graphql_request(ZP_PAYMENT_REQUEST_QUERY, variables)
            print(f"GraphQL Response: {response}")
            
            if response.get('data', {}).get('createPaymentRequest', {}).get('success'):
                payment_data = response['data']['createPaymentRequest']['data']
                authority = payment_data['authority']
                payment_url = payment_data['paymentUrl']
                
                # Create payment record
                payment = Payment.objects.create(
                    user=request.user,
                    order=current_order,
                    amount=total_price,
                    authority=authority,
                    description=description,
                    status='pending'
                )
                
                return redirect(payment_url)
            else:
                errors = response.get('data', {}).get('createPaymentRequest', {}).get('errors', [])
                error_msg = errors[0]['message'] if errors else 'Unknown error'
                return JsonResponse({'error': f'Payment request failed: {error_msg}'}, status=400)
                
        except Exception as e:
            print(f"Exception: {str(e)}")
            return JsonResponse({'error': f'Request failed: {str(e)}'}, status=400)


class CallbackView(View):
    def get(self, request):
        return HttpResponse('Payment callback received')


@method_decorator(login_required, name='dispatch')
class VerifyPayView(View):
    def get(self, request):
        current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
        total_price = current_order.calculate_total_price()
        authority = request.GET['Authority']
        data = {
            'MerchantID': settings.ZARINPAL_MERCHANT_ID,
            'Amount': total_price,
            'Authority': authority,
        }
        data = json.dumps(data)
        headers = {'content-type': 'application/json', 'content-length': str(len(data))}
        res = requests.post(ZP_API_VERIFY, data=data, headers=headers)
        if res.status_code == 200:
            response = res.json()
            if response['Status'] == 100:
                # return HttpResponse({'Status': response['پرداخت با شکست مواجه شد '], 'RefID': response['RefID']})
                return render(request, 'payment_result.html')

            else:
                # return HttpResponse({'Status': response['پرداخت با شکست مواجه شد'], 'RefID': response['RefID']})
                return render(request, 'payment_result_failed.html')
        else:
            return HttpResponse('پرداخت ناموفق')


# SamanEPay Views (keeping existing implementation)
@method_decorator(login_required, name='dispatch')
class SamanEPayView(View):
    def get(self, request):
        current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
        total_price = current_order.calculate_total_price() * 10  # Add an extra zero to the amount
        if total_price == 0:
            return redirect(reverse('user_basket_page'))

        # Prepare data for token request
        token_request_data = {
            'action': 'token',
            'TerminalId': settings.SAMANEPAY_MID,
            'Amount': total_price,
            'ResNum': str(current_order.id),
            'RedirectUrl': settings.SAMANEPAY_REDIRECT_URL,
        }

        # Send token request
        token_response = requests.post('https://acquirer.samanepay.com/payment.aspx', json=token_request_data)

        # Debugging: Print the raw response content
        print("Raw response content:", token_response.content)

        try:
            token_response_data = token_response.json()
        except json.JSONDecodeError as e:
            return JsonResponse({
                'status': 'error',
                'message': 'Failed to decode JSON response',
                'raw_response': token_response.content.decode('utf-8')
            }, status=400)

        if token_response_data.get('status') == 1:
            token = token_response_data.get('token')
            payment_url = f"https://sep.shaparak.ir/OnlinePG/SendToken?token={token}"
            return redirect(payment_url)
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'Token request failed',
                'errorCode': token_response_data.get('errorCode'),
                'errorDesc': token_response_data.get('errorDesc')
            }, status=400)


class SamanEPayCallbackView(View):
    def get(self, request):
        ref_num = request.GET.get('RefNum')
        res_num = request.GET.get('ResNum')
        state = request.GET.get('state')

        if state == 'OK':
            # Verify the transaction
            verify_url = 'https://acquirer.samanepay.com/verify.aspx'
            verify_data = {
                'RefNum': ref_num,
                'MID': settings.SAMANEPAY_MID,
            }

            response = requests.post(verify_url, data=verify_data)

            if response.status_code == 200:
                print(response.json())  # Debugging statement
                verify_result = response.json()
                if verify_result.get('status') == 'success':
                    order = Order.objects.get(id=res_num)
                    order.is_paid = True
                    order.save()
                    return render(request, 'payment_result.html', {'status': 'success'})
                else:
                    print("Verification failed:", verify_result)  # Debugging statement
                    return render(request, 'payment_result_failed.html', {'status': 'verification_failed'})
            else:
                print("Verification request failed with status code", response.status_code)  # Debugging statement
                return render(request, 'payment_result_failed.html', {'status': 'verification_error'})
        else:
            print("Payment failed with state", state)  # Debugging statement
            return render(request, 'payment_result_failed.html', {'status': 'payment_failed'})