from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tag = models.CharField(max_length=100, help_text="Category tag (e.g., 'Cement Factory Project')")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    link_url = models.URLField(blank=True, help_text="Optional external link")
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_featured = models.BooleanField(default=False, help_text="Show in featured projects section")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    project = models.ForeignKey(Project, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/', help_text="Upload gallery images for this project")
    title = models.CharField(max_length=200, blank=True, help_text="Optional title for this image")
    description = models.TextField(blank=True, help_text="Optional description for this image")
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"

    def __str__(self):
        return f"{self.project.title} - {self.title or f'Image {self.id}'}"

    def get_display_title(self):
        return self.title or self.project.title

    def get_display_description(self):
        return self.description or self.project.description
