from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateNewUser


def RegisterUserView(request):
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = CreateNewUser()
    return render(request, 'users/register.html', {'form': form})

def Profile(request):
    return render(request, 'users/profile.html')


