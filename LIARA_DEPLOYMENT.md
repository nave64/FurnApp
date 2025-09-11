# Liara Deployment Guide - FurnApp

This guide will help you deploy your FurnApp Django e-commerce platform to Liara.

## 🚀 Quick Fix for Database Error

The "unable to open database file" error occurs because Liara doesn't support SQLite in production. You need to use PostgreSQL.

## 📋 Prerequisites

1. **Liara Account**: Sign up at [liara.ir](https://liara.ir)
2. **Liara CLI**: Install from [docs.liara.ir](https://docs.liara.ir/cli)
3. **PostgreSQL Database**: Create a database in Liara

## 🔧 Step-by-Step Deployment

### Step 1: Create PostgreSQL Database

1. **Login to Liara Dashboard**
   - Go to [console.liara.ir](https://console.liara.ir)
   - Login with your account

2. **Create Database**
   - Click "Create Database"
   - Choose "PostgreSQL"
   - Select plan (Basic is fine for testing)
   - Name it: `furnapp-db`
   - Click "Create"

3. **Get Database URL**
   - Go to your database dashboard
   - Copy the "Connection String" (DATABASE_URL)
   - It looks like: `postgresql://username:password@host:port/database`

### Step 2: Deploy Application

1. **Install Liara CLI**
   ```bash
   # Download from https://docs.liara.ir/cli
   # Or use npm
   npm install -g @liara/cli
   ```

2. **Login to Liara**
   ```bash
   liara login
   ```

3. **Create App**
   ```bash
   liara create app --platform django --name furnapp
   ```

4. **Set Environment Variables**
   ```bash
   # Set database URL
   liara env set DATABASE_URL=postgresql://username:password@host:port/database
   
   # Set other required variables
   liara env set DJANGO_SETTINGS_MODULE=mobland.settings
   liara env set DEBUG=False
   liara env set ALLOWED_HOSTS=furniture.liara.run,*.liara.run
   liara env set SECRET_KEY=your-secret-key-here
   
   # Set your API keys
   liara env set EMAIL_USER=your-email@gmail.com
   liara env set EMAIL_PASSWORD=your-app-password
   liara env set RECAPTCHA_PUBLIC_KEY=your-public-key
   liara env set RECAPTCHA_PRIVATE_KEY=your-private-key
   liara env set ZARINPAL_MERCHANT_ID=your-merchant-id
   liara env set ZARINPAL_ACCESS_TOKEN=your-access-token
   liara env set KAVENEGAR_API_KEY=your-api-key
   ```

5. **Deploy**
   ```bash
   liara deploy
   ```

### Step 3: Run Migrations

After deployment, run migrations to create database tables:

```bash
liara run python manage.py migrate
liara run python manage.py createsuperuser
liara run python manage.py collectstatic --noinput
```

## 🔧 Alternative: Manual Deployment

If you prefer to use the Liara dashboard:

1. **Create App**
   - Go to Liara dashboard
   - Click "Create App"
   - Choose "Django"
   - Name: `furnapp`

2. **Connect Repository**
   - Connect your GitHub repository
   - Select the `main` branch

3. **Set Environment Variables**
   - Go to "Environment Variables" tab
   - Add all required variables (see list above)

4. **Deploy**
   - Click "Deploy" button
   - Wait for deployment to complete

## 🗄️ Database Configuration

Your app now automatically detects the environment:

- **Development**: Uses SQLite (local)
- **Production**: Uses PostgreSQL (Liara)

The settings.py file has been updated to:
```python
if os.environ.get('DATABASE_URL'):
    # Production database (PostgreSQL)
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    # Development database (SQLite)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'database', 'db.sqlite3'),
        }
    }
```

## 🔐 Required Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://user:pass@host:port/db` |
| `DJANGO_SETTINGS_MODULE` | Django settings module | `mobland.settings` |
| `DEBUG` | Debug mode | `False` |
| `ALLOWED_HOSTS` | Allowed hosts | `furniture.liara.run,*.liara.run` |
| `SECRET_KEY` | Django secret key | `your-secret-key` |
| `EMAIL_USER` | Gmail address | `your-email@gmail.com` |
| `EMAIL_PASSWORD` | Gmail app password | `your-app-password` |
| `RECAPTCHA_PUBLIC_KEY` | reCAPTCHA site key | `6Ld...` |
| `RECAPTCHA_PRIVATE_KEY` | reCAPTCHA secret key | `6Ld...` |
| `ZARINPAL_MERCHANT_ID` | Zarinpal merchant ID | `your-merchant-id` |
| `ZARINPAL_ACCESS_TOKEN` | Zarinpal access token | `your-access-token` |
| `KAVENEGAR_API_KEY` | Kavenegar API key | `your-api-key` |

## 🚀 Post-Deployment Steps

1. **Run Migrations**
   ```bash
   liara run python manage.py migrate
   ```

2. **Create Superuser**
   ```bash
   liara run python manage.py createsuperuser
   ```

3. **Collect Static Files**
   ```bash
   liara run python manage.py collectstatic --noinput
   ```

4. **Test Your App**
   - Visit your app URL
   - Test user registration
   - Test product pages
   - Test admin panel

## 🐛 Troubleshooting

### Database Connection Issues
- Check DATABASE_URL format
- Ensure database is running
- Verify credentials

### Static Files Not Loading
- Run `python manage.py collectstatic --noinput`
- Check STATIC_ROOT setting
- Verify file permissions

### Environment Variables Not Working
- Check variable names (case-sensitive)
- Ensure no extra spaces
- Restart app after setting variables

### App Not Starting
- Check logs: `liara logs`
- Verify all required variables are set
- Check Python version compatibility

## 📞 Support

- **Liara Documentation**: [docs.liara.ir](https://docs.liara.ir)
- **Liara Support**: [support.liara.ir](https://support.liara.ir)
- **Django Documentation**: [docs.djangoproject.com](https://docs.djangoproject.com)

---

**Your FurnApp should now work perfectly on Liara!** 🎉
