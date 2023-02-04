from django.shortcuts import get_object_or_404
from ninja.security import HttpBearer
from jwt import PyJWTError, decode
from django.conf import settings

from user.models import User


class AuthBearer(HttpBearer):
    """Gives access to auth user."""
    def authenticate(self, request, token: str) -> User:
        user = self.get_current_user(token)
        if user:
            return user

    @staticmethod
    def get_current_user(token: str) -> User | None:
        """Check auth user"""
        try:
            payload = decode(
                token,
                settings.SECRET_KEY,
                algorithms=['HS256'])

        except PyJWTError:
            return None
        user = get_object_or_404(User, email=payload['sub'])
        return user
