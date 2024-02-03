from django.contrib import admin

from GymMembershipsApp.gym.models import Membership


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    fields = ['duration', 'membership_type', 'user', 'end_date']
    readonly_fields = ['end_date']
