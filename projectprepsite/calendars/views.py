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
        return render(request, "calendars/upload.html")
    elif "POST" == request.method:
        return render(request, "calendars/uploadsuccess.html")
    
    # if not GET, then proceed
    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            return HttpResponseRedirect(reverse("calendars:upload"))
        #if file is too large, return
        if csv_file.multiple_chunks():
            messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
            return HttpResponseRedirect(reverse("calendars:upload"))

    except Exception as e:
        logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
        messages.error(request,"Unable to upload file. "+repr(e))

    return render(request, 'calendars/upload.html')
def handle_uploaded_file(f):
    with open('calendars/upload'+csv_file.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def uploadSuccess(request):
    return render(request, 'calendars/uploadsuccess.html')