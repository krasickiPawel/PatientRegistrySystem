from django.contrib.auth.base_user import BaseUserManager
from .models import User


class UserManager(BaseUserManager):
    class UserManager(BaseUserManager):
        def create_user(self, email, password=None):
            if email is None:
                raise ValueError("Users must have an email address")

            user = self.model(
                email=self.normalize_email(email),
            )

            user.set_password(password)
            user.save(using=self._db)
            return user

        def create_superuser(self, email, password):
            if password is None:
                raise TypeError("Superusers must have a password.")
            if email is None:
                raise TypeError("Superusers must have an email address.")

            user = self.create_user(email, password)
            user.is_superuser = True
            user.is_staff = True
            user.type = User.UserType.ADMIN
            user.save(using=self._db)
            return user

        # TODO: maybe add a method to create a doctor or a patient
