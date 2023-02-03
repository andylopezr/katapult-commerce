"""
User and superuser manager.
"""
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
import re


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email: str, password=None, **extra_fields):
        """
        Create save and return a User with the given email and password.
        """

        e = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        p = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[!@#?\]]).{8,}$'

        if not email:
            raise ValueError(_('Enter email'))

        if not re.fullmatch(e, email):
            raise ValueError(_('Invalid email'))

        if not password:
            raise ValueError(_('Enter password'))

        if not re.fullmatch(p, password):
            raise ValueError(_('Password does not comply with requirements'))

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user