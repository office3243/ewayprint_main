from django.core.exceptions import ValidationError


def phone_number_validator(value):
    if not (value[:4] == '+91 ' and value[4:].isdigit()):
        raise ValidationError('Phone number not valid')
