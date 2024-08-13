from django.db import models
from django.contrib.auth.models import AbstractUser
from general.choices import UserGenderType, UserRoleType

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=24, null=True, blank=True)
    last_name = models.CharField(max_length=24, null=True, blank=True)
    phone = models.CharField(max_length=13, null=False, unique=True)
    role = models.CharField(
        max_length=24, default=UserRoleType.user.value,
        choices=UserRoleType.choices)
    gender = models.CharField(
        max_length=14, choices=UserGenderType.choices,
        default=UserGenderType.male.value)
    date_of_birth = models.DateField(null=True, blank=True)