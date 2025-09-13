import random
from django.conf import settings
from kavenegar import KavenegarAPI, APIException, HTTPException
import logging

logger = logging.getLogger(__name__)


class SMSService:
    """Reusable SMS service for sending OTP codes via Kavenegar"""
    
    def __init__(self):
        self.api_key = settings.KAVENEGAR_API_KEY
        self.api = KavenegarAPI(self.api_key)
    
    def send_otp(self, phone_number, template_name, token):
        """
        Send OTP code via SMS
        
        Args:
            phone_number (str): User's phone number
            template_name (str): Kavenegar template name
            token (str): OTP code to send
            
        Returns:
            dict: Response from Kavenegar API or error info
        """
        try:
            params = {
                'receptor': phone_number,
                'template': template_name,
                'token': token,
                'type': 'sms',
            }
            
            response = self.api.verify_lookup(params)
            logger.info(f"SMS sent successfully to {phone_number}")
            return {
                'success': True,
                'response': response,
                'message': 'SMS sent successfully'
            }
            
        except APIException as e:
            logger.error(f"Kavenegar APIException: {str(e)}")
            return {
                'success': False,
                'error': str(e),
                'message': 'مشکلی در ارسال پیامک به وجود آمد'
            }
            
        except HTTPException as e:
            logger.error(f"Kavenegar HTTPException: {str(e)}")
            return {
                'success': False,
                'error': str(e),
                'message': 'مشکلی در ارتباط با سرویس پیامک به وجود آمد'
            }
    
    def send_registration_otp(self, phone_number, otp_code):
        """Send registration OTP"""
        return self.send_otp(
            phone_number, 
            settings.KAVENEGAR_TEMPLATE_REGISTER, 
            otp_code
        )
    
    def send_reset_password_otp(self, phone_number, otp_code):
        """Send password reset OTP"""
        return self.send_otp(
            phone_number, 
            settings.KAVENEGAR_TEMPLATE_RESET, 
            otp_code
        )


def generate_otp_code():
    """Generate a 6-digit OTP code"""
    return random.randint(100000, 999999)


# Convenience functions for easy usage
def send_registration_sms(phone_number, otp_code):
    """Send registration SMS"""
    sms_service = SMSService()
    return sms_service.send_registration_otp(phone_number, otp_code)


def send_reset_password_sms(phone_number, otp_code):
    """Send password reset SMS"""
    sms_service = SMSService()
    return sms_service.send_reset_password_otp(phone_number, otp_code)