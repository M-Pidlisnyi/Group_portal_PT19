from django.db import models
from accounts_app.models import CustomUser

class GalleryItem(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('photo', 'Фото'),
        ('video', 'Відео'),
    ]

    title = models.CharField(max_length=100, verbose_name="Назва")
    description = models.TextField(blank=True, verbose_name="Опис")
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES, verbose_name="Тип")
    file = models.FileField(upload_to='gallery/', verbose_name="Файл")
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Завантажив")
    is_approved = models.BooleanField(default=False, verbose_name="Перевірено")

    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата завантаження")

    def __str__(self):
        return self.title
