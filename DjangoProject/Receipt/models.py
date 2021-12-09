from django.db import models
from .validators import validate_iban, validate_name, validate_amount
from enum import Enum


class Banks(Enum):
    privatbank = "pb"
    universalbank = "ub"

    @classmethod
    def items(cls):
        return [(bank.name, bank.name) for bank in cls]


class PaymentType(Enum):
    handle = 1
    card = 2
    NFC = 3

    @classmethod
    def items(cls):
        return [(payment_type.name, payment_type.name) for payment_type in cls]


class Receipt(models.Model):
    recipientName = models.CharField(max_length=30, validators=[validate_name])
    recipientIban = models.CharField(max_length=29, validators=[validate_iban])
    bank = models.CharField(max_length=30, choices=Banks.items())
    paymentType = models.CharField(max_length=10, choices=PaymentType.items())
    amount = models.FloatField(validators=[validate_amount])
    paymentDatetime = models.DateTimeField()
