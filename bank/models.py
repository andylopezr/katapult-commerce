"""
Bank and BankAccount models.
"""
from django.db import models
from vendor.models import Vendor


class Bank(models.Model):
    """Bank model"""
    BANK_L = [
        ('AVV', 'AV Villas'),
        ('BDB', 'Banco de Bogota'),
        ('BCO', 'Bancolombia'),
        ('BBV', 'BBVA'),
        ('BDO', 'Banco de Occidente'),
        ('BDO', 'Davivienda'),
        ('CSO', 'Caja Social'),
        ('ITA', 'Itaú'),
        ('SCO', 'Scotiabank'),
        ('POP', 'Popular'),
    ]

    bank_name = models.CharField(max_length=50, choices=BANK_L, default="AVV")

    def __str__(self):
        return self.bank_name


class BankAccount(models.Model):
    account_number = models.CharField(max_length=255, blank=False)
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return self.account_number
