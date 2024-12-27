from django.urls import path

from . import views

urlpatterns = [
    path('', views.gallery_list, name='gallery-list'),
    path('add/', views.gallery_add, name='gallery-add'),
    path('moderate/', views.gallery_moderate, name='gallery-moderate'),
    path('approve/<int:pk>/', views.approve_item, name='approve-item'),
]
