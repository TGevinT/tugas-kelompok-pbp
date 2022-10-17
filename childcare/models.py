from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    doctor = models.TextField()
    description = models.TextField()
    bill = models.IntegerField()
