from datetime import datetime

from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class CustomDateField(forms.DateField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        current_year = datetime.now().year
        self.widget.years = range(1950, current_year - 12)


class UserAdminRegisterForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'phone_number']

    def save(self, commit=True):
        user = super().save(commit=False)

        user.created_via_admin = True

        if commit:
            user.save()
            
        return user


class UserRegisterForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ['email', 'password1', 'password2']


class UserDetailsForm(forms.ModelForm):
    date_of_birth = CustomDateField(
        widget=forms.SelectDateWidget(),
    )

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number']
