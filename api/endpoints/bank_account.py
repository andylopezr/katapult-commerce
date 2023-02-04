"""
Bank and Bank Account schemas and routes.
"""
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from ninja import Schema, Router
from ninja.pagination import paginate
from typing import List

from bank.models import BankAccount, Bank
from vendor.models import Vendor

router = Router()


class AccountSchema(Schema):
    account_number: str
    bank: int
    vendor: int


class GetAccountSchema(Schema):
    id: int
    bank_id: str
    account_number: str
    vendor_id: str


@router.post('')
def create_account(request, payload: AccountSchema):
    """Add a new account."""

    if not payload.account_number:
        raise ValueError(_('Enter account number'))

    if not payload.bank:
        raise ValueError(_('Enter bank id'))

    if not payload.vendor:
        raise ValueError(_('Enter vendor id'))

    bank = get_object_or_404(Bank, id=payload.bank)
    vendor = get_object_or_404(Vendor, id=payload.vendor)
    account_form = {
            'account_number': payload.account_number,
            'bank': bank,
            'vendor': vendor,
        }

    account = BankAccount.objects.create(**account_form)

    return {"success": account.account_number}


@router.get('', response=List[GetAccountSchema])
@paginate
def get_accounts(request):
    """List all accounts."""
    all_accounts = BankAccount.objects.all()
    return all_accounts


@router.get('/{account_id}', response=GetAccountSchema)
def get_account(request, account_id: int):
    """List a single account by id."""
    account = get_object_or_404(BankAccount, id=account_id)
    return account


@router.put('/{account_id}')
def update_account(request, account_id: int, payload: AccountSchema):
    """Update an account."""
    if not payload.account_number:
        raise ValueError(_('Enter account number'))

    if not payload.bank:
        raise ValueError(_('Enter bank id'))

    if not payload.vendor:
        raise ValueError(_('Enter vendor id'))

    bank = get_object_or_404(Bank, id=payload.bank)
    vendor = get_object_or_404(Vendor, id=payload.vendor)
    account = get_object_or_404(BankAccount, id=account_id)

    account.account_number = payload.account_number
    account.bank = bank
    account.vendor = vendor
    account.save()
    return {"success": True}


@router.delete('/{account_id}')
def delete_account(request, account_id: int):
    """Delete an account."""
    account = get_object_or_404(BankAccount, id=account_id)
    account.delete()
    return {"success": True}
