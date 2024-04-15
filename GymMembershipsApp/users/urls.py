from django.urls import path

from GymMembershipsApp.users import views

urlpatterns = [
    path('register/', views.UserRegisterWizardView.as_view(), name='register user'),
    path('login/', views.UserLoginView.as_view(), name='login user'),
    path('logout/', views.UserLogoutView.as_view(), name='logout user'),
    path('profile/', views.UserDetailsView.as_view(), name='details user'),
    path('change-password/', views.ChangeUserPasswordView.as_view(), name='change password user'),
    path('change-email/', views.ChangeUserEmailView.as_view(), name='change user email'),
]
