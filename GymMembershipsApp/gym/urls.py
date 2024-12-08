from django.urls import path

from GymMembershipsApp.gym import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('prices/', views.PricesView.as_view(), name='prices'),
    path('products/', views.ProductsView.as_view(), name='products'),
    path('api/products/', views.ProductsAPIView.as_view(), name='products api'),
    path('switch_language/', views.switch_language, name='switch language')
]
