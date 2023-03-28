from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
import logging
from django.contrib import messages
from django import forms
from calendars.models import CSV_FILE
from calendars.forms import DocumentForm

# Create your views here.
def titlePage(request):
    return render(request, 'calendars/titlepage.html')
def uploadFile(request):
    return render(request, 'calendars/uploadfile.html')
def upload_csv(request):
    # Handle file upload
    if request.method == 'GET':
        file = CSV_FILE(names=names, prep_times=prep_times, locations=locations)
        if file.is_valid():
            file.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))

        else:
            file = CSV_FILE() # A empty, unbound form

    # Load documents for the list page
    entries = CSV_FILE.objects.all()

    for i in file in entries:
        print(i)


    # Render list page with the documents and the form
    return render(request, 'upload.html', {'documents': documents, 'form': form})
    
def handle_uploaded_file(f):
    with open('calendars/upload'+csv_file.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def uploadSuccess(request):
    return render(request, 'calendars/uploadsuccess.html')