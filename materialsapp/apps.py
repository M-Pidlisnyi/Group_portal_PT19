from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


class MaterialsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'materialsapp'

    def ready(self):
        # Створення груп
        admin_group, created = Group.objects.get_or_create(name='Administrators')
        moderator_group, created = Group.objects.get_or_create(name='Moderators')

        # Додавання прав для моделі Material
        content_type = ContentType.objects.get(app_label='materials', model='material')
        
        # Доступ до редагування, додавання та видалення матеріалів
        permissions = Permission.objects.filter(content_type=content_type)
        
        # Адміністраторам даємо всі права
        admin_group.permissions.set(permissions)

        # Модераторам лише додавання і редагування
        moderator_permissions = permissions.filter(codename__in=['add_material', 'change_material'])
        moderator_group.permissions.set(moderator_permissions)