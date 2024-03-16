from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


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
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number']
