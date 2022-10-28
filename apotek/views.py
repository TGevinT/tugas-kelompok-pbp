from django.contrib.auth.decorators import login_required
import datetime

from django.urls import reverse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from apotek.models import Apotek
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.core import serializers


# Create your views here.
def show_apotek(request):
    database = Apotek.objects.all()

    context = {
        'data': database,
        'button_register': 'Register',
        'button_login': 'Login',
    }

    return render(request, 'apotek.html', context)


def show_json(request):
    data = Apotek.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url="login/")
def show_json_by_id(request, id):

    data = Apotek.objects.all().filter(pk = id)

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse('todolist:todolist'))  # membuat response
            response.set_cookie('last_login',
                                str(datetime.datetime.now()))  # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau password tidak tepat')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

# def create_ajax(request):
#     if request.method == "POST":
#         data_name = request.POST.get("name", "")
#         data_title = request.POST.get("doctor", "")
#         data_desc = request.POST.get("desc", "")
#         model = Apotek(
#             name=data_name,
#             doctor=data_title,
#             description=data_desc)
#         model.save()
#         return redirect('apotek:show_apotek')
#
#     return render(request, 'apotek.html')

@csrf_exempt
def add_data(request):
    if request.method == 'POST':
        nama_pasien = request.POST.get('nama_pasien')
        umur_pasien = request.POST.get('umur_pasien')
        data = Apotek.objects.create(user=request.user, date=datetime.date.today(), title=title, description=description,)
        result = {
            'fields': {
                'nama_pasien': data.title,
                'umur_pasien': data.date,
                'resep_obat': data.meds_list,
            },
            'pk': data.pk
        }
        return JsonResponse(result)


def checkbox_meds(request):
    meds_list = ['Antibiotik', 'Paracetamol', 'Ibuprofen', 'Salep alergi', 'Anti-inflamasi', 'Anti-depresi']
    if request.method == "POST":
        meds = request.POST.getlist('meds')
        print('meds')
    return render(request, 'register.html')

def no_login(request):

    context = {
        'logout_status': 'hidden',
        'display_status': 'hidden',
        'path' : 'childcare'
    }

    return render(request, 'childcare.html', context)
