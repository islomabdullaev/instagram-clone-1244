from django.db import models

class UserRoleType(models.TextChoices):
    user = 'user', 'User'
    premium = 'premium', 'Premium'