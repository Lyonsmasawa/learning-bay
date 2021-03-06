from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from learning.forms import GroupForm
from .models import Group, Language, Message
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def loginPage(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
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

    context = { 'page':page}
    return render(request, 'learning/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occurred during registration")

    context = { 'form': form}
    return render(request, 'learning/login_register.html', context)

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    groups = Group.objects.filter(
        Q(language__name__icontains = q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    languages = Language.objects.all()
    group_messages  = Message.objects.filter(Q(group__name__icontains = q))
    group_count = groups.count()

    context = {'groups' : groups, 'languages': languages, 'groups_count': group_count, 'group_messages': group_messages, } #dictionary
    return render(request, 'learning/home.html', context)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    groups = user.group_set.all()
    group_messages = user.message_set.all()
    languages = Language.objects.all()

    context = {'user': user, 'groups': groups, 'group_messages': group_messages, 'languages': languages,}
    return render(request, 'learning/profile.html', context)

def group(request, pk):
    group = Group.objects.get(id = pk)
    group_messages = group.message_set.all().order_by('-created') #many to one
    members = group.members.all() # many to many

    if request.method == 'POST':
        group_message = Message.objects.create(
            user = request.user,
            group = group,
            body = request.POST.get('body')
        )
        group.members.add(request.user)  #add a new member, use remove() to remove a member
        return redirect('group', pk=group.id)

    context = {'group' : group, 'group_messages':group_messages, 'members': members,}
    return render(request, 'learning/group.html', context)

@login_required(login_url='login-page')
def createGroup(request):
    form = GroupForm()
    languages = Language.objects.all()

    if request.method == 'POST':
        # print(request.POST)
        language_name = request.POST.get('language')
        language, created = Language.objects.get_or_create(name=language_name) #returns an object or creates and returns an object
        
        Group.objects.create(
            leader = request.user,
            language = language,
            name = request.POST.get('name'),
            description = request.POST.get('description'),
        )
        return redirect('home')

    context = { 'form': form, 'languages': languages, }
    return render(request, 'learning/create_group.html', context)

@login_required(login_url='login-page')
def updateGroup(request, pk):
    group = Group.objects.get(id = pk)
    form = GroupForm(instance=group)
    languages = Language.objects.all()

    if request.user != group.leader:
        return HttpResponse("You are not authorized")

    if request.method == 'POST':
        language_name = request.POST.get('language')
        language, created = Language.objects.get_or_create(name=language_name) #returns an object or creates and returns an object
        group.name = request.POST.get("name")
        group.language = language
        group.description = request.POST.get("description")
        group.save()
        return redirect('home')

    context = { 'form': form, 'group': group, 'languages': languages,}
    return render(request, 'learning/create_group.html', context)

@login_required(login_url='login-page')
def deleteGroup(request, pk):
    group = Group.objects.get(id=pk)

    if request.user != group.leader:
        return HttpResponse("You are not authorized")

    if request.method == 'POST':
        group.delete()
        return redirect('home')

    context = {'obj' : group }
    return render(request, 'learning/delete.html', context)

@login_required(login_url='login-page')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse("You are not authorized")

    if request.method == 'POST':
        message.delete()
        return redirect('home')

    context = {'obj' : message }
    return render(request, 'learning/delete.html', context)
