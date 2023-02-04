"""
Bank and Bank Account schemas and routes.
"""
from django.shortcuts import get_object_or_404
from ninja import Schema, Router
from ninja.pagination import paginate
from typing import List

from bank.models import Bank

router = Router()


class BankSchema(Schema):
    bank_name: str


class GetBankSchema(Schema):
    id: int
    bank_name: str


@router.post('')
def create_bank(request, payload: BankSchema):
    """Add a new Bank"""
    bank = Bank.objects.create(**payload.dict())
    return {"success": bank.bank_name}


@router.get('', response=List[GetBankSchema])
@paginate
def get_banks(request):
    """List all Banks."""
    all_banks = Bank.objects.all()
    return all_banks


@router.get('/{bank_id}', response=GetBankSchema)
def get_bank(request, bank_id: int):
    """List a single bank by id."""
    bank = get_object_or_404(Bank, id=bank_id)
    return bank


@router.put('/{bank_id}')
def update_bank(request, bank_id: int, payload: BankSchema):
    """Update a bank."""
    bank = get_object_or_404(Bank, id=bank_id)
    for attr, value in payload.dict().items():
        setattr(bank, attr, value)
    bank.save()
    return {"success": True}


@router.delete('/{bank_id}')
def delete_bank(request, bank_id: int):
    """Delete a bank."""
    bank = get_object_or_404(Bank, id=bank_id)
    bank.delete()
    return {"success": True}
