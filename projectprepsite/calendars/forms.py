from django import forms
from calendars.models import CSV_FILE

SEM_TYPES_CHOICES = (
    ("Non-Semestered", "Non-Semestered"),
    ("Semestered", "Semestered")
)

SCHOOL_BOARD_CHOICES = (
    ("OCDSB", "OCDSB"),
    ("OCSB", "OCSB"),
    ("N/A", "N/A")
)

class EventsForm(forms.ModelForm):
    file = forms.FileField()

class CSV_FILE_FORM(forms.ModelForm):
    class Meta:
        model = CSV_FILE
        fields = ("names", "prep_times", "locations")

class ADDITIONAL_INFO(forms.Form):
    sem_type = forms.ChoiceField(choices=SEM_TYPES_CHOICES)
    start_date = forms.DateField()
    end_date = forms.DateField()
    school_board = forms.ChoiceField(choices=SCHOOL_BOARD_CHOICES)
