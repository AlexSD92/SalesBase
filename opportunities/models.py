from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import AccountsModel


class OpportunitiesModel(models.Model):
    opportunity_name = models.CharField(max_length=50, null=True, blank=False, verbose_name='Opportunity Name')
    account_name = models.ForeignKey(AccountsModel, on_delete=models.CASCADE, verbose_name='Opportunity Account')
    opportunity_value = models.PositiveIntegerField(null=True, blank=False, verbose_name='Opportunity Value')
    # opportunity_contacts = models.ManyToManyField(ContactsModel, on_delete=models.CASCADE, verbose_name='Opportunity Contacts')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Last Updated')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Owner')

    def __str__(self):
        return self.opportunity_name

    class Meta:
        verbose_name='Opportunitie'