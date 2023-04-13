from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
import logging
from django.contrib import messages
from django import forms
from calendars.forms import EventsForm
from calendars.models import CSV_FILE
from calendars.forms import CSV_FILE_FORM

# Create your views here.
def titlePage(request):
    return render(request, 'calendars/titlepage.html')
def uploadFile(request):
    return render(request, 'calendars/uploadfile.html')
def upload_csv(request):
    if "GET" == request.method:
        file = CSV_FILE_FORM(request.POST, request.FILES)
        if file.is_valid():
            file.save()
        # return render(request, "calendars/upload.html")
    elif "POST" == request.method:
        return render(request, "calendars/uploadsuccess.html")
    
    # if not GET, then proceed

    return render(request, 'calendars/upload.html')
def handle_uploaded_file(f):
    with open('calendars/upload'+csv_file.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def uploadSuccess(request):
    return render(request, 'calendars/uploadsuccess.html')