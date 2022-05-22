from django.db import models
from django.contrib.auth.models import User
from accounts.models import AccountsModel
from salesbase.list_data import OPP_STATUS_CHOICES


class OpportunitiesModel(models.Model):
    opportunity_name = models.CharField(max_length=50, null=True, blank=False, verbose_name='Opportunity Name')
    account_name = models.ForeignKey(AccountsModel, on_delete=models.CASCADE, verbose_name='Opportunity Account')
    opportunity_value = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=False, verbose_name='Opportunity Value')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Last Updated')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Owner')
    progress = models.CharField(max_length=2, choices=OPP_STATUS_CHOICES, default=OPP_STATUS_CHOICES[0], verbose_name='Status')

    def __str__(self):
        return self.opportunity_name

    class Meta:
        verbose_name='Opportunitie'