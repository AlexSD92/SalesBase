from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserForm, CustomUserUpdateForm
from .models import CustomUserModel

class CustomUserAdmin(UserAdmin):
    add_form=CustomUserForm
    form=CustomUserUpdateForm
    model=CustomUserModel
    list_display=[
        'username',
        'first_name',
        'last_name',
        'email',
        'role',
        'is_staff',
    ]
    fieldsets=UserAdmin.fieldsets +((None,{'fields':('role',)}),)
    add_fieldsets=UserAdmin.add_fieldsets +((None,{'fields':('role',)}),)

admin.site.register(CustomUserModel, CustomUserAdmin)
