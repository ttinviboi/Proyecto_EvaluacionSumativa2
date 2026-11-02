from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver


def ensure_portal_roles():
    admin, _ = Group.objects.get_or_create(name='Administrador')
    supervisor, _ = Group.objects.get_or_create(name='Supervisor')
    staff, _ = Group.objects.get_or_create(name='Administrativo')
    models = [('noticias', 'categoria'), ('cine', 'genero'), ('gestion', 'reserva')]
    perms = {}
    for app_label, model in models:
        ct = ContentType.objects.get(app_label=app_label, model=model)
        perms[model] = list(Permission.objects.filter(content_type=ct))
    admin.permissions.set(Permission.objects.all())
    supervisor.permissions.set([p for key in ('categoria', 'genero', 'reserva') for p in perms[key] if p.codename.startswith(('add_', 'change_', 'view_'))] + list(Permission.objects.filter(codename='gestionar_reservas')))
    staff.permissions.set([p for p in perms['reserva'] if p.codename in ('add_reserva', 'view_reserva')])


@receiver(post_migrate)
def create_portal_roles(sender, **kwargs):
    if sender.name == 'gestion':
        ensure_portal_roles()
