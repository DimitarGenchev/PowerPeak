from dateutil.relativedelta import relativedelta
from django.contrib.auth import models as auth_models, get_user_model
from django.db import models

from GymMembershipsApp.gym.utils import determine_membership_price


class GymUser(auth_models.AbstractUser):
    email = models.EmailField(
        unique=True,
    )

    username = None

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []


UserModel = get_user_model()


class MembershipType(models.Model):
    name = models.CharField(
        max_length=30,
    )

    display_name = models.CharField(
        max_length=30,
    )

    price_for_one_month = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )

    price_for_three_months = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    price_for_six_months = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    price_for_twelve_months = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    def __str__(self):
        return self.name


class Membership(models.Model):
    class DurationChoices(models.IntegerChoices):
        ONE_MONTH = 1, '1 month'
        THREE_MONTHS = 3, '3 months'
        SIX_MONTHS = 6, '6 months'
        TWELVE_MONTHS = 12, '12 months'

    duration = models.IntegerField(
        choices=DurationChoices.choices,
    )

    start_date = models.DateField(
        auto_now_add=True,
    )

    end_date = models.DateField(
        blank=True,
        null=True,
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
    )

    membership_type = models.ForeignKey(
        MembershipType,
        on_delete=models.SET_NULL,
        null=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        result = super().save(*args, **kwargs)

        if self.end_date is None and self.price is None:
            self.end_date = self.start_date + relativedelta(months=self.duration)
            self.price = determine_membership_price(self.duration, self.membership_type)

            self.save()

        return result


class Category(models.Model):
    name = models.CharField(
        max_length=30,
    )

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(
        max_length=30,
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
    )

    price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )

    def __str__(self):
        return f'{self.name} - {self.brand}'

