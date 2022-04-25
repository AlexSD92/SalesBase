from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib.auth import login
from django.contrib import messages

def LoginView(request):
    return render(request, 'users/login.html')

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