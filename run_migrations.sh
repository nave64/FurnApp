#!/bin/bash

# Script to run Django migrations on Liara
# This can be run manually if needed

echo "Starting Django migrations..."

# Run all migrations
python manage.py migrate --noinput

echo "Migrations completed successfully"

# Show migration status
echo "Current migration status:"
python manage.py showmigrations
