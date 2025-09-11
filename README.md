# FurnApp - Django E-commerce Platform

A comprehensive Django-based e-commerce platform for furniture sales with Persian/Jalali date support, payment gateway integration, and modern admin interface.

## 🚀 Features

### Core Features
- **User Management**: Registration, authentication, and user profiles
- **Product Catalog**: Categories, products, images, and add-ons
- **Shopping Cart**: Add to cart, quantity management, and checkout
- **Order Management**: Order tracking and payment processing
- **Blog System**: Content management with CKEditor
- **Contact System**: Contact forms with admin responses
- **Admin Panel**: Comprehensive admin interface with custom widgets

### Technical Features
- **Persian/Jalali Date Support**: Full RTL and Persian date integration
- **Payment Gateway**: Zarinpal payment integration
- **SMS Integration**: Kavenegar SMS service
- **Rich Text Editor**: CKEditor for content management
- **Form Handling**: Crispy Forms for beautiful form rendering
- **Security**: reCAPTCHA integration
- **Responsive Design**: Mobile-friendly interface

## 🛠️ Technology Stack

- **Backend**: Django 5.1.4
- **Database**: SQLite (development), PostgreSQL/MySQL (production)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Payment**: Zarinpal Gateway
- **SMS**: Kavenegar API
- **Editor**: CKEditor
- **Forms**: Django Crispy Forms
- **Date**: Django Jalali Date

## 📋 Requirements

- Python 3.10+
- Django 5.1.4
- Pillow (image processing)
- All dependencies listed in `requirements.txt`

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/mobland.git
cd mobland
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv env
env\Scripts\activate

# macOS/Linux
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Copy the environment template and configure:
```bash
cp .env.example .env
```

Edit `.env` with your configuration:
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

### 5. Database Setup
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Collect Static Files
```bash
python manage.py collectstatic
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to see the application.

## 📁 Project Structure

```
mobland/
├── mobland/                 # Main Django project
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── account_module/          # User authentication & profiles
├── home_module/             # Homepage and main pages
├── product_module/          # Product catalog management
├── order_module/            # Shopping cart and orders
├── user_panel_module/       # User dashboard
├── blogs/                   # Blog system
├── contact_us/              # Contact forms
├── site_module/             # Site settings
├── polls/                   # Template tags and utilities
├── templates/               # HTML templates
├── static/                  # Static files (CSS, JS, images)
├── uploads/                 # User uploaded files
├── database/                # SQLite database
├── requirements.txt         # Python dependencies
├── Procfile                 # Heroku deployment
├── runtime.txt              # Python version
└── README.md               # This file
```

## 🔧 Configuration

### Database
The project uses SQLite by default. For production, configure PostgreSQL or MySQL in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Static Files
Configure static files for production:
```python
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

### Media Files
User uploads are stored in the `uploads/` directory:
```python
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
```

## 🚀 Deployment

### Heroku
1. Install Heroku CLI
2. Login to Heroku: `heroku login`
3. Create app: `heroku create your-app-name`
4. Set environment variables: `heroku config:set DJANGO_SETTINGS_MODULE=mobland.settings`
5. Deploy: `git push heroku main`

### Railway
1. Connect your GitHub repository
2. Set environment variables in Railway dashboard
3. Deploy automatically on push

### DigitalOcean App Platform
1. Connect your GitHub repository
2. Configure environment variables
3. Deploy with one click

## 🔐 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `EMAIL_USER` | Gmail address for sending emails | Yes |
| `EMAIL_PASSWORD` | Gmail app password | Yes |
| `RECAPTCHA_PUBLIC_KEY` | reCAPTCHA site key | Yes |
| `RECAPTCHA_PRIVATE_KEY` | reCAPTCHA secret key | Yes |
| `ZARINPAL_MERCHANT_ID` | Zarinpal merchant ID | Yes |
| `ZARINPAL_ACCESS_TOKEN` | Zarinpal access token | Yes |
| `KAVENEGAR_API_KEY` | Kavenegar API key | Yes |

## 📱 API Endpoints

### Authentication
- `POST /register/` - User registration
- `POST /login/` - User login
- `POST /logout/` - User logout

### Products
- `GET /products/` - Product list
- `GET /products/<id>/` - Product detail
- `POST /products/search/` - Product search

### Orders
- `POST /order/add-to-cart/` - Add to cart
- `GET /order/cart/` - View cart
- `POST /order/checkout/` - Process checkout

## 🧪 Testing

Run tests:
```bash
python manage.py test
```

## 📝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

## 📄 License

This project is private and proprietary. All rights reserved.

## 👥 Support

For support and questions:
- Create an issue in the repository
- Contact the development team

## 🔄 Changelog

### Version 1.0.0
- Initial release
- User authentication system
- Product catalog
- Shopping cart functionality
- Order management
- Payment gateway integration
- Admin panel
- Blog system
- Contact forms

---

**Note**: This is a private repository. Do not share sensitive information publicly.