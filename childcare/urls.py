from django.urls import path, include
from . import views
from childcare.views import *
# TODO: Implement Routings Here

app_name= 'childcare'

urlpatterns= [
   path('', show_childcare, name="show_childcare"),
   path('json/', show_json, name="show_json"),
   path('json/<int:id>', show_json_by_id, name="json_id"),
   path('login/', login_user, name="login_user"),
   path('register/', register, name="register"),
   path('logout/', logout_user, name="logout"),
   path('add/', create_ajax, name="create_ajax"),
   path('delete/<int:id>', delete_row, name="delete_row"),
   path('no_login/', no_login, name="no_login"),
]