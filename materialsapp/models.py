from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Material(models.Model):
    TYPE_CHOICES = [
        ('file', 'File'),
        ('image', 'Image'),
        ('video', 'YouTube Video'),
        ('link', 'Link'),
    ]

    title = models.CharField(max_length=255, verbose_name="Назва матеріалу")
    description = models.TextField(blank=True, null=True, verbose_name="Опис матеріалу")
    material_type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name="Тип матеріалу")
    file = models.FileField(upload_to='materials/files/', blank=True, null=True, verbose_name="Файл")
    image = models.ImageField(upload_to='materials/images/', blank=True, null=True, verbose_name="Зображення")
    youtube_url = models.URLField(blank=True, null=True, verbose_name="Посилання на YouTube")
    external_link = models.URLField(blank=True, null=True, verbose_name="Зовнішнє посилання")
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Додав користувач")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")

    def __str__(self):
        return self.title

    def is_video(self):
        return self.material_type == 'video'

    def is_file(self):
        return self.material_type == 'file'

    def is_image(self):
        return self.material_type == 'image'

    def is_link(self):
        return self.material_type == 'link'

    class Meta:
        verbose_name = "Матеріал"
        verbose_name_plural = "Матеріали"
        ordering = ['-created_at']