from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Group(models.Model):
    leader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True) #blank is for submission, null is for the database
    # members
    created = models.DateTimeField(auto_now_add=True) #once
    updated = models.DateTimeField(auto_now=True) #every time

    def __str__(self):
        return self.name  #has to be a string if not convert str(value)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True) #once
    updated = models.DateTimeField(auto_now=True) #every time

    def __str__(self):
        return self.body[0:50]
