from urllib.parse import urlparse, urlunparse

from django.contrib.auth import get_user_model
from django.shortcuts import redirect

from django.utils.translation import gettext_lazy as _

from django.views import generic as views

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


class ProductsView(views.ListView):
    template_name = 'products.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        filter_form = ProductsFilterForm()
        context['form'] = filter_form

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        search = self.request.GET.get('search')
        product_category = self.request.GET.get('category')
        product_brand = self.request.GET.get('brand')

        if search != '' and search is not None:
            queryset = queryset.filter(name__icontains=search)

        if product_category != '' and product_category is not None:
            queryset = queryset.filter(category_id=product_category)

        if product_brand != '' and product_brand is not None:
            queryset = queryset.filter(brand_id=product_brand)

        return queryset


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
