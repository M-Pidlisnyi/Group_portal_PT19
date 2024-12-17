from django.db import models
from django.contrib.auth.models import User
from accounts_app.models import CustomUser

class Material(models.Model):
    MATERIAL_TYPES = [
        ('file', 'Файл'),
        ('image', 'Зображення'),
        ('youtube', 'YouTube Посилання'),
        ('link', 'Посилання'),
    ]

    title = models.CharField(max_length=255, verbose_name="Назва")
    description = models.TextField(blank=True, verbose_name="Опис")
    material_type = models.CharField(max_length=10, choices=MATERIAL_TYPES, verbose_name="Тип матеріалу")
    file = models.FileField(upload_to='materials/files/', blank=True, null=True, verbose_name="Файл")
    image = models.ImageField(upload_to='materials/images/', blank=True, null=True, verbose_name="Зображення")
    youtube_link = models.URLField(blank=True, null=True, verbose_name="YouTube Посилання")
    external_link = models.URLField(blank=True, null=True, verbose_name="Посилання")
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Матеріал"
        verbose_name_plural = "Матеріали"
