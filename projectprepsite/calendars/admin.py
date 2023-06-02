from django.contrib import admin
from calendars.models import CSV_FILE
from calendars.models import additional_info_models

# Register models to the admin site
admin.site.register(additional_info_models)
admin.site.register(CSV_FILE)

