from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class CreateNewUser(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__ (self, *args, **kwargs):
        super(CreateNewUser, self).__init__(*args, **kwargs)
        del self.fields ['email']


class UpdateExistingUser(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username']

    def __init__ (self, *args, **kwargs):
        super(UpdateExistingUser, self).__init__(*args, **kwargs)
        del self.fields ['email']


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']