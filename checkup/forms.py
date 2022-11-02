from django import forms
from checkup.models import Checkup

class form_checkup(forms.ModelForm):
    class Meta:
        model = Checkup
        fields = ('name','date','doctor','status_checkup_type','recommendations','paid')

    # validate patient name
    def clean_patient_name(self):
        name = self.cleaned_data.get('name')
        if (name == ""):
            raise forms.ValidationError('This field cannot be blank')
        return name
    
    # validate doctor name
    def clean_doctor_name(self):
        doctor = self.cleaned_data.get('doctor')
        if (doctor == ""):
            raise forms.ValidationError('This field cannot be blank')
        return doctor
