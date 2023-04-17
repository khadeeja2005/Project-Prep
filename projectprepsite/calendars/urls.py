from django.urls import path
from . import views

app_name = "calendars"

urlpatterns = [
    path(r'', views.titlePage, name='titlepage'),
    path(r'uploadfile/', views.uploadFile, name='uploadfile'),
    path(r'upload/', views.upload_csv, name='upload'),
    path(r'uploadsuccess/', views.uploadSuccess, name='uploadsuccess'),
    path(r'additionalform/', views.additionalForm, name='additionalform'),
]