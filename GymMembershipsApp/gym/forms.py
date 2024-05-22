from django import forms
from django.utils.translation import gettext_lazy as _

from GymMembershipsApp.gym.models import Category, Brand


class ProductsFilterForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'search-input',
                'placeholder': _('Търсете продукти...'),
            },
        ),
        required=False,
    )

    category = forms.ChoiceField(
        choices=[('', _('Категория'))] + [(cat.id, cat.name) for cat in Category.objects.all()],
        widget=forms.Select(
            attrs={
                'id': 'product-category-input',
            },
        ),
        required=False,
    )

    brand = forms.ChoiceField(
        choices=[('', _('Марка'))] + [(brand.id, brand.name) for brand in Brand.objects.all()],
        widget=forms.Select(
            attrs={
                'id': 'product-brand-input',
            },
        ),
        required=False,
    )
