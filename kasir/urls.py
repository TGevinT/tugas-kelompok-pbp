from django.urls import path
from kasir.views import *

app_name = 'kasir'

urlpatterns= [
   path('', show_kasir, name="show_kasir"),
   path('json/', show_json, name="show_json"),
   path('login/', login_user, name="login_user"),
   path('register/', register, name="register"),
   path('logout/', logout_user, name="logout"),
   path('create/', create_bill_ajax, name="create_bill_ajax" ),
   path('payment/<int:id>', payment_bill_ajax, name="payment_bill_ajax"),
   path('delete/<int:id>', delete_bill_ajax, name="delete_bill_ajax" ),
   path('no_login/', no_login, name="no_login"),
   path('add/', flutter_add, name='flutter_add'),
   path('delete_flutter/<int:pk>/', delete_flutter, name='delete_flutter'),
]

 

