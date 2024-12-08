from datetime import date

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string


def calculate_age(date_of_birth):
    today = date.today()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

    return age


def generate_password():
    while True:
        password = get_random_string(10)

        try:
            validate_password(password)
            break
        except ValidationError:
            pass

    return password


def generate_email(user, generated_password=None):
    email = f'Hey, {user.first_name}. Welcome to PowerPeak! Thank you for registering!'

    if hasattr(user, 'created_via_admin'):
        email += f'\nYour default password is: {generated_password}'

    return email
