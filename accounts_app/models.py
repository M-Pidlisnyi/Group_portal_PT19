from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    premissions = models.ManyToManyField("auth.Permission", help_text="Список дозволів через кому", blank=True, null=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def save(self, *args, **kwargs):
        if not self.role:
            guest_role, _ = Role.objects.get_or_create(name="Гість")
            self.role = guest_role
        super().save(*args, **kwargs)