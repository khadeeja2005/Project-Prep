from django.contrib import admin
from calendars.models import CSV_FILE
from calendars.models import additional_info_models

admin.site.register(additional_info_models)
admin.site.register(CSV_FILE)

# Register your models here.
