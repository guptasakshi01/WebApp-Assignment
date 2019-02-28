from django.db import  models
import csv
from django.utils import timezone
from django.contrib.auth.models import  User

class csvdata(models.Model):
    key = models.TextField(max_length=100)
    value = models.TextField()

    def __str__(self):
        return self.key



