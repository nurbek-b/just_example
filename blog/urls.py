from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('new/', BlogCreateView.as_view(), name='post_new'),
    path('<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
]