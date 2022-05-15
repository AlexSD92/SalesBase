from django.conf import settings
from django.db import models
from django.urls import reverse
from accounts.models import AccountsModel


class OpportunitiesModel(models.Model):
    opportunity_name = models.CharField(max_length=50, null=True, blank=False)
    opportunity_company = models.CharField(max_length=50, null=True, blank=False)
    # account_name = models.OneToOneField(AccountsModel, on_delete=models.CASCADE)
    # opportunity_value = models.IntegerField(null=True, blank=False)
    # opportunity_close_date = models.DateField(null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.opportunity_name
