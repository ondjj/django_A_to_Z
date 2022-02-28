from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.single_post_page),
]