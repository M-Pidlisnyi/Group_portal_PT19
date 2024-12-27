from django.urls import path
from .views import ThreadView, ThreadDetailView, ThreadUpdateView, PostUpdateView

urlpatterns = [
    path("", ThreadView.as_view(), name="thread_list"),
    path("detail/<int:pk>/", ThreadDetailView.as_view(), name="thread-detail"),
    path("update/thread/<int:pk>/", ThreadUpdateView.as_view(), name="thread-update"),
    path("update/post/<int:pk>/", PostUpdateView.as_view(), name="post-update"),
]