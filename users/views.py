from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateNewUser, UpdateExistingUser, UpdateProfile


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
    if request.method == 'POST':
        u_form = UpdateExistingUser(request.POST, instance=request.user)
        p_form = UpdateProfile(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UpdateExistingUser(instance=request.user)
        p_form = UpdateProfile(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)





