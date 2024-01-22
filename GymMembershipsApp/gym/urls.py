from django.urls import path

from GymMembershipsApp.gym import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.UserRegisterView.as_view(), name='register user'),
    path('login/', views.UserLoginView.as_view(), name='login user'),
    path('logout/', views.UserLogoutView.as_view(), name='logout user'),
]
