"""
Zarinpal Payment Gateway Utility Functions
"""
import requests
from django.conf import settings
from django.urls import reverse


def create_payment_request(amount, description, callback_url, metadata=None):
    """
    Create a payment request with Zarinpal API
    
    Args:
        amount (int): Amount in Rials (already converted from Toman)
        description (str): Payment description
        callback_url (str): Callback URL for payment verification
        metadata (dict): Additional metadata
    
    Returns:
        dict: API response
    """
    data = {
        'merchant_id': settings.ZARINPAL_MERCHANT_ID,
        'amount': amount,
        'description': description,
        'callback_url': callback_url,
    }
    
    if metadata:
        data['metadata'] = metadata
    
    try:
        response = requests.post(
            'https://api.zarinpal.com/pg/v4/request.json',
            json=data,
            timeout=30
        )
        return response.json()
    except requests.RequestException as e:
        return {
            'data': {'code': -1, 'message': f'Connection error: {str(e)}'},
            'errors': {'message': 'خطا در ارتباط با درگاه پرداخت'}
        }


def verify_payment(amount, authority):
    """
    Verify payment with Zarinpal API
    
    Args:
        amount (int): Amount in Rials (already converted from Toman)
        authority (str): Payment authority code
    
    Returns:
        dict: API response
    """
    data = {
        'merchant_id': settings.ZARINPAL_MERCHANT_ID,
        'amount': amount,
        'authority': authority
    }
    
    try:
        response = requests.post(
            'https://api.zarinpal.com/pg/v4/verify.json',
            json=data,
            timeout=30
        )
        return response.json()
    except requests.RequestException as e:
        return {
            'data': {'code': -1, 'message': f'Connection error: {str(e)}'},
            'errors': {'message': 'خطا در تأیید پرداخت'}
        }


def get_payment_url(authority):
    """
    Get Zarinpal payment URL
    
    Args:
        authority (str): Payment authority code
    
    Returns:
        str: Payment URL
    """
    return f"https://www.zarinpal.com/pg/StartPay/{authority}"


def format_amount(amount):
    """
    Format amount for display
    
    Args:
        amount (int): Amount in Rials
    
    Returns:
        str: Formatted amount
    """
    return f"{amount:,} ریال"
