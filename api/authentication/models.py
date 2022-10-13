from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    class UserType(models.IntegerChoices):
        ADMIN = (1, "Admin")
        MODERATOR = (2, "Moderator")
        DOCTOR = (3, "Doctor")
        PATIENT = (4, "Patient")

    # base fields
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.IntegerField(choices=UserType.choices, default=UserType.PATIENT)

    # personal information
    email = models.EmailField(max_length=320, unique=True)
    first_name = models.CharField(max_length=63, blank=True, null=True)
    last_name = models.CharField(max_length=63, blank=True, null=True)

    def __str__(self):
        return self.email

    @property
    def username(self):
        return self.first_name + " " + self.last_name or self.email.split("@")[0]
