# Fix for "Multiple Settings Files" Error

## The Problem
Your hosting platform is detecting multiple Django settings files:
1. `env/Lib/site-packages/ckeditor_demo/settings.py` (from virtual environment)
2. `env/Lib/site-packages/django/conf/global_settings.py` (Django's global settings)
3. `env/Lib/site-packages/django/core/servers/basehttp.py` (Django's development server)
4. `mobland/settings.py` (your actual settings)

## The Solution

### Step 1: Don't Deploy the Virtual Environment
The main issue is that your `env/` folder (virtual environment) is being deployed. This should never happen.

**Files to exclude from deployment:**
- `env/` (entire virtual environment folder)
- `__pycache__/` folders
- `*.pyc` files
- `.git/` folder

### Step 2: Use the Correct Requirements File
Use `requirements-deploy.txt` instead of `requirements.txt`:

```bash
pip install -r requirements-deploy.txt
```

### Step 3: Set Environment Variables
Make sure your hosting platform knows which settings file to use:

**For Heroku:**
```bash
heroku config:set DJANGO_SETTINGS_MODULE=mobland.settings
```

**For other platforms:**
Set the environment variable:
```
DJANGO_SETTINGS_MODULE=mobland.settings
```

### Step 4: Update Your Deployment Files

**Procfile** (for Heroku/Railway):
```
web: gunicorn mobland.wsgi:application --bind 0.0.0.0:$PORT
```

**runtime.txt** (specify Python version):
```
python-3.10.11
```

### Step 5: Clean Your Project Structure

Make sure your project structure looks like this:
```
mobland/
├── mobland/
│   ├── __init__.py
│   ├── settings.py          # Your main settings
│   ├── urls.py
│   └── wsgi.py
├── account_module/
├── home_module/
├── product_module/
├── order_module/
├── user_panel_module/
├── blogs/
├── contact_us/
├── site_module/
├── polls/
├── templates/
├── static/
├── uploads/
├── manage.py
├── requirements-deploy.txt
├── Procfile
├── runtime.txt
└── .gitignore
```

### Step 6: Platform-Specific Instructions

#### For Heroku:
1. Remove `env/` from your repository
2. Use `requirements-deploy.txt`
3. Set `DJANGO_SETTINGS_MODULE=mobland.settings`
4. Deploy without the virtual environment

#### For Railway:
1. Don't include `env/` in your deployment
2. Use `requirements-deploy.txt`
3. Set environment variable `DJANGO_SETTINGS_MODULE=mobland.settings`

#### For PythonAnywhere:
1. Upload only your project files (not `env/`)
2. Install dependencies using `requirements-deploy.txt`
3. Set `DJANGO_SETTINGS_MODULE=mobland.settings` in your web app configuration

### Step 7: Test Locally
Before deploying, test that your app works without the virtual environment:

```bash
# Create a fresh virtual environment
python -m venv test_env
test_env\Scripts\activate  # Windows
# or
source test_env/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements-deploy.txt

# Test the app
python manage.py runserver
```

## Quick Fix Commands

1. **Remove virtual environment from git:**
   ```bash
   git rm -r --cached env/
   echo "env/" >> .gitignore
   git add .gitignore
   git commit -m "Remove virtual environment from repository"
   ```

2. **Deploy with correct requirements:**
   ```bash
   # Use requirements-deploy.txt instead of requirements.txt
   ```

3. **Set environment variable:**
   ```bash
   # On your hosting platform, set:
   DJANGO_SETTINGS_MODULE=mobland.settings
   ```

This should resolve the "multiple settings files" error.
