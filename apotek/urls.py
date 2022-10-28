from django.urls import path, include
from . import views
from apotek.views import *

app_name ='apotek'

urlpatterns = [
    path('', show_apotek, name="show_childcare"),
    path('register/', register, name="register"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('json/', show_json, name="show_json"),
    path('json/<int:id>', show_json_by_id, name="json_id"),
    path('add/', add_data, name="add_data"),
    # path('delete/<int:id>', delete_row, name="delete_row"),
    path('no_login/', no_login, name="no_login"),
]