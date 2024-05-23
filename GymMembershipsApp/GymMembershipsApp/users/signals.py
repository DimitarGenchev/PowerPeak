from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail

from GymMembershipsApp.users.utils import generate_email, generate_password

UserModel = get_user_model()


@receiver(pre_save, sender=UserModel)
def pre_create_user(sender, instance, **kwargs):
    if instance._state.adding:
        if hasattr(instance, 'created_via_admin'):
            password = generate_password()
            email = generate_email(instance, password)

            instance.set_password(password)
        else:
            email = generate_email(instance)

        send_mail(
            'Welcome to PowerPeak',
            email,
            settings.EMAIL_HOST_USER,
            [instance.email],
            fail_silently=False,
        )
