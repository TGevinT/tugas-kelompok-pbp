from django.urls import path, include
from apotek.views import *

app_name = 'apotek'

urlpatterns = [
    path('', show_apotek, name="show_apotek"),
    path('register/', register, name="register"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('json/', show_json, name="show_json"),
    # path('json/<int:id>', show_json_by_id, name="json_id"),
    path('add/', add_prescription, name="add_prescription"),
    path('no_login/', no_login, name="no_login"),
]