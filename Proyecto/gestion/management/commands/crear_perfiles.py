from django.core.management.base import BaseCommand
from gestion.signals import ensure_portal_roles


class Command(BaseCommand):
    help = 'Crea los perfiles y asigna los permisos del portal.'
    def handle(self, *args, **options):
        ensure_portal_roles()
        self.stdout.write(self.style.SUCCESS('Perfiles y permisos del portal configurados.'))
