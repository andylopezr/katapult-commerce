"""
Vendor model.
"""
from django.db import models


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=255, blank=False)
    vendor_nit = models.CharField(max_length=11, unique=True)
    contact_name = models.CharField(max_length=200, blank=False)
    contat_phone = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return self.vendor_name
