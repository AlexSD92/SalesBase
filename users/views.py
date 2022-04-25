from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def LoginView(request):
    return render(request, 'users/login.html')

def DashboardView(request):
    return render(request, 'users/dashboard.html')

def RegisterUserView(request):
    if request.method =='POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return render(request, 'users/login.html')
        messages.error(request, 'Unsuccessful registration. Invalid information.')
    form = RegisterUserForm()
    return render(request, 'users/register.html', context={'RegisterForm':form})

def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return render(request, 'users/dashboard.html')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request, 'users/login.html', context={'LoginForm':form})