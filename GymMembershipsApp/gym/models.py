from datetime import timedelta

from django.contrib.auth import models as auth_models, get_user_model
from django.db import models


class GymUser(auth_models.AbstractUser):
    email = models.EmailField(
        unique=True,
    )

    username = None

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []


UserModel = get_user_model()


class Membership(models.Model):
    class MembershipTypeChoices(models.TextChoices):
        SCHOOL_STUDENT = 'school', 'School Student'
        UNIVERSITY_STUDENT = 'university', 'University Student'
        ADULT = 'adult', 'Adult'

        @classmethod
        def max_length(cls):
            return max(len(choice.value) for choice in cls)

    class DurationChoices(models.IntegerChoices):
        ONE_MONTH = 1, "1 month"
        THREE_MONTHS = 3, "3 months"
        SIX_MONTHS = 6, "6 months"
        TWELVE_MONTHS = 12, "12 months"

    duration = models.IntegerField(
        choices=DurationChoices.choices,
    )

    start_date = models.DateField(
        auto_now_add=True,
    )

    end_date = models.DateField(
    )

    membership_type = models.CharField(
        max_length=MembershipTypeChoices.max_length(),
        choices=MembershipTypeChoices.choices,
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        self.end_date = self.start_date + timedelta(days=self.duration*30)
        self.price = 50 * self.duration

        return super().save(*args, **kwargs)


