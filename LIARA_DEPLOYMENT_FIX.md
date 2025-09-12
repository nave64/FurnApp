# Liara Deployment Fix for File Uploads

## Problem
The application was getting "Read-only file system" errors when trying to save files in the Django admin panel on Liara deployment.

## Solution Implemented

### 1. Updated `liara.json`
Added an uploads disk to the Liara configuration:
```json
{
  "django": {
    "settingsFile": "mobland/settings.py"
  },
  "disks": [
    {
      "name": "database",
      "mountTo": "database"
    },
    {
      "name": "uploads",
      "mountTo": "uploads"
    }
  ]
}
```

### 2. Updated `mobland/settings.py`
Modified MEDIA_ROOT to use the mounted disk in production:
```python
# Media files (User uploads)
MEDIA_URL = '/uploads/'
# Use mounted disk in production, local directory in development
if os.getenv('LIARA_DISK_UPLOADS'):
    MEDIA_ROOT = '/uploads'  # Liara mounted disk
else:
    MEDIA_ROOT = BASE_DIR / 'uploads'  # Local development
```

### 3. Created `liara_pre_start.sh`
Pre-start script to ensure uploads directory structure exists:
- Creates `/uploads` directory
- Creates all necessary subdirectories
- Sets proper permissions (755)

### 4. Updated `Procfile`
Modified to run the pre-start script before starting the application:
```
web: bash liara_pre_start.sh && python manage.py runserver 0.0.0.0:$PORT
```

## How It Works

1. **Liara Disk Mounting**: The `uploads` disk is mounted to `/uploads` in the container
2. **Environment Detection**: Django detects if it's running on Liara using environment variables
3. **Path Selection**: Uses `/uploads` (mounted disk) in production, local `uploads/` in development
4. **Directory Setup**: Pre-start script ensures all required directories exist with proper permissions

## Deployment Steps

1. **Deploy to Liara**: Push these changes to your Liara app
2. **Create Disk**: In Liara dashboard, create a new disk named "uploads"
3. **Mount Disk**: Mount the disk to your application
4. **Test**: Try uploading files in the Django admin panel

## Benefits

- ✅ **Persistent Storage**: Files survive container restarts
- ✅ **Proper Permissions**: Directory structure created with correct permissions
- ✅ **Development Compatibility**: Still works locally with local uploads folder
- ✅ **Security**: Uses Liara's secure disk mounting system

## Environment Variables

The system automatically detects the deployment environment. No additional environment variables are required for basic functionality.

## Troubleshooting

If you still get read-only errors:
1. Check that the "uploads" disk is created and mounted in Liara dashboard
2. Verify the disk is properly attached to your application
3. Check Liara logs for any disk mounting errors
4. Ensure the pre-start script is running (check Procfile)

## File Structure

After deployment, the following structure will be available:
```
/uploads/
├── blogs/
├── category_images/
├── department_cards/
├── home/
├── homepage-categories/
├── images/
├── product-list-bg/
└── user_uploads/
```
