"""
User schemas and routes.
"""
from django.shortcuts import get_object_or_404
from django.db.utils import IntegrityError
from ninja import Schema, Router
from ninja.pagination import paginate
from typing import List

from user.models import User

router = Router()


class UserSchema(Schema):
    email: str
    password: str


class GetUserSchema(Schema):
    id: int
    email: str


class Success(Schema):
    success: str


class Error(Schema):
    message: str


@router.post('', auth=None, response={200: Success, 409: Error})
def create_user_api(request, payload: UserSchema):
    """

        Create a new user using email and password.

        Password constrains:

            - At least 8 characters long.

            - Should include one lowercase letter.

            - Should include one UPPERCASE letter.

            - Should include one of these special characters: ! @ # ? ]

    """

    try:
        user = User.objects.create_user(
            payload.email,
            payload.password,
        )

    except IntegrityError:
        return 409, {"message": 'Email already exists!'}

    return 200, {"success": user.email}


@router.get('', response=List[GetUserSchema], auth=None)
@paginate
def get_users(request):
    """Lists all users."""
    all_users = User.objects.all()
    return all_users


@router.get('/{user_id}', response=GetUserSchema, auth=None)
def get_user(request, user_id: int):
    """List a single user by id."""
    user = get_object_or_404(User, id=user_id)
    return user


@router.put('/{user_id}', auth=None)
def update_user(request, user_id: int, payload: UserSchema):
    """Update user attributes."""
    user = get_object_or_404(User, id=user_id)

    for attr, value in payload.dict().items():
        setattr(user, attr, value)
        if payload.password:
            user.set_password(payload.password)
    user.save()
    return {"success": True}


@router.delete('/{user_id}', auth=None)
def delete_user(request, user_id: int):
    """Delete a user by id."""
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return {"success": True}
