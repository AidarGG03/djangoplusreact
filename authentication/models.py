from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    email = models.CharField(max_length=250, unique=True, null=False, blank=False)
    REGISTRATION_CHOICES = [
        ('email', 'Email'),
        ('google', 'Google'),
    ]
    registration_method = models.CharField(
        max_length = 10,
        choices = REGISTRATION_CHOICES,
        default='email'
    )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name = 'custom_user_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name = 'custom_user_permissions'
    )

    def __str__(self):
        return self.username
