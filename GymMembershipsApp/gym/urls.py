from django.urls import path

from GymMembershipsApp.gym import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]
