from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    role = models.CharField(max_length=40,null=True,blank=False)
