from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class UserRegisterForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = [
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
        ]
