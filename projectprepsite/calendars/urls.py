from django.urls import path
from . import views

urlpatterns = [
    path('', views.titlePage, name='titlepage'),
    path('', views.uploadFile, name='uploadfile')
]