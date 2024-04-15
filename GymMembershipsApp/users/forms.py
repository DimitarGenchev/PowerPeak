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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'


class UserDetailsForm(forms.ModelForm):
    date_of_birth = CustomDateField(
        widget=forms.SelectDateWidget(),
    )

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone number'


class UserLoginForm(auth_forms.AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'autofocus': True,
                'placeholder': 'Email',
                'name': 'email',
            }
        ),
    )

    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'placeholder': 'Password',
            },
        ),
    )


class UserChangePasswordForm(auth_forms.PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs['placeholder'] = 'Old password'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New password'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm new password'
