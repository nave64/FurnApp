# Mobland Django Project - Installation Guide

## Prerequisites

- Python 3.10 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## Installation Methods

### Method 1: Using requirements.txt (Recommended)

1. **Clone or download the project**
   ```bash
   cd mobland
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows
   python -m venv env
   env\Scripts\activate

   # macOS/Linux
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

### Method 2: Using Pipenv

1. **Install pipenv** (if not already installed)
   ```bash
   pip install pipenv
   ```

2. **Install dependencies**
   ```bash
   pipenv install
   ```

3. **Activate the virtual environment**
   ```bash
   pipenv shell
   ```

4. **Run migrations and start the server**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

## Project Dependencies

### Core Dependencies
- **Django 5.1.4** - Web framework
- **Pillow 11.3.0** - Image processing
- **django-ckeditor 6.7.3** - Rich text editor
- **django-crispy-forms 2.4** - Form rendering
- **django-jalali-date 2.0.0** - Persian/Jalali date support
- **django-recaptcha 4.1.0** - reCAPTCHA integration
- **requests 2.32.4** - HTTP library for API calls
- **kavenegar 1.1.2** - SMS service integration

### Development Dependencies (Optional)
Install with: `pip install -r requirements-dev.txt`

- **black** - Code formatter
- **flake8** - Linting
- **pytest** - Testing framework
- **django-debug-toolbar** - Debug toolbar

## Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# Email Configuration
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password

# reCAPTCHA Keys
RECAPTCHA_PUBLIC_KEY=your-public-key
RECAPTCHA_PRIVATE_KEY=your-private-key

# Zarinpal Payment Gateway
ZARINPAL_MERCHANT_ID=your-merchant-id
ZARINPAL_ACCESS_TOKEN=your-access-token
ZARINPAL_SANDBOX=True

# Kavenegar SMS
KAVENEGAR_API_KEY=your-api-key
```

## Database

The project uses SQLite by default. For production, consider using PostgreSQL or MySQL.

## Static Files

Collect static files for production:
```bash
python manage.py collectstatic
```

## Troubleshooting

1. **Import errors**: Make sure the virtual environment is activated
2. **Database errors**: Run `python manage.py migrate`
3. **Static files not loading**: Run `python manage.py collectstatic`
4. **Permission errors**: Check file permissions on Windows/macOS/Linux

## Support

For issues and questions, please check the Django documentation or create an issue in the project repository.
