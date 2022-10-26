from django.shortcuts import render
from childcare.models import Childcare
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
def show_childcare(request):

    database = Childcare.objects.all()

    context = {
        'data': database,
        'button_register': 'Register',
        'button_login': 'Login',
    }

    return render(request, 'childcare.html', context)

def show_json(request):

    data = Childcare.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def create_ajax(request):
    if request.method == "POST":
        data_name = request.POST.get("name", "")
        data_title = request.POST.get("doctor", "")
        data_desc = request.POST.get("desc", "")
        model = Childcare(
                    name = data_name,
                    doctor=data_title,
                    description=data_desc)
        model.save()
        return redirect('childcare:show_childcare')

    return render(request, 'childcare.html')

def login(request):
    return render(request, 'login.html')