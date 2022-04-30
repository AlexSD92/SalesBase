from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy


class RegisterUserView(CreateView):
    form_class = CustomUserForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'