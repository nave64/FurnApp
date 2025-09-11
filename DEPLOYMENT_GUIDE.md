# Deployment Guide - Mobland Django E-commerce Platform

This guide covers deploying the Mobland Django application to various hosting platforms.

## 🚀 Quick Deployment Options

### 1. Heroku (Recommended for beginners)

#### Prerequisites
- Heroku CLI installed
- Git repository
- Heroku account

#### Steps
1. **Install Heroku CLI**
   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku App**
   ```bash
   heroku create your-app-name
   ```

4. **Set Environment Variables**
   ```bash
   heroku config:set DJANGO_SETTINGS_MODULE=mobland.settings
   heroku config:set DEBUG=False
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set EMAIL_USER=your-email@gmail.com
   heroku config:set EMAIL_PASSWORD=your-app-password
   heroku config:set RECAPTCHA_PUBLIC_KEY=your-public-key
   heroku config:set RECAPTCHA_PRIVATE_KEY=your-private-key
   heroku config:set ZARINPAL_MERCHANT_ID=your-merchant-id
   heroku config:set ZARINPAL_ACCESS_TOKEN=your-access-token
   heroku config:set KAVENEGAR_API_KEY=your-api-key
   ```

5. **Add PostgreSQL Database**
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

6. **Deploy**
   ```bash
   git push heroku main
   ```

7. **Run Migrations**
   ```bash
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   heroku run python manage.py collectstatic
   ```

### 2. Railway

#### Steps
1. **Connect GitHub Repository**
   - Go to Railway.app
   - Connect your GitHub account
   - Select your repository

2. **Configure Environment Variables**
   - Add all required environment variables in Railway dashboard
   - Set `DJANGO_SETTINGS_MODULE=mobland.settings`

3. **Deploy**
   - Railway automatically deploys on git push
   - Check logs for any issues

### 3. DigitalOcean App Platform

#### Steps
1. **Create App**
   - Go to DigitalOcean App Platform
   - Create new app from GitHub

2. **Configure App Spec**
   ```yaml
   name: mobland
   services:
   - name: web
     source_dir: /
     github:
       repo: yourusername/mobland
       branch: main
     run_command: gunicorn mobland.wsgi:application
     environment_slug: python
     instance_count: 1
     instance_size_slug: basic-xxs
     envs:
     - key: DJANGO_SETTINGS_MODULE
       value: mobland.settings
     - key: DEBUG
       value: "False"
   ```

3. **Add Database**
   - Add PostgreSQL database
   - Update `DATABASE_URL` environment variable

### 4. PythonAnywhere

#### Steps
1. **Create Account**
   - Sign up at PythonAnywhere.com
   - Choose appropriate plan

2. **Upload Code**
   - Clone repository or upload files
   - Install dependencies

3. **Configure Web App**
   - Create new web app
   - Set source code directory
   - Configure WSGI file

4. **Set Environment Variables**
   - Add all required variables
   - Restart web app

## 🔧 Production Configuration

### Database Configuration

#### PostgreSQL (Recommended)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}
```

#### MySQL
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', '3306'),
    }
}
```

### Static Files Configuration

```python
# settings.py
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# For production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### Media Files Configuration

```python
# settings.py
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# For production with cloud storage
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
```

### Security Settings

```python
# settings.py - Production security
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Security settings
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'

# Session security
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

## 📋 Environment Variables Checklist

### Required Variables
- [ ] `DEBUG=False`
- [ ] `SECRET_KEY` (generate new for production)
- [ ] `ALLOWED_HOSTS` (your domain)
- [ ] `DATABASE_URL` (or individual DB settings)
- [ ] `EMAIL_USER` (Gmail address)
- [ ] `EMAIL_PASSWORD` (Gmail app password)
- [ ] `RECAPTCHA_PUBLIC_KEY`
- [ ] `RECAPTCHA_PRIVATE_KEY`
- [ ] `ZARINPAL_MERCHANT_ID`
- [ ] `ZARINPAL_ACCESS_TOKEN`
- [ ] `KAVENEGAR_API_KEY`

### Optional Variables
- [ ] `AWS_ACCESS_KEY_ID` (for S3 storage)
- [ ] `AWS_SECRET_ACCESS_KEY`
- [ ] `AWS_STORAGE_BUCKET_NAME`
- [ ] `REDIS_URL` (for caching)
- [ ] `SENTRY_DSN` (for error tracking)

## 🚀 Pre-deployment Checklist

### Code Preparation
- [ ] All tests pass
- [ ] Static files collected
- [ ] Migrations created and tested
- [ ] Environment variables configured
- [ ] Security settings enabled
- [ ] Debug mode disabled

### Database
- [ ] Database configured
- [ ] Migrations applied
- [ ] Superuser created
- [ ] Initial data loaded (if needed)

### Static Files
- [ ] Static files collected
- [ ] Media files configured
- [ ] CDN configured (if using)

### Domain and SSL
- [ ] Domain configured
- [ ] SSL certificate installed
- [ ] HTTPS redirect enabled

## 🔍 Post-deployment Testing

### Basic Functionality
- [ ] Homepage loads
- [ ] User registration works
- [ ] User login works
- [ ] Product pages load
- [ ] Shopping cart functions
- [ ] Checkout process works
- [ ] Payment integration works
- [ ] Admin panel accessible

### Performance
- [ ] Page load times acceptable
- [ ] Static files loading
- [ ] Database queries optimized
- [ ] Caching working (if implemented)

### Security
- [ ] HTTPS working
- [ ] Security headers present
- [ ] No sensitive data exposed
- [ ] Error pages don't reveal information

## 🐛 Troubleshooting

### Common Issues

#### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

#### Database Connection Issues
- Check database credentials
- Verify database server is running
- Check network connectivity

#### Email Not Sending
- Verify Gmail app password
- Check SMTP settings
- Test with different email provider

#### Payment Gateway Issues
- Verify API credentials
- Check sandbox/production mode
- Test with small amounts

### Logs and Monitoring
- Check application logs
- Monitor error rates
- Set up uptime monitoring
- Configure error tracking (Sentry)

## 📞 Support

For deployment issues:
- Check platform-specific documentation
- Review application logs
- Contact hosting provider support
- Create issue in repository

---

**Note**: Always test deployments in a staging environment before deploying to production.
