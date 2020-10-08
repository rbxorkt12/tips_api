from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    KIND_LIST = (
        ('U','Undergraduate'),
        ('G','Graduated')
    )
    user_kind = models.CharField(max_length=1, choices=KIND_LIST)
# Create your models here.
