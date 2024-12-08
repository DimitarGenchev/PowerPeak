from urllib.parse import urlparse, urlunparse

from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.template.loader import render_to_string

from django.utils.translation import gettext_lazy as _

from django.views import generic as views
from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from GymMembershipsApp.gym.forms import ProductsFilterForm
from GymMembershipsApp.gym.models import MembershipType, Trainer, Product

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


class ProductsAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'brand']

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', '')

        if search:
            language = self.request.LANGUAGE_CODE

            if language == 'bg':
                queryset = queryset.filter(name_bg__icontains=search)
            else:
                queryset = queryset.filter(name_en__icontains=search)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        rendered_products = [
            render_to_string('common/partials/product-box.html', {'product': product})
            for product in queryset
        ]

        return Response({'products': rendered_products, 'count': len(queryset)})


class ProductsView(views.FormView):
    template_name = 'products.html'
    form_class = ProductsFilterForm


def switch_language(request):
    language = request.LANGUAGE_CODE
    url = request.META.get('HTTP_REFERER')
    parsed_url = urlparse(url)

    if language == 'bg':
        new_path = f'/en{parsed_url.path}'
    else:
        new_path = parsed_url.path.replace('/en', '', 1)

    modified_url = urlunparse(parsed_url._replace(path=new_path))

    return redirect(modified_url)
