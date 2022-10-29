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

@login_required(login_url='/vaksin/login/')
def show_vaksin_info(request):
    form = VaksinForm()
    context = {'form': form}
    return render(request, "doctor_views.html", context)

def show_vaksin_history(request):
    vaksin_data = Vaksin.objects.filter(user=request.user)
    context={'list_vaksin': vaksin_data}
    return render(request, "patient_views.html", context)

def show_json(request):
    vaksin_data = Vaksin.objects.all()
    return HttpResponse(serializers.serialize("json", vaksin_data))

def add_vaksin(request):
    if request.method == "POST":
        form = VaksinForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(username=request.user.username)
            obj.save()
            return HttpResponse(b"CREATED", status=201)
            
    return HttpResponseNotFound()

def delete_vaksin(request, id):
    vaksin = Vaksin.objects.get(pk=id)
    vaksin.delete()

    return HttpResponse(b"DELETED", status=204)

def change_dose(request):
    if request.method=="POST":
        new_dose = request.POST.get("vaksin_dose")
        vaksin_id = request.POST.get("vaksin_option")
        vaksin = Vaksin.objects.get(pk=vaksin_id)
        vaksin.dose = new_dose
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
    
    context = {'form':form}
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
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('vaksin:login'))
    response.delete_cookie('last_login')
    return response