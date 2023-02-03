from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.shortcuts import get_object_or_404
from datetime import timedelta, datetime
from ninja import NinjaAPI, Schema
from ninja.security import HttpBearer
from jwt import encode, PyJWTError, decode

from user.models import User


class TokenPayload(Schema):
    user_id: int = None


class AuthBearer(HttpBearer):
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

# Django Ninja AccessToken --------------------------------------------------


class AccessToken:
    @staticmethod
    def create(user: User) -> dict:
        email = user.email
        access_token_expires = timedelta(minutes=999999)
        token = AccessToken.create_token(
            data={"sub": email},
            expires_delta=access_token_expires,
        )
        user.save()
        return {
            "email": email,
            "access_token": token,
        }

    @staticmethod
    def create_token(data: dict, expires_delta: timedelta = None) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = encode(
            to_encode, settings.SECRET_KEY, algorithm="HS256"
        )
        return encoded_jwt


api = NinjaAPI(
    auth=AuthBearer(),
    title='Citation',
    version="0.1.0",
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
