from django.apps import AppConfig


class MaterialsappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "materialsapp"

    def ready(self):
        from django.contrib.auth.models import Group, Permission

        # Тут можна виконувати налаштування для груп і пермішенів
        moderators_group, created = Group.objects.get_or_create(name="Moderators")
        admins_group, created = Group.objects.get_or_create(name="Admins")

        # Додати права для цих груп, якщо потрібно
