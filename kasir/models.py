from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    doctor = models.CharField(max_length=100)
    patient = models.CharField(max_length=100)
    patient_status_payment = models.BooleanField(default=False)
    description = models.CharField(max_length=9999)
    bill = models.IntegerField()



