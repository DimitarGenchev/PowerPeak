from django.contrib.auth import get_user_model

from django.views import generic as views

from GymMembershipsApp.gym.models import MembershipType, Trainer

UserModel = get_user_model()


class IndexView(views.ListView):
    template_name = 'index.html'
    model = MembershipType


class AboutView(views.ListView):
    template_name = 'about.html'
    model = Trainer


class PricesView(views.ListView):
    template_name = 'prices.html'
    model = MembershipType
