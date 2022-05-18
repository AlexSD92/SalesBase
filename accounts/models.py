from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class AccountsModel(models.Model):
    account_name = models.CharField(max_length=50, null=True, blank=False, unique=True, verbose_name='Account Name')
    account_ind = models.CharField(max_length=50, null=True, blank=False, verbose_name='Account Industry')
    account_size = models.PositiveIntegerField(null=True, blank=False, verbose_name='# of Employees')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created On')
    updated = models.DateTimeField(auto_now=True, verbose_name='Last Updated')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Owner')

    def __str__(self):
        return self.account_name

    class Meta:
        verbose_name='Account'
