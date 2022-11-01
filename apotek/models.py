from django.db import models
from django.contrib.auth.models import User


class Apotek(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nama_pasien = models.CharField(max_length=100)
    umur_pasien = models.IntegerField(max_length=3)
    # restock_date = models.CharField(max_length=30)
    # restock_time = models.DateTimeField(auto_now_add=True)
    # medicine = models.CharField(max_length=30)
    # description = models.CharField(max_length=300)
    # is_finished = models.BooleanField(null=True, blank=True)
