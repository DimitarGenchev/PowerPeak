from django.contrib import admin
from GymMembershipsApp.gym.models import Membership, Category, Product, Brand, MembershipType, Trainer


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


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    ...
