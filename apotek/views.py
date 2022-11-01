from django.contrib.auth.decorators import login_required
import datetime

from django.urls import reverse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from apotek.models import Apotek
from apotek.forms import prescription_form, login_form, register_form
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from django.http import HttpResponseRedirect, JsonResponse, HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/apotek/no-login/')
def show_apotek(request):
    data_apotek = Apotek.objects.all()
    context = {
        'list_prescription': data_apotek,
        # 'button_register': 'Register',
        # 'button_login': 'Login',
        'username': request.user.username,
    }

    return render(request, 'apotek.html', context)

def apotek_home(request):
    context = {
        'logout_status': 'hidden',
        'path': 'apotek'
    }
    return render(request, "apotek_nologin.html", context)

@login_required(login_url='/apotek/login/')
def add_prescription(request):
    form = prescription_form
    if request.is_ajax():
        form = prescription_form(request.POST)
        if form.is_valid():
            pick_user = request.user
            new_form = form.save(commit=False)
            new_form.user = pick_user
            new_form.save()
            return JsonResponse({
                'msg': 'Success'
            })

    return render(request, "add_prescription.html", {"apotek":form})


# @login_required(login_url='/apotek/login/')
# def add_prescription(request):
#     if request.method == "POST":
#         form = prescription_form(request.POST)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user = User.objects.get(username=request.user.username)
#             obj.save()
#             return HttpResponse(b"CREATED", status=201)
#
#     return HttpResponseNotFound()



def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('apotek:login')

    context = {'form': form}
    return render(request, 'register.html', context)


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
    context = {'path': 'apotek',
               'logout_status': 'hidden'}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('apotek:login'))
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


# @login_required(login_url='login/')
# def new_prescription(request):
#     if request.method == 'POST':
#         username = request.user
#         # date = datetime.datetime.now()
#         nama_pasien = request.POST.get('nama_pasien')
#         umur_pasien = request.POST.get('umur_pasien')
#         # bonus
#         is_finished = False
#         Apotek.objects.create(nama_pasien=nama_pasien, umur_pasien=umur_pasien)
#         # Apotek.objects.create(user=username, date=date, title=title, description=description, is_finished=is_finished)
#         response = HttpResponseRedirect(reverse("apotek:show_apotek"))
#         return response
#
#     return render(request, "add_prescription.html")
#
#
# @csrf_exempt
# def add_prescription(request):
#     if request.method == 'POST':
#         nama_pasien = request.POST.get('nama_pasien')
#         umur_pasien = request.POST.get('umur_pasien')
#         prescription = Apotek.objects.create(nama_pasien=nama_pasien, umur_pasien=umur_pasien, )
#         result = {
#             'fields': {
#                 'nama_pasien': prescription.nama_pasien,
#                 'umur_pasien': prescription.umur_pasien,
#             },
#             'pk': prescription.pk
#         }
#         return JsonResponse(result)


def show_added_vaksin(request):
    model_prescription = Apotek.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", model_prescription))


def show_json(request):
    model_prescription = Apotek.objects.all()
    return HttpResponse(serializers.serialize("json", model_prescription), content_type="application/json")


@login_required(login_url="login/")
def show_json_by_id(request, id):
    data = Apotek.objects.all().filter(pk=id)

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@login_required(login_url='login/')
def delete_prescription(request, id):
    item = Apotek.objects.get(pk=id)
    item.delete()
    return redirect("apotek:apotek")

# def no_login(request):
#
#     context = {
#         'logout_status': 'hidden',
#         'display_status': 'hidden',
#         'path' : 'childcare'
#     }
#
#     return render(request, 'childcare.html', context)
