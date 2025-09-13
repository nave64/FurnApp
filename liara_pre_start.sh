#!/bin/bash

# Liara pre-start script to ensure uploads directory exists and run migrations

# Create uploads directory if it doesn't exist
mkdir -p /uploads

# Set proper permissions for uploads directory
chmod 755 /uploads

# Create subdirectories for different upload types
mkdir -p /uploads/blogs
mkdir -p /uploads/category_images
mkdir -p /uploads/department_cards
mkdir -p /uploads/home
mkdir -p /uploads/homepage-categories
mkdir -p /uploads/images
mkdir -p /uploads/product-list-bg
mkdir -p /uploads/user_uploads

# Set permissions for all subdirectories
chmod -R 755 /uploads

echo "Uploads directory setup completed successfully"

# Run database migrations
echo "Running database migrations..."
python manage.py migrate --noinput

echo "Database migrations completed successfully"
