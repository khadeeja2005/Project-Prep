from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
import logging
from django.contrib import messages
from django import forms
from calendars.forms import EventsForm

# Create your views here.
def titlePage(request):
    return render(request, 'calendars/titlepage.html')
def uploadFile(request):
    return render(request, 'calendars/uploadfile.html')
def upload_csv(request):
    data = {}
    if "GET" == request.method:
        return render(request, "calendars/upload.html", data)
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

        file_data = csv_file.read().decode("utf-8")		

        lines = file_data.split("\n")
            try:
                form = EventsForm()
                if form.is_valid():
                    form.save()
                    handle_uploaded_file(csv_file)			
                else:
                    logging.getLogger("error_logger").error(form.errors.as_json())												
            except Exception as e:
                logging.getLogger("error_logger").error(repr(e))					
                pass

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