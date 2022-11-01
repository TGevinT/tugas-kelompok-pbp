from django import forms
from apotek.models import Apotek, User
from django.contrib.auth.forms import UserCreationForm


class prescription_form(forms.ModelForm):
    class Meta:
        model = Apotek
        exclude = ('user',)


class login_form(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class register_form(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = {'username', 'password1','password2', 'is_doctor', 'is_patient'}

# class Apotek(forms.Form):
#     nama_pasien = forms.CharField(max_length=100,
#                                   widget=forms.TextInput(attrs={"class": "border-2 rounded-md border-black p-2"}))
#     umur_pasien = forms.IntegerField(max_length=10,
#                                      widget=forms.TextInput(attrs={"class": "border-2 rounded-md border-black p-2"}))
