'''
Version 1.0
Authors: Eddy Wang
Last Updated: June 1, 2023
'''

#import statements
from django import forms
from calendars.models import CSV_FILE
from calendars.models import additional_info_models

# For CSV file upload (including all fields)
class CSV_FILE_FORM(forms.ModelForm):
    class Meta:
        model = CSV_FILE
        fields = ("names", "prep_times", "locations")

# For Additional Information form (including all fields)
class ADDITIONAL_INFO(forms.ModelForm):
    class Meta:
        model = additional_info_models
        fields = '__all__'
