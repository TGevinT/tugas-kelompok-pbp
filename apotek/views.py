from django.shortcuts import render
from apotek.models import Apotek
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def show_apotek(request):
    database = Apotek.objects.all()

    context = {
        'data': database,
        'button_register': 'Register',
        'button_login': 'Login',
    }

    return render(request, 'apotek_main.html', context)


def show_json(request):
    data = Apotek.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def create_ajax(request):
    if request.method == "POST":
        data_name = request.POST.get("name", "")
        data_title = request.POST.get("doctor", "")
        data_desc = request.POST.get("desc", "")
        model = Apotek(
            name=data_name,
            doctor=data_title,
            description=data_desc)
        model.save()
        return redirect('apotek:show_apotek')

    return render(request, 'apotek.html')


def login(request):
    return render(request, 'login.html')
