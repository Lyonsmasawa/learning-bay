from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Group

# Create your views here.
def home(request):
    groups = Group.objects.all()

    context = {'groups' : groups} #dictionary
    return render(request, 'learning/home.html', context)

def group(request, pk):
    group = Group.objects.get(id = pk)

    context = {'group' : group}
    return render(request, 'learning/group.html', context)

def createGroup(request):
    
    context = {  }
    return render(request, 'learning/create_group.html', context)
