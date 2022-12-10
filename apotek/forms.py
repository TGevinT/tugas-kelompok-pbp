from django import forms
from .models import *


class CreatePrescription(forms.ModelForm):
    class Meta:
        model = Apotek
        fields = ['patient_name', 'patient_age', 'patient_gender', 'medicine']