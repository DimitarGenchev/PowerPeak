from django.contrib import admin
from GymMembershipsApp.gym.models import Membership, Category, Product, Brand, MembershipType, Trainer


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    fields = ['start_date', 'duration', 'membership_type', 'user', 'end_date']
    readonly_fields = ['start_date', 'end_date']
    list_filter = ['membership_type', 'duration', 'start_date']
    search_fields = ['user__first_name', 'user__last_name', 'user__phone_number', 'user__email']
    list_display = ['user', 'start_date', 'end_date']


@admin.register(MembershipType)
class MembershipTypeAdmin(admin.ModelAdmin):
    ordering = ['price_for_one_month']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ['name_bg', 'name_en']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    ordering = ['name_bg', 'name_en']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ['name_bg', 'name_en']


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    ...
