from django.urls import path
from . import views

urlpatterns = [
    path('', views.titlePage, name='titlepage'),
    path('uploadfile/', views.uploadFile, name='uploadfile'),
]