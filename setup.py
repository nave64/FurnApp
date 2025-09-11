#!/usr/bin/env python
"""
Setup script for Mobland Django E-commerce Platform
Run this script to set up the project for development
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def create_directories():
    """Create necessary directories"""
    directories = [
        'logs',
        'staticfiles',
        'media',
        'uploads/blogs',
        'uploads/category_images',
        'uploads/department_cards',
        'uploads/home',
        'uploads/homepage-categories',
        'uploads/images',
        'uploads/product-list-bg',
        'uploads/user_uploads'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"📁 Created directory: {directory}")

def setup_environment():
    """Set up environment file"""
    env_example = Path('env.example')
    env_file = Path('.env')
    
    if env_example.exists() and not env_file.exists():
        shutil.copy(env_example, env_file)
        print("📝 Created .env file from env.example")
        print("⚠️  Please edit .env file with your configuration")
    elif env_file.exists():
        print("📝 .env file already exists")
    else:
        print("❌ env.example file not found")

def main():
    """Main setup function"""
    print("🚀 Setting up Mobland Django E-commerce Platform")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 10):
        print("❌ Python 3.10 or higher is required")
        sys.exit(1)
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    
    # Create directories
    print("\n📁 Creating directories...")
    create_directories()
    
    # Setup environment
    print("\n🔧 Setting up environment...")
    setup_environment()
    
    # Install dependencies
    print("\n📦 Installing dependencies...")
    if not run_command("pip install -r requirements.txt", "Installing Python packages"):
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Run migrations
    print("\n🗄️  Setting up database...")
    if not run_command("python manage.py migrate", "Running database migrations"):
        print("❌ Failed to run migrations")
        sys.exit(1)
    
    # Collect static files
    print("\n📄 Collecting static files...")
    if not run_command("python manage.py collectstatic --noinput", "Collecting static files"):
        print("❌ Failed to collect static files")
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Edit .env file with your configuration")
    print("2. Create a superuser: python manage.py createsuperuser")
    print("3. Run the development server: python manage.py runserver")
    print("4. Visit http://127.0.0.1:8000 to see your application")
    print("\nFor more information, see README.md")

if __name__ == "__main__":
    main()
