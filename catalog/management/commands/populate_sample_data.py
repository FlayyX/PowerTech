from django.core.management.base import BaseCommand
from catalog.models import Service, Project
from django.core.files.base import ContentFile
import os

class Command(BaseCommand):
    help = 'Populate database with sample services and projects'

    def handle(self, *args, **options):
        # Create sample services with different images
        services_data = [
            {
                'title': 'Panel Design',
                'description': 'Smart industrial automation systems designed for efficiency and scalability.',
                'image_path': 'catalog/images/s4.jpg',
                'order': 1,
            },
            {
                'title': 'Installation of PLC Program',
                'description': 'Advanced IoT integration for real-time monitoring and control.',
                'image_path': 'catalog/images/s3.jpg',
                'order': 2,
            },
            {
                'title': 'Installation of VFD and Softstarter',
                'description': 'Expert installation to maximize motor control, safety, and energy efficiency.',
                'image_path': 'catalog/images/soft.jpg',
                'order': 3,
            },
            {
                'title': 'System Maintenance',
                'description': 'Preventive maintenance to keep your production systems running smoothly.',
                'image_path': 'catalog/images/s2.jpg',
                'order': 4,
            },
            {
                'title': 'Factory Automation',
                'description': 'End-to-end automation solutions for higher productivity and reliability.',
                'image_path': 'catalog/images/2.jpg',
                'order': 5,
            },
        ]

        for service_data in services_data:
            service, created = Service.objects.get_or_create(
                title=service_data['title'],
                defaults={
                    'description': service_data['description'],
                    'order': service_data['order'],
                }
            )
            # Note: In a real scenario, you'd copy the actual image file
            # For now, we'll just update the database record

        # Create sample projects with different images
        projects_data = [
            {
                'title': 'Cement Factory Site Development',
                'description': 'A state-of-the-art cement factory site designed for efficient production and environmental sustainability.',
                'tag': 'Cement Factory Project',
                'image_path': 'catalog/images/s1.jpg',
                'is_featured': True,
                'order': 1,
            },
            {
                'title': 'Snack Project',
                'description': 'Major road infrastructure enhancing goods movement and local connectivity.',
                'tag': 'Cartoon Snack Factory',
                'image_path': 'catalog/images/s2.jpg',
                'is_featured': True,
                'order': 2,
            },
            {
                'title': 'BEER Factory Project',
                'description': 'Highway construction delivering smooth travel through challenging terrain.',
                'tag': 'Electrical Project',
                'image_path': 'catalog/images/s3.jpg',
                'is_featured': True,
                'order': 3,
            },
            {
                'title': 'Mawk Mai Road Construction Project',
                'description': 'Strategic roadway development connecting remote communities with the main network.',
                'tag': 'Construction',
                'image_path': 'catalog/images/s4.jpg',
                'is_featured': True,
                'order': 4,
            },
            {
                'title': 'Factory Control Room',
                'description': 'A premium control panel layout installed for motor and process automation. Clean wiring and modern component placement highlight our quality standards.',
                'tag': 'Control Panel',
                'image_path': 'catalog/images/2.jpg',
                'is_featured': False,
                'order': 5,
            },
            {
                'title': 'Electrical Assembly',
                'description': 'Precision electrical assembly featuring organized cable management and robust switchgear solutions for heavy equipment environments.',
                'tag': 'Assembly',
                'image_path': 'catalog/images/3.jpg',
                'is_featured': False,
                'order': 6,
            },
        ]

        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults={
                    'description': project_data['description'],
                    'tag': project_data['tag'],
                    'is_featured': project_data['is_featured'],
                    'order': project_data['order'],
                }
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample data')
        )