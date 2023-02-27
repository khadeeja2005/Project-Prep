from django.urls import path
from . import views

app_name = "calendars"

urlpatterns = [
    path('', views.titlePage, name='titlepage'),
    path('uploadfile/', views.uploadFile, name='uploadfile'),
    path('upload/', views.upload_csv, name='upload'),
]