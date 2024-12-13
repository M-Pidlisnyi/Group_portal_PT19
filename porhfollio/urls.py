from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_list, name='portfolio_list'),
    path('create/', views.create_portfolio, name='create_portfolio'),
    path('<int:pk>/edit/', views.edit_portfolio, name='edit_portfolio'),
    path('<int:portfolio_pk>/add_item/', views.add_portfolio_item, name='add_portfolio_item'),
    path('<int:pk>/', views.portfolio_detail, name='portfolio_detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


