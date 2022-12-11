from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.

class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Childcare(Staff):
    name = models.CharField(max_length = 100)
    date = models.DateField(auto_now=True)
    doctor = models.CharField(max_length = 100)
    description = models.CharField(max_length = 9999)