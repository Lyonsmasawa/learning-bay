from multiprocessing import context
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

def group(request, pk):
    group = None
    for i in groups:
        if i['id'] == int(pk):
            group = i

    context = {'group' : group}
    return render(request, 'learning/group.html', context)