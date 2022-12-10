from django import forms
from vaksin.models import Vaksin, User
from django.contrib.auth.forms import UserCreationForm

class VaksinForm(forms.ModelForm):
    class Meta:
        model = Vaksin
        # fields = '__all__'
        exclude = ('user',)

class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class RegisterForm(forms.Form):
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