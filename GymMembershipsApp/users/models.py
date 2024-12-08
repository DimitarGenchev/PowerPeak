from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from django.contrib.auth import models as auth_models
from django.utils.translation import gettext_lazy as _

from GymMembershipsApp.users import managers
from GymMembershipsApp.users.utils import calculate_age
from GymMembershipsApp.users.validators import validate_age_12_and_above, validate_name_contains_alphabet_only


class GymUser(auth_models.AbstractUser):
    email = models.EmailField(
        unique=True,
    )

    first_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            validate_name_contains_alphabet_only,
        ],
    )

    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            validate_name_contains_alphabet_only,
        ],
    )

    phone_number = models.CharField(
        max_length=13,
        validators=[
            RegexValidator(
                regex=r'^(?:\+359|0)\d{9}$',
                message=_('Телефонният номер трябва да започва с +359 или 0, последвано от 9 цифри.')
            ),
        ]
    )

    date_of_birth = models.DateField(
        validators=[
            validate_age_12_and_above,
        ]
    )

    username = None

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = managers.GymUserManager()

    @property
    def age(self):
        return calculate_age(self.date_of_birth)

    def __str__(self):
        return f'{self.get_full_name()} - {self.email}'
