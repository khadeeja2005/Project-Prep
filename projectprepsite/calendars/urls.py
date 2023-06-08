'''
Version 1.0
Authors: Khadeeja Rizwan and Eddy Wang
Last Updated: June 1, 2023
'''

#import statements
from django.urls import path
from . import views

app_name = "calendars"

# Declaring URL paths for navigation
urlpatterns = [
    path(r'', views.titlePage, name='titlepage'),
    path(r'uploadfile/', views.uploadFile, name='uploadfile'),
    path(r'upload/', views.upload_csv, name='upload'),
    path(r'uploadsuccess/', views.uploadSuccess, name='uploadsuccess'),
    path(r'additionalform/', views.additionalForm, name='additionalform'),
    path(r'supervisionscheduledisplay', views.supervisionscheduledisplay, name='supervisionscheduledisplay'),
    path(r'weekdisplay', views.weekdisplay, name='weekdisplay'),
    path(r'daydisplay', views.daydisplay, name='daydisplay'),
]