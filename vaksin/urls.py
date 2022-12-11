from django.urls import path
from vaksin.views import show_vaksin_info, add_vaksin, show_json, login_user, register, logout_user, show_added_vaksin, delete_vaksin
from vaksin.views import change_dose, homepage, flutter_add

app_name = 'vaksin'

urlpatterns = [
    path('', show_vaksin_info, name='show_vaksin_info'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('json/', show_json, name='show_json'),
    path('json1/', show_added_vaksin, name='show_added_vaksin'),
    path('add/', add_vaksin, name='add_vaksin'),
    path('change/', change_dose, name='change_dose'),
    path('delete-vaksin/<int:id>', delete_vaksin, name='delete_vaksin'),
    path('no-login/', homepage, name='homepage'),
    path('flutter-add/', flutter_add, name='flutter_add'),
]