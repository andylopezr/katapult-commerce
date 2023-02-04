"""
Vendor schemas and routes.
"""
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from ninja import Schema, Router
from ninja.pagination import paginate
from typing import List
import re

from vendor.models import Vendor

router = Router()

nit = r'(^[0-9]+-{1}[0-9]{1})'
phone = r'^[0-9]*$'


class VendorSchema(Schema):
    vendor_name: str
    vendor_nit: str
    contact_name: str
    contact_phone: str


class GetVendorSchema(Schema):
    id: int
    vendor_name: str
    vendor_nit: str
    contact_name: str
    contact_phone: str


@router.post('')
def create_vendor(request, payload: VendorSchema):
    """"Add a new vendor."""

    if not payload.vendor_name:
        raise ValueError(_('Enter Vendor Name'))

    if not payload.vendor_nit:
        raise ValueError(_('Enter Vendor NIT'))

    if not re.fullmatch(nit, payload.vendor_nit):
        raise ValueError(_('NIT is incomplete'))

    if not payload.contact_name:
        raise ValueError(_('Enter Vendor Contact Name'))

    if not payload.contact_phone:
        raise ValueError(_('Enter Vendor Contact Number'))

    if not re.fullmatch(phone, payload.contact_phone):
        raise ValueError(_('Invalid Contact Number'))

    vendor_form = {
        'vendor_name': payload.vendor_name,
        'vendor_nit': payload.vendor_nit,
        'contact_name': payload.contact_name,
        'contact_phone': payload.contact_phone,
        }

    vendor = Vendor.objects.create(**vendor_form)

    return {"success": vendor.vendor_name}


@router.get('', response=List[GetVendorSchema])
@paginate
def get_vendors(request):
    """List all vendors."""
    all_vendors = Vendor.objects.all()
    return all_vendors


@router.get('/{vendor_id}', response=GetVendorSchema)
def get_vendor(request, vendor_id: int):
    """List a single vendor by id."""
    vendor = get_object_or_404(Vendor, id=vendor_id)

    return vendor


@router.put('/{vendor_id}')
def update_vendor(request, vendor_id: int, payload: VendorSchema):
    """Update a vendor."""
    vendor = get_object_or_404(Vendor, id=vendor_id)

    if not payload.vendor_name:
        raise ValueError(_('Enter Vendor Name'))

    if not payload.vendor_nit:
        raise ValueError(_('Enter Vendor NIT'))

    if not re.fullmatch(nit, payload.vendor_nit):
        raise ValueError(_('NIT is incomplete'))

    if not payload.contact_name:
        raise ValueError(_('Enter Vendor Contact Name'))

    if not payload.contact_phone:
        raise ValueError(_('Enter Vendor Contact Number'))

    if not re.fullmatch(phone, vendor.contact_phone):
        raise ValueError(_('Invalid Contact Number'))

    for attr, value in payload.dict().items():
        setattr(vendor, attr, value)
    vendor.save()
    return {"success": True}


@router.delete('/{vendor_id}')
def delete_vendor(request, vendor_id: int):
    """Delete a vendor."""
    vendor = get_object_or_404(Vendor, id=vendor_id)
    vendor.delete()
    return {"success": True}
