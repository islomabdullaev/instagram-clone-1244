from django.db import models
from django.contrib.auth.models import AbstractUser
from general.choices import UserRoleType

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=24, null=True, blank=True)
    last_name = models.CharField(max_length=24, null=True, blank=True)
    phone = models.CharField(max_length=13, null=False, unique=True)
    role = models.CharField(
        max_length=24, default=UserRoleType.user.value,
        choices=UserRoleType.choices)
    date_of_birth = models.DateField()