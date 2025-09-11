"""
Test script for Zarinpal payment system
Run this script to test the payment functionality
"""

import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mobland.settings')
django.setup()

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Payment, Order
from .zarinpal_utils import create_payment_request, verify_payment, get_payment_url

User = get_user_model()

class PaymentSystemTest:
    """Test class for payment system functionality"""
    
    def __init__(self):
        self.client = Client()
        self.user = None
        
    def setup_test_user(self):
        """Create a test user"""
        try:
            self.user = User.objects.create_user(
                username='testuser',
                email='test@example.com',
                password='testpass123'
            )
            print("✓ Test user created successfully")
            return True
        except Exception as e:
            print(f"✗ Error creating test user: {e}")
            return False
    
    def test_payment_model(self):
        """Test Payment model creation"""
        try:
            payment = Payment.objects.create(
                user=self.user,
                amount=10000,
                description='Test payment',
                status='pending'
            )
            print(f"✓ Payment model test passed - Payment ID: {payment.id}")
            return True
        except Exception as e:
            print(f"✗ Payment model test failed: {e}")
            return False
    
    def test_payment_form_access(self):
        """Test payment form access"""
        try:
            self.client.force_login(self.user)
            response = self.client.get(reverse('payment_form'))
            if response.status_code == 200:
                print("✓ Payment form access test passed")
                return True
            else:
                print(f"✗ Payment form access test failed - Status: {response.status_code}")
                return False
        except Exception as e:
            print(f"✗ Payment form access test failed: {e}")
            return False
    
    def test_payment_history_access(self):
        """Test payment history access"""
        try:
            response = self.client.get(reverse('payment_history'))
            if response.status_code == 200:
                print("✓ Payment history access test passed")
                return True
            else:
                print(f"✗ Payment history access test failed - Status: {response.status_code}")
                return False
        except Exception as e:
            print(f"✗ Payment history access test failed: {e}")
            return False
    
    def test_zarinpal_utils(self):
        """Test Zarinpal utility functions"""
        try:
            # Test get_payment_url
            url = get_payment_url('test_authority')
            expected_url = 'https://www.zarinpal.com/pg/StartPay/test_authority'
            if url == expected_url:
                print("✓ Zarinpal utils test passed")
                return True
            else:
                print(f"✗ Zarinpal utils test failed - Expected: {expected_url}, Got: {url}")
                return False
        except Exception as e:
            print(f"✗ Zarinpal utils test failed: {e}")
            return False
    
    def cleanup(self):
        """Clean up test data"""
        try:
            if self.user:
                Payment.objects.filter(user=self.user).delete()
                self.user.delete()
            print("✓ Test cleanup completed")
        except Exception as e:
            print(f"✗ Error during cleanup: {e}")
    
    def run_all_tests(self):
        """Run all tests"""
        print("Starting Payment System Tests...")
        print("=" * 50)
        
        tests = [
            self.setup_test_user,
            self.test_payment_model,
            self.test_payment_form_access,
            self.test_payment_history_access,
            self.test_zarinpal_utils,
        ]
        
        passed = 0
        total = len(tests)
        
        for test in tests:
            if test():
                passed += 1
            print()
        
        print("=" * 50)
        print(f"Test Results: {passed}/{total} tests passed")
        
        if passed == total:
            print("🎉 All tests passed! Payment system is ready to use.")
        else:
            print("⚠️  Some tests failed. Please check the errors above.")
        
        self.cleanup()
        return passed == total

if __name__ == '__main__':
    tester = PaymentSystemTest()
    tester.run_all_tests()
