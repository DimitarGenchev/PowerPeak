from django.contrib.auth import get_user_model
from django.contrib.auth import backends as auth_backends

UserModel = get_user_model()


class EmailBackend(auth_backends.ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user

        return None
