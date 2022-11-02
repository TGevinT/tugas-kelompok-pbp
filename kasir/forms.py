# from attr import field
from django import forms
from .models import *

class CreateBill(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['patient', 'doctor', 'description', 'bill']
