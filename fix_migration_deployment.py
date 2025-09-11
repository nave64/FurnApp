#!/usr/bin/env python
"""
Deployment script to fix the ProductOptionType migration issue.
This script should be run before the main migration process.
"""

import os
import sys
import django
from django.conf import settings

# Add the project directory to Python path
sys.path.insert(0, '/usr/src/app')

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mobland.settings')
django.setup()

from django.db import connection
from django.core.management import execute_from_command_line

def check_table_exists(table_name):
    """Check if a table exists in the database."""
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name=?
        """, [table_name])
        return cursor.fetchone() is not None

def fix_migration_issue():
    """Fix the migration issue by faking the problematic migration."""
    print("Checking for ProductOptionType table...")
    
    if check_table_exists('product_module_productoptiontype'):
        print("✅ ProductOptionType table already exists")
        print("Faking migration 0005_auto_20250910_1616...")
        
        # Fake the migration since the table already exists
        execute_from_command_line([
            'manage.py', 
            'migrate', 
            'product_module', 
            '0005_auto_20250910_1616', 
            '--fake'
        ])
        print("✅ Migration 0005_auto_20250910_1616 has been faked")
    else:
        print("❌ ProductOptionType table does not exist")
        print("Running normal migration...")
        execute_from_command_line([
            'manage.py', 
            'migrate', 
            'product_module', 
            '0005_auto_20250910_1616'
        ])

if __name__ == '__main__':
    try:
        fix_migration_issue()
        print("✅ Migration fix completed successfully")
    except Exception as e:
        print(f"❌ Error fixing migration: {e}")
        sys.exit(1)
