from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.

class Childcare(models.Model):
    name = models.TextField()
    date = models.DateField(auto_now=True)
    doctor = models.TextField()
    description = models.TextField()
    bill = models.IntegerField()
