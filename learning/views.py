from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

groups = [
    {'id':1, 'name':'Js'},
    {'id':2, 'name':'Jsx'},
    {'id':3, 'name':'Jsv'}
]

def home(request):
    context = {'groups' : groups} #dictionary
    return render(request, 'learning/home.html', context)

def group(request):
    return render(request, 'learning/group.html')