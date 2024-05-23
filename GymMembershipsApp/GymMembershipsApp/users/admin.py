from django.contrib import admin
from django.contrib.auth import get_user_model

from GymMembershipsApp.users.forms import UserAdminRegisterForm

UserModel = get_user_model()


@admin.register(UserModel)
class GymUserAdmin(admin.ModelAdmin):
    form = UserAdminRegisterForm
    search_fields = ['first_name', 'last_name', 'email']
