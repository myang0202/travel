from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    username= models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now= True)

class Trip(models.Model):
    destination = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User,default='')
    travel_from = models.CharField(max_length=100)
    travel_to = models.CharField(max_length=100)
