from django.contrib.auth import get_user_model, login
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from django.views import generic as views

from GymMembershipsApp.gym.forms import UserRegisterForm

UserModel = get_user_model()


class IndexView(views.TemplateView):
    template_name = 'index.html'


class UserRegisterView(views.CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)

        return response


class UserLoginView(auth_views.LoginView):
    template_name = 'login.html'


class UserLogoutView(auth_views.LogoutView):
    ...
