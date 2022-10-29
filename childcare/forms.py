# from attr import field
from django import forms
from .models import *

# class Queue(forms.Form):
#     name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "border-2 rounded-md border-black p-2"}))
#     doctor=forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "border-2 rounded-md border-black p-2"}))
#     description = forms.CharField(widget=forms.TextInput(attrs={"class": "border-2 rounded-md border-black p-2"}))

class Queue(forms.ModelForm):
    class Meta:
        model = Childcare
        fields = ['name', 'doctor', 'description']