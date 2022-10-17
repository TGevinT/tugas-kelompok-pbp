from django.urls import path, include
from . import views
from childcare.views import *
# TODO: Implement Routings Here

app_name= 'childcare'

urlpatterns= [
   path('', show_childcare, name="childcare"),
]