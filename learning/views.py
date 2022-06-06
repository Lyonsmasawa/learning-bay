from django.shortcuts import redirect, render
from django.db.models import Q
from learning.forms import GroupForm
from .models import Group, Language
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User doesn't exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Username or password is Invalid')

    context = { }
    return render(request, 'learning/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    groups = Group.objects.filter(
        Q(language__name__icontains = q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    languages = Language.objects.all()
    group_count = groups.count()

    context = {'groups' : groups, 'languages': languages, 'groups_count': group_count, } #dictionary
    return render(request, 'learning/home.html', context)

def group(request, pk):
    group = Group.objects.get(id = pk)

    context = {'group' : group}
    return render(request, 'learning/group.html', context)

@login_required(login_url='login-page')
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

@login_required(login_url='login-page')
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

@login_required(login_url='login-page')
def deleteGroup(request, pk):
    group = Group.objects.get(id=pk)

    if request.method == 'POST':
        group.delete()
        return redirect('home')

    context = {'obj' : group }
    return render(request, 'learning/delete.html', context)
