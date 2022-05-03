from .forms import CustomUserForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class RegisterUserView(CreateView):
    form_class = CustomUserForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'