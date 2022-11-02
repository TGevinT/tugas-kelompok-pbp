from datetime import datetime
from http.client import HTTPResponse
from venv import create
from django.shortcuts import *
from checkup.models import Checkup,Staff
from django.contrib.auth import authenticate,login,logout
from django.http import *
from django.views.decorators.csrf import *
from django.urls import *
from django.contrib import messages
from checkup.forms import forms, form_checkup
from django.contrib.auth.decorators import login_required
from django.core import serializers



# show_checkup
@login_required(login_url='/checkup/login/')
def show_checkup(request):
    data_checkup = Checkup.objects.filter(user=request.user)
    form = form_checkup()
    context = {
        'register_status':'hidden',
        'login_status':'hidden',
        'form' : form,
        'path': 'checkup'
    }
    print(context)
    return render(request, "checkup.html", context)
# register
def register(request):
    form = form_checkup()

    if request.method == "POST":
        form = form_checkup(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created!')
            return redirect('checkup:login')
        else:
            messages.error(request, "Unsuccessful registration")
            form = form_checkup()
    context = {'form':form,'path':'checkup','logout_status':'hidden'}
    return render(
        request, 
        'register.html', 
        context)
# login
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            response = HttpResponseRedirect(reverse("checkup:show_checkup")) 
            return response
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {'path':'checkup','logout_status':'hidden'}
    return render(
        request, 
        'login.html', 
        context)
# logout
def logout_user(request):
    logout(request)
    messages.info(request,"You have successfully logged out")
    return redirect('checkup:login_user')


@csrf_exempt
@login_required(login_url='/checkup/login/')
def delete_checkup_ajax(request,pk):
    data_checkup = Checkup.objects.get(id=pk)
    if request.method == 'POST':
        data_checkup.delete()
        return JsonResponse({"checkup":"delete checkup"})
        
@login_required(login_url='/checkup/login/')
def create_checkup_ajax(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        doctor = request.POST.get('doctor')
        status_checkup_type = request.POST.get('status_checkup_type')
        recommendations = request.POST.get('recommendations')
        paid = request.POST.get('paid')
        if paid == "true":
            paid = True
        else:
            paid = False
        create = Checkup(user=request.user,name=name,date=date,doctor=doctor,status_checkup_type=status_checkup_type,recommendations=recommendations,paid=paid)
        create.save()
        return JsonResponse({"checkup":"new checkup"},status=200)

@login_required(login_url="login/")
def show_json(request):
    data_checkup = Checkup.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json',data_checkup),content_type='application/json')

def home(request):
    context = {
        'logout_status' : 'hidden',
        'display_status':'hidden',
        'path':'checkup'
    }
    return render(request,'checkup.html',context)

def refresh_json(request,id):
    data_checkup = Checkup.objects.filter(pk=id)
    return HTTPResponse(serializers.serialize('json',data_checkup),content_type='application/json')
