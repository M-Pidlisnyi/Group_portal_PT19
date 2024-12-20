from django.urls import path
from . import views

urlpatterns = [
    path('', views.material_list, name='material-list'),
    path('new/', views.material_create, name='material-create'),
    path('edit/<int:pk>/', views.material_edit, name='material-edit'),
    path('delete/<int:pk>/', views.material_delete, name='material-delete'),
]
