from tkinter import CASCADE
from django.db import models
from users.models import CustomUserModel


class AccountsModel(models.Model):
    account_name = models.TextField(max_length=50, null=True, blank=False)
    account_ind = models.TextField(max_length=50, null=True, blank=False)
    account_size = models.PositiveIntegerField(null=True, blank=False)
    account_rev = models.PositiveIntegerField(null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.account_name
