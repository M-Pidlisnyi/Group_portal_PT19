from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page),
    path("home/", views.main_page, name="home")
]