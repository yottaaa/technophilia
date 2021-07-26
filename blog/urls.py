from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('detail/<str:pk>/', views.blogDetail, name="blog-detail"),
    path('create/', views.blogCreate, name="blog-create"),
    path('about/', views.about, name="blog-about"),
]
