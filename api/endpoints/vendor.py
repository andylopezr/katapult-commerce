"""
Vendor schemas and routes.
"""
from django.shortcuts import get_object_or_404
from django.db.utils import IntegrityError
from ninja import Schema, Router
from ninja.pagination import paginate
from typing import List

from vendor.models import Vendor

router = Router()


class VendorSchema(Schema):
    vendor_name: str
    vendor_nit: str
    contact_name: str
    contact_phone: str


class VendorSchema(Schema):
    vendor_name: str
    vendor_nit: str
    contact_name: str
    contact_phone: str
    