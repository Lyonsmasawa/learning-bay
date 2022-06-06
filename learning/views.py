from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render

from learning.forms import GroupForm
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
    form = GroupForm()

    if request.method == 'POST':
        # print(request.POST)
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = { 'form': form, }
    return render(request, 'learning/create_group.html', context)

def updateGroup(request, pk):
    group = Group.objects.get(id = pk)
    form = GroupForm(instance=group)

    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = { 'form': form, 'group': group}
    return render(request, 'learning/create_group.html', context)

def deleteGroup(request, pk):
    group = Group.objects.get(id=pk)

    if request.method == 'POST':
        group.delete()
        return redirect('home')

    context = {'obj' : group }
    return render(request, 'learning/delete.html', context)