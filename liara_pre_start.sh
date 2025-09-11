#!/bin/bash

mkdir -p database

# Fix migration issue for ProductOptionType
echo "Checking for ProductOptionType migration issue..."
python -c "
import sqlite3
import os
import sys

# Check if database exists and table exists
db_path = 'database/db.sqlite3'
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(\"SELECT name FROM sqlite_master WHERE type='table' AND name='product_module_productoptiontype'\")
    table_exists = cursor.fetchone() is not None
    conn.close()
    
    if table_exists:
        print('ProductOptionType table exists, faking migration...')
        os.system('python manage.py migrate product_module 0005_auto_20250910_1616 --fake')
    else:
        print('ProductOptionType table does not exist, running normal migration...')
        os.system('python manage.py migrate')
else:
    print('Database does not exist, running normal migration...')
    os.system('python manage.py migrate')
"

# Collect static files for production
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Verify static files were collected
if [ -d "staticfiles" ]; then
    echo "Static files collected successfully"
    ls -la staticfiles/ | head -10
else
    echo "Static files collection failed"
    echo "Checking if static directory exists..."
    if [ -d "static" ]; then
        echo "Static directory found, retrying collection..."
        python manage.py collectstatic --noinput
    else
        echo "Static directory not found - this is the problem!"
    fi
fi