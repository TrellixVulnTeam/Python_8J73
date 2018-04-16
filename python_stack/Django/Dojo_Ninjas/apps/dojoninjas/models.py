from __future__ import unicode_literals
from django.db import models

class dojo(models.Model):
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    desc = models.TextField(default = " ")
    created_at = models.DateTimeField(auto_now_add = True)     
    update_at = models.DateTimeField(auto_now = True)

class ninja(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    dojo = models.ForeignKey(dojo, related_name = "ninjas", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)     
    update_at = models.DateTimeField(auto_now = True)
# Create your models here.
