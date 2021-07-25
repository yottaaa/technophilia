from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('detail/<str:pk>/', views.blogDetail, name="blog-detail"),
    path('about/', views.about, name="blog-about"),
]
