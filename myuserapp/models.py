from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    homepage = models.URLField(null=True, blank=True)
    display_name = models.CharField(max_length=40, blank=True, unique=True)

    REQUIRED_FIELDS = ['age', 'display_name', 'homepage']

    def __str__(self):
        return f"{self.display_name}"
