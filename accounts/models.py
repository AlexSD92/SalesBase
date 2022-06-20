from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify


class AccountsModel(models.Model):
    account_name = models.CharField(max_length=100, null=True, blank=False, unique=True, verbose_name='Account Name')
    account_size = models.PositiveIntegerField(null=True, blank=False, verbose_name='# of Employees')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created On')
    updated = models.DateTimeField(auto_now=True, verbose_name='Last Updated')
    owner = models.ForeignKey(User, max_length=100, on_delete=models.CASCADE, verbose_name='Owner')
    slug = models.SlugField(max_length=255, default='', editable=False)    

    def __str__(self):
        return self.account_name

    def get_absolute_url(self):
        return reverse('accounts-detail-view', kwargs={'slug': self.slug, 'pk': self.id})

    def save(self, *args, **kwargs):
        value = self.account_name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name='Account'
