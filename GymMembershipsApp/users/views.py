from django.contrib.auth import login, views as auth_views, get_user_model
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from formtools.wizard.views import SessionWizardView

from GymMembershipsApp.users.forms import UserRegisterForm, UserDetailsForm, UserLoginForm, UserChangePasswordForm

UserModel = get_user_model()


class UserRegisterWizardView(SessionWizardView):
    template_name = 'register.html'
    form_list = [UserRegisterForm, UserDetailsForm]

    def done(self, form_list, **kwargs):
        form_data = {}

        for form in form_list:
            form_data.update(form.cleaned_data)

        new_user = UserModel.objects.create_user(
            email=form_data['email'],
            password=form_data['password1'],
            first_name=form_data['first_name'],
            last_name=form_data['last_name'],
            date_of_birth=form_data['date_of_birth'],
            phone_number=form_data['phone_number'],
        )

        login(self.request, new_user)

        return redirect('index')


class UserLoginView(auth_views.LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm


class UserLogoutView(auth_mixins.LoginRequiredMixin, auth_views.LogoutView):
    ...


class UserDetailsView(auth_mixins.LoginRequiredMixin, views.ListView):
    template_name = 'profile.html'

    def get_queryset(self):
        return self.request.user.membership_set.order_by('-start_date')


class ChangeUserPasswordView(auth_mixins.LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = 'change-password.html'
    form_class = UserChangePasswordForm
    success_url = reverse_lazy('details user')


class ChangeUserEmailView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'change-email.html'
    fields = ['email']
    success_url = reverse_lazy('details user')

    def get_object(self, queryset=None):
        return self.request.user
