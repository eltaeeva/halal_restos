from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models

import database
from database.models import Restaurants, Mosque
from .forms import CreateUserForm, ProfileForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url = 'login')
def index(request):
    return render(request, 'profileapp/home.html')

@login_required(login_url = 'login')
def about(request):
    return render(request, 'profileapp/about_us.html')

@login_required(login_url = 'login')
def restos(request):
    restos = Restaurants.objects.all()
    return render(request, 'profileapp/restos_all.html', {'restos': restos})

@login_required(login_url = 'login')
def resto_detail(request):
    return render(request, 'profileapp/resto_detail.html')

@login_required(login_url = 'login')
def mosques(request):
    mosques = Mosque.objects.all()
    return render(request, 'profileapp/mosques_all.html', {'mosques': mosques})

@login_required(login_url = 'login')
def mosque_details(request):
    return render(request, 'profileapp/mosque_details.html')

@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, Your profile is updated.')
            return redirect('/')
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {'form':form}
    return render(request, 'profileapp/profile.html', context)

def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'{username}, You are logged in.')
            return redirect("/")
        else:
            messages.info(request, 'Wrong password or username')
            return redirect('login')
    return render(request, 'profileapp/login_page.html')
#gggjjj
def register_user(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Аккаунт успешно создан!')
            return redirect('login')
        else:
            context = {'form': form}
            messages.info(request, 'Неверные данные!')
            return redirect('register')

    context = {'form': form}
    return render(request, 'profileapp/register_page.html', context)

@login_required(login_url = 'login')
def logout_user(request):
    logout(request)
    messages.info(request, 'You logged out successfully')
    return redirect('login')