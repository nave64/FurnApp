# Zarinpal Production Setup Guide

## 🚀 Production Configuration

### Required Environment Variables

Set these environment variables in your production environment (Liara dashboard):

```bash
# Zarinpal Production Configuration
ZARINPAL_MERCHANT_ID=your_real_merchant_id_here
ZARINPAL_ACCESS_TOKEN=your_real_access_token_here
ZARINPAL_SANDBOX=False
ZARINPAL_CALLBACK_URL=https://yourdomain.com/order/payment-verify/
ZARINPAL_MOCK_MODE=False

# Site Configuration
SITE_URL=https://yourdomain.com
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DEBUG=False
```

### 🔧 How to Get Zarinpal Credentials

1. **Register at Zarinpal**: Go to [zarinpal.com](https://zarinpal.com)
2. **Get Merchant ID**: From your Zarinpal dashboard
3. **Get Access Token**: Generate OAuth 2.0 token for GraphQL API
4. **Configure Callback URL**: Set your production domain

### ✅ Payment Flow Verification

The system will work correctly in production because:

1. **Dynamic Callback URLs**: Uses `request.build_absolute_uri(reverse('payment_verify'))`
2. **Environment Variables**: All settings loaded from environment
3. **GraphQL API**: Uses modern Zarinpal GraphQL API
4. **Error Handling**: Comprehensive error handling and validation
5. **Production Validation**: Checks for proper configuration

### 🔍 Testing Production Setup

1. **Check Configuration**:
   ```python
   # These should NOT be default values in production
   assert settings.ZARINPAL_MERCHANT_ID != 'test'
   assert settings.ZARINPAL_ACCESS_TOKEN != 'YOUR_ACCESS_TOKEN'
   assert settings.ZARINPAL_SANDBOX == False
   assert settings.ZARINPAL_MOCK_MODE == False
   ```

2. **Test Payment Flow**:
   - Create payment request
   - Redirect to Zarinpal
   - Complete payment
   - Verify callback
   - Check payment status

### 🚨 Common Issues & Solutions

#### Issue: "Zarinpal access token not configured"
**Solution**: Set `ZARINPAL_ACCESS_TOKEN` environment variable

#### Issue: "Zarinpal merchant ID not configured"  
**Solution**: Set `ZARINPAL_MERCHANT_ID` environment variable

#### Issue: Callback URL mismatch
**Solution**: Ensure `ZARINPAL_CALLBACK_URL` matches your domain

#### Issue: Payment verification fails
**Solution**: Check that `ZARINPAL_SANDBOX=False` in production

### 📋 Production Checklist

- [ ] Set real Zarinpal merchant ID
- [ ] Set real Zarinpal access token  
- [ ] Set `ZARINPAL_SANDBOX=False`
- [ ] Set `ZARINPAL_MOCK_MODE=False`
- [ ] Set correct callback URL
- [ ] Set production domain in `ALLOWED_HOSTS`
- [ ] Set `DEBUG=False`
- [ ] Test payment flow end-to-end

### 🔒 Security Notes

- Never commit real credentials to code
- Use environment variables for all sensitive data
- Enable HTTPS in production
- Monitor payment logs for suspicious activity
