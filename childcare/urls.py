from django.urls import path, include
from . import views
from childcare.views import *
# TODO: Implement Routings Here

app_name= 'childcare'

urlpatterns= [
   path('', show_childcare, name="show_childcare"),
   path('login/', login_user, name="login"),
   path('register/', register, name="register"),
   path('logout/', logout_user, name="logout"),
   path('json/', show_json, name="show_json"),
]