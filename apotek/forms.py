from django import forms

class Apotek(forms.Form):
    nama_pasien = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "border-2 rounded-md border-black p-2"}))
    umur_pasien = forms.IntegerField(max_length=10, widget=forms.TextInput(attrs={"class": "border-2 rounded-md border-black p-2"}))
