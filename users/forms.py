from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from users.models import CustomUserModel

class CustomUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUserModel
        fields = UserCreationForm.Meta.fields+('role',)

class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model=CustomUserModel
        fields=UserChangeForm.Meta.fields