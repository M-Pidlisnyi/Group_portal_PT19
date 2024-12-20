from django.urls import path
from . import views

urlpatterns = [
    path('anns/', views.Announcment_list, name='Announcment_list'),
]