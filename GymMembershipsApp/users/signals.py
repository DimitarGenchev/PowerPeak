from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models.signals import pre_save, m2m_changed
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


@receiver(m2m_changed, sender=UserModel.groups.through)
def update_is_staff_and_is_superuser(sender, instance, action, pk_set, **kwargs):
    if action in ['post_add', 'post_remove']:
        staff_group = Group.objects.filter(name='Staff').first()
        admin_group = Group.objects.filter(name='Admin').first()

        if admin_group:
            in_admin_group = admin_group in instance.groups.all()
            instance.is_staff = in_admin_group
            instance.is_superuser = in_admin_group

        if staff_group:
            in_staff_group = staff_group in instance.groups.all()
            instance.is_staff = in_staff_group

        instance.save()
