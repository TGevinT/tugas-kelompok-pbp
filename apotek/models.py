from django.db import models
from django.contrib.auth.models import User


class Apotek(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    patient_name = models.CharField(max_length=100)
    patient_age = models.IntegerField()
    patient_gender = models.CharField(max_length=50, default='F')
    medicine = models.CharField(max_length=200)
