from django.db import models

from django.contrib.auth.models import User

from accounts_app.models import CustomUser

class Portfolio(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="portfolios", verbose_name="Користувач")
    title = models.CharField(max_length=200, verbose_name="Назва")
    description = models.TextField(blank=True, verbose_name="Опис")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено")

    def __str__(self):
        return self.title


class PortfolioItem(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="items", verbose_name="Портфоліо")
    title = models.CharField(max_length=200, verbose_name="Назва")
    description = models.TextField(blank=True, null=True, verbose_name="Опис")
    screenshot = models.ImageField(upload_to="portfolio_screenshots/", blank=True, null=True, verbose_name="Скріншот")
    link = models.URLField(blank=True, null=True, verbose_name="Посилання на проект")
    file = models.FileField(upload_to="portfolio_files/", blank=True, null=True, verbose_name="Файл")


    def __str__(self):
        return self.title




