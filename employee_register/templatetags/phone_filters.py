from django import template
import phonenumbers
from phonenumbers import PhoneNumberFormat

register = template.Library()


@register.filter
def format_phone(value, country="GH"):
    try:
        parsed = phonenumbers.parse(value, country)
        return phonenumbers.format_number(parsed, PhoneNumberFormat.INTERNATIONAL)
    except Exception:
        return value  # fallback if number is invalid
