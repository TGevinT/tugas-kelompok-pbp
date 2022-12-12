from django.urls import path
from . import views
from checkup.views import *

app_name = 'checkup'

urlpatterns = [
    path('',show_checkup, name='show_checkup'),
    path('register/',register,name='register'),
    path('login/',login_user, name='login_user'),
    path('logout/',logout_user,name='logout_user'),
    path('delete/<int:id>', delete_checkup_ajax, name='delete_checkup_ajax'),
    path('create/', create_checkup_ajax, name='create_checkup_ajax'),
    path('json/',show_json,name='show_json'),
    path('refresh-json/',refresh_json,name='refresh_json'),
    path('no_login',home,name='home'),
    path('flutter-add/', flutter_add, name='flutter_add'),
]


