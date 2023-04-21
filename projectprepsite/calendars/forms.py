from django import forms
from calendars.models import CSV_FILE
from calendars.models import additional_info_models

class EventsForm(forms.ModelForm):
    file = forms.FileField()

class CSV_FILE_FORM(forms.ModelForm):
    class Meta:
        model = CSV_FILE
        fields = ("names", "prep_times", "locations")

class ADDITIONAL_INFO(forms.ModelForm):
    class Meta:
        model = additional_info_models
        fields = '__all__'
