from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from GymMembershipsApp.gym.models import Membership, Category, Product, Brand, MembershipType, GymUser


@admin.register(GymUser)
class GymUserAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'email']


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    fields = ['duration', 'membership_type', 'user', 'end_date']
    readonly_fields = ['end_date']


@admin.register(MembershipType)
class MembershipTypeAdmin(admin.ModelAdmin):
    ...


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    ...


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...
