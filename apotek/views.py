from django.contrib.auth.decorators import login_required
import datetime

from django.urls import reverse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from apotek.models import Apotek
from apotek.forms import CreatePrescription
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.core import serializers


def no_login(request):
    context = {
        'path': 'apotek',
        'logout_status': 'hidden',
        'button': 'hidden',
    }
    return render(request, 'apotek_nologin.html', context)

@login_required(login_url="login/")
def show_json(request):
    data = Apotek.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@login_required(login_url="no_login/")
def show_apotek(request):
    data_apotek = Apotek.objects.all()
    form = CreatePrescription()
    context = {
        'data_apotek': data_apotek,
        'register_status': 'hidden',
        'login_status': 'hidden',
        'form': form,
        'path': 'apotek',
    }
    return render(request, 'apotek.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse('apotek:show_apotek'))  # membuat response
            response.set_cookie('last_login',
                                str(datetime.datetime.now()))  # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau password tidak tepat')
    context = {}
    return render(request, 'login.html', context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/apotek/login/')

    context = {
        'form': form,
        'path': 'apotek',
        'logout_status': 'hidden'
    }
    return render(request, 'register.html', context)


@login_required(login_url="login/")
def logout_user(request):
    logout(request)
    return redirect('apotek:login')


@login_required(login_url="login/")
def add_prescription(request):
    if request.method == 'POST':
        user = request.user
        patient_name = request.POST.get('patient_name')
        patient_age = request.POST.get('patient_age')
        patient_gender = request.POST.get('patient_gender')
        medicine = request.POST.get('medicine')

        Apotek.objects.create(
            user=user,
            patient_name=patient_name,
            patient_age=patient_age,
            patient_gender=patient_gender,
            medicine=medicine,
        )
    return JsonResponse({}, status=200)

