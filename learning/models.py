from turtle import update
from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) #blank is for submission, null is for the database
    # members
    created = models.DateTimeField(auto_now_add=True) #once
    updated = models.DateTimeField(auto_now=True) #every time

    def __str__(self):
        return self.name  #has to be a string if not convert str(value)