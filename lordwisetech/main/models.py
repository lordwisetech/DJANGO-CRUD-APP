from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class data(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    mobie = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)

    def __str__(self):
        return self.name







