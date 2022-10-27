from django.shortcuts import render
from childcare.models import Childcare
from django.http import HttpResponse, JsonResponse
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
from .forms import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url="login/")
def show_childcare(request):

    database = Childcare.objects.all()
    form = Queue()

    context = {
        'data': database,
        'button_register': 'Register',
        'button_login': 'Login',
        'form' : form,
    }

    return render(request, 'childcare.html', context)

def show_json(request):

    data = Childcare.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url="login/")
def show_json_by_id(request, id):

    data = Childcare.objects.all().filter(pk = id)

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('childcare:show_childcare')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/childcare/login/')
    
    context = {'form':form}
    return render(request, 'register.html', context)

@login_required(login_url="login/")
def logout_user(request):
    logout(request)
    return redirect('childcare:login_user')

@login_required(login_url="login/")
def create_ajax(request):
    if request.method == "POST":
        data_name = request.POST.get("name", "")
        data_doctor = request.POST.get("doctor", "")
        data_desc = request.POST.get("description", "")
        model = Childcare(
                    user = request.user,
                    name = data_name,
                    doctor = data_doctor,
                    description = data_desc
                    )

        model.save()
        return JsonResponse({})

@login_required(login_url="login/")
def delete_row(request, id):
    if request.method == "POST":
        data = Childcare.objects.all().filter(pk = id)
        data.delete()
        return JsonResponse({})