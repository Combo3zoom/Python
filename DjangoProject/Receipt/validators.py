from django.core.exceptions import ValidationError
import re


def validate_name(value):
    if not re.fullmatch(r'[A-Z][a-z]{2,30}', value):
        raise ValidationError("Incorrect name")


def validate_iban(value):
    if not re.fullmatch(r"^[A-Z]{2}[0-9]{8}[0]{5}[0-9]{14}$", value):
        raise ValidationError("Incorrect IBAN format")


def validate_amount(value):
    if value < 0:
        raise ValidationError("Incorrect amount")

