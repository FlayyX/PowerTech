from django.shortcuts import render
from django.db.models import Prefetch
from .models import Service, Project, GalleryImage

def home(request):
    services = Service.objects.filter(is_active=True).order_by('order', '-created_at')
    projects = Project.objects.filter(is_active=True, is_featured=True).order_by('order', '-created_at')
    context = {
        'services': services,
        'projects': projects,
    }
    return render(request, 'catalog/home.html', context)

def cement(request):
    projects = Project.objects.filter(is_active=True).prefetch_related(
        Prefetch(
            'gallery_images',
            queryset=GalleryImage.objects.filter(is_active=True).order_by('order', '-created_at')
        )
    ).order_by('order', '-created_at')

    context = {
        'projects': projects,
    }
    return render(request, 'catalog/cement.html', context)