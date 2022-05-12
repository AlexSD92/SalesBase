from django.conf import settings
from django.db import models
from django.urls import reverse


class ContactsModel(models.Model):
    contact_name = models.CharField(max_length=50, null=True, blank=False)
    contact_company = models.CharField(max_length=50, null=True, blank=False)
    contact_role = models.CharField(max_length=50, null=True, blank=False)
    contact_opp = models.CharField(max_length=50, null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact_name
