from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from GymMembershipsApp.users.forms import UserAdminRegisterForm

UserModel = get_user_model()


@admin.register(UserModel)
class GymUserAdmin(admin.ModelAdmin):
    form = UserAdminRegisterForm
    search_fields = ['first_name', 'last_name', 'email', 'phone_number']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        if request.user.is_superuser:
            form.base_fields['groups'] = forms.ModelMultipleChoiceField(
                queryset=Group.objects.all(),
                required=False,
                widget=forms.CheckboxSelectMultiple,
                label="Groups",
            )

        return form
