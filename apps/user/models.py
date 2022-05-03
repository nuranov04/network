from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    username = models.CharField(
        max_length=25,
        unique=True
    )
    first_name = models.CharField(
        max_length=25
    )
    last_name = models.CharField(
        max_length=25
    )
    email = models.EmailField(
        unique=True
    )
    last_activity = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return str(self.username)
