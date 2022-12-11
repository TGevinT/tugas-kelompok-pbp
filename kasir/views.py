from django.shortcuts import render, redirect
from kasir.models import *
from kasir.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

@login_required(login_url="no_login/")
def show_kasir(request):
    data_object = Data.objects.all()
    form = CreateBill()
    context = {
        'data_object': data_object,
        'register_status': 'hidden',
        'login_status': 'hidden',
        'form' : form,
        'path' : 'kasir',
    }
    return render(request, 'kasir.html', context)

def show_json(request):

    data = Data.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('kasir:show_kasir')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {
        "logout_status": 'hidden',
        'path' : 'kasir'
    }
    return render(request, 'login_kasir.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/kasir/login/')
    
    context = {
        'form':form,
        'path' : 'kasir',
        'logout_status' : 'hidden'
        }
    return render(request, 'register_kasir.html', context)

@login_required(login_url="login/")
def logout_user(request):
    logout(request)
    return redirect('kasir:login_user')


@login_required(login_url="login/")
def create_bill_ajax(request):
    if request.method == 'POST':
        patient = request.POST.get('patient')
        doctor = request.POST.get('doctor')
        description = request.POST.get('description')
        bill = request.POST.get('bill')
        user = request.user

        Data.objects.create(
            user = user,
            patient = patient,
            doctor = doctor,
            description = description,
            bill = bill,
        )
    

    return JsonResponse({}, status=200)

@login_required(login_url="login/")
def payment_bill_ajax(request, id):
    data = Data.objects.get(pk=id)
    kembalian = 0
    payment = False
    if request.method == 'POST':
        money_paid = int(request.POST.get('money_paid'))
        if(money_paid - data.bill >= 0):
            data.patient_status_payment = not data.patient_status_payment
            kembalian = money_paid - data.bill
            payment = True
            data.save()
    print(kembalian, payment)
    return JsonResponse({'kembalian': kembalian, 'payment': payment})

@login_required(login_url="login/")
def delete_bill_ajax(request, id):
    if request.method == 'POST':
        task = Data.objects.get(pk=id)
        task.delete()
    return JsonResponse({}, status=200)

def no_login(request):
    context = {
        'logout_status': 'hidden',
        'button_show' :'hidden',
        'path' : 'kasir',
    }

    return render(request, 'kasir.html', context)

@csrf_exempt
def flutter_add(request):
    if request.method == 'POST':
        patient = request.POST.get('patient')
        doctor = request.POST.get('doctor')
        description = request.POST.get('description')
        bill = request.POST.get('patient')
        user = request.user

        data = Data(
            user = user,
            patient = patient,
            doctor = doctor,
            description = description,
            bill = bill
        )
        data.save()
        return JsonResponse({}, status=200)

@csrf_exempt
def flutter_add(request):
    data = json.loads(request.body)
    patient = data['patient']
    doctor = data['doctor']
    description = data['description']
    bill = data['bill']
    if request.method == 'POST':
        kasir = Data(
                    user = request.user,
                    patien = patient,
                    doctor = doctor,
                    description = description,
                    bill = bill
                    )
        kasir.save()
        return JsonResponse({"message": "Kasir Data berhasil ditambahkan", "status":200}, status=200)

    return JsonResponse({"message": "wrong method", "status":502}, status = 502)



