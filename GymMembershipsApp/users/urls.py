from django.urls import path

from GymMembershipsApp.users import views

urlpatterns = [
    path('register/', views.UserRegisterWizardView.as_view(), name='register user'),
    path('login/', views.UserLoginView.as_view(), name='login user'),
    path('logout/', views.UserLogoutView.as_view(), name='logout user'),
]