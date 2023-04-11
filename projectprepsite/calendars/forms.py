from django import forms
from calendars.models import CSV_FILE

class EventsForm(forms.ModelForm):
    file = forms.FileField()

class CSV_FILE_FORM(forms.ModelForm):
    class Meta:
        model = CSV_FILE
        fields = ("names", "prep_times", "locations")
