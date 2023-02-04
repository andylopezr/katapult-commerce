"""
Login route.
"""
from django.contrib.auth.hashers import check_password
from pydantic import SecretStr
from ninja import Schema, Router

from api.controllers.access_token import AccessToken
from user.models import User

router = Router()


class LoginSchema(Schema):
    email: str
    password: SecretStr


@router.post('', auth=None)
def user_login(request, payload: LoginSchema):
    """Login using email and password"""
    try:
        user = User.objects.get(email=payload.email)

    except Exception:
        return {"error": "User not found"}

    if check_password(payload.password.get_secret_value(), user.password):
        return AccessToken.create(user)
