from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify


class ContactsModel(models.Model):
    contact_name = models.CharField(max_length=100, null=True, blank=False, verbose_name='Contact Name')
    contact_role = models.CharField(max_length=100, null=True, blank=False, verbose_name='Contact Role')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Last Updated')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Owner')
    slug = models.SlugField(max_length=255, default='', editable=False)

    def __str__(self):
        return self.contact_name

    def get_absolute_url(self):
        return reverse('contacts-detail-view', kwargs={'slug': self.slug, 'pk': self.id})

    def save(self, *args, **kwargs):
        value = self.contact_name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name='Contact'
