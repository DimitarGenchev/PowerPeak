from datetime import datetime

from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.utils.translation import gettext_lazy as _, pgettext

UserModel = get_user_model()


class CustomDateField(forms.DateField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        min_year = datetime.now().year - 12
        self.widget.years = range(1950, min_year + 1)
        self.initial = datetime(2000, 1, 1)


class UserAdminRegisterForm(forms.ModelForm):
    date_of_birth = CustomDateField(
        widget=forms.SelectDateWidget(),
    )

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

        self.fields['email'].widget.attrs['placeholder'] = _('Имейл')
        self.fields['password1'].widget.attrs['placeholder'] = _('Парола')
        self.fields['password2'].widget.attrs['placeholder'] = _('Потвърдете парола')


class UserDetailsForm(forms.ModelForm):
    date_of_birth = CustomDateField(
        widget=forms.SelectDateWidget(),
        label=_('Дата на раждане'),
    )

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['placeholder'] = pgettext('forms', 'Име')
        self.fields['last_name'].widget.attrs['placeholder'] = _('Фамилия')
        self.fields['phone_number'].widget.attrs['placeholder'] = _('Телефон')


class UserLoginForm(auth_forms.AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'autofocus': True,
                'placeholder': _('Имейл'),
                'name': 'email',
            }
        ),
    )

    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'placeholder': _('Парола'),
            },
        ),
    )


class UserChangePasswordForm(auth_forms.PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs['placeholder'] = _('Стара парола')
        self.fields['new_password1'].widget.attrs['placeholder'] = _('Нова парола')
        self.fields['new_password2'].widget.attrs['placeholder'] = _('Потвърдете нова парола')
