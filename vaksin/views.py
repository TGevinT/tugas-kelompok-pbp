from django.shortcuts import render, redirect

# Create your views here.
import datetime
from vaksin.models import Vaksin
from vaksin.forms import VaksinForm, LoginForm, RegisterForm
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json

@login_required(login_url='/vaksin/no-login/')
def show_vaksin_info(request):
    form = VaksinForm()
    context = {
        'register_status': 'hidden',
        'login_status': 'hidden',
        'form': form,
        'path': 'vaksin'
        }
    return render(request, "doctor_views.html", context)

def homepage(request):
    context = {
        'logout_status': 'hidden',
        'path': 'vaksin'
    }
    return render(request, "default_views.html", context)

def show_added_vaksin(request):
    vaksin_data = Vaksin.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", vaksin_data))

def show_json(request):
    vaksin_data = Vaksin.objects.all()
    return HttpResponse(serializers.serialize("json", vaksin_data))

@login_required(login_url='/vaksin/login/')
def add_vaksin(request):
    if request.method == "POST":
        form = VaksinForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(username=request.user.username)
            obj.save()
            return HttpResponse(b"CREATED", status=201)
            
    return HttpResponseNotFound()

@login_required(login_url='/vaksin/login/')
def delete_vaksin(request, id):
    vaksin = Vaksin.objects.get(pk=id)
    vaksin.delete()

    return HttpResponse(b"DELETED", status=204)

@login_required(login_url='/vaksin/login/')
def change_dose(request):
    if request.method=="POST":
        new_dose = request.POST.get("vaksin_dose")
        vaksin_id = request.POST.get("vaksin_option")
        vaksin = Vaksin.objects.get(pk=vaksin_id)
        vaksin.dose = float(new_dose)
        vaksin.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('vaksin:login')
    
    context = {
        'form':form,
        'path': 'vaksin',
        'logout_status': 'hidden'
        }
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("vaksin:show_vaksin_info")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {
        'path': 'vaksin',
        'logout_status': 'hidden'
    }
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('vaksin:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def flutter_add(request):
    data = json.loads(request.body)
    name = data['name']
    sideEffect = data['sideEffect']
    dose = data['dose']
    stock = data['stock']
    user = User.object.get(username=request.username)
    if request.method == 'POST':
        vaksin = Vaksin(user=user, name=name, side_effect=sideEffect, dose=dose, stock=stock)
        vaksin.save()
        return JsonResponse({"message": "vaksin berhasil ditambahkan", "status":200}, status=200)

    return JsonResponse({"message": "wrong method", "status":502}, status = 502)