from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('creative', 'Creative'),
        ('admin', 'Admin'),
    )
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=32, blank=True, null=True)
    role = models.CharField(max_length=16, choices=ROLE_CHOICES, default='client')
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
