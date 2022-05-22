from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import AccountsModel
from opportunities.models import OpportunitiesModel
from salesbase.list_data import ACC_CON_STATUS_CHOICES


class ContactsModel(models.Model):
    contact_name = models.CharField(max_length=50, null=True, blank=False, verbose_name='Contact Name')
    contact_company = models.ForeignKey(AccountsModel, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Contact Company')
    contact_role = models.CharField(max_length=50, null=True, blank=False, verbose_name='Contact Role')
    contact_opp = models.ForeignKey(OpportunitiesModel, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Contact Opportunity')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Last Updated')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Owner')
    progress = models.CharField(max_length=2, choices=ACC_CON_STATUS_CHOICES, default=ACC_CON_STATUS_CHOICES[0], verbose_name='Status')

    def __str__(self):
        return self.contact_name

    class Meta:
        verbose_name='Contact'
