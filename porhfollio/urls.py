from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_list, name='portfolio_list'),
    path('create/', views.create_portfolio, name='create_portfolio'),
    path('edit/<int:pk>/', views.edit_portfolio, name='edit_portfolio'),
    path('add_item/<int:portfolio_pk>/', views.add_portfolio_item, name='add_portfolio_item'),

    path('view/<int:pk>/', views.portfolio_detail, name='portfolio_detail'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


