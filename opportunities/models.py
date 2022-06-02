from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import AccountsModel
from salesbase.list_data import OPP_STATUS_CHOICES
from django.utils.text import slugify
from djmoney.models.fields import MoneyField


class OpportunitiesModel(models.Model):
    opportunity_name = models.CharField(max_length=50, null=True, blank=False, verbose_name='Opportunity Name')
    account_name = models.ForeignKey(AccountsModel, on_delete=models.CASCADE, verbose_name='Opportunity Account')
    opportunity_value = MoneyField(max_digits=20, decimal_places=2, null=True, blank=False, default_currency='GBP', verbose_name='Opportunity Value')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Last Updated')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Owner')
    progress = models.CharField(max_length=2, choices=OPP_STATUS_CHOICES, default=OPP_STATUS_CHOICES[0], verbose_name='Status')
    slug = models.SlugField(default='', editable=False)

    def __str__(self):
        return self.opportunity_name

    def get_absolute_url(self):
        return reverse('opportunities-detail-view', kwargs={'slug': self.slug, 'pk': self.id})

    def save(self, *args, **kwargs):
        value = self.opportunity_name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name='Opportunitie'