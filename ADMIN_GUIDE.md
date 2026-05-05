# Power Tech Admin Guide

## Admin Access
- **URL**: http://127.0.0.1:8000/admin/
- **Username**: admin
- **Password**: PowerTech2026!
- **Email**: admin@powertech.com

## Managing Content

### Services
- **Location**: Admin → Catalog → Services
- **Fields**:
  - Title: Service name
  - Description: Detailed description
  - Image: **Click "Choose File" to upload a unique image for each service**
  - Order: Display order (lower numbers first)
  - Is Active: Show/hide service

### Projects
- **Location**: Admin → Catalog → Projects
- **Fields**:
  - Title: Project name
  - Description: Project details
  - Tag: Category (e.g., "Control Panel", "Factory")
  - Image: **Click "Choose File" to upload a unique image for each project**
  - Link URL: External link (optional)
  - Order: Display order
  - Is Featured: Show on homepage
  - Is Active: Show/hide project

## Image Upload Instructions
1. Go to Services or Projects in the admin
2. Click on a service/project to edit it
3. In the "Image" field, click "Choose File"
4. Select a JPG or PNG image from your computer
5. Click "Save" at the bottom
6. The image will automatically appear on the website

## Current Image Assignments (Fallback)
If no custom image is uploaded, the system uses these default images:
- **Services**: s4.jpg, s3.jpg, soft.jpg, s2.jpg, 2.jpg (different for each)
- **Projects**: s1.jpg, s2.jpg, s3.jpg, s4.jpg (rotating pattern)

## Features
- ✅ Add, edit, delete services and projects
- ✅ Upload custom images for each item
- ✅ Control display order
- ✅ Featured projects appear on homepage
- ✅ Active/inactive status control
- ✅ Search and filter functionality
- ✅ Automatic image handling

## File Structure
```
catalog/
├── models.py          # Database models
├── admin.py           # Admin interface
├── views.py           # Page views
├── templates/catalog/ # HTML templates
└── static/catalog/    # Images and assets
```

## Commands
- `python manage.py populate_sample_data` - Add sample content
- `python manage.py runserver` - Start development server
- `python manage.py createsuperuser` - Create admin user