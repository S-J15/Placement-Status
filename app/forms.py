from django import forms
from .models import *

class DataForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['prn','name','email','phn','status','div','doc']