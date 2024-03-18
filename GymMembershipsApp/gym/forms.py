from django import forms

from GymMembershipsApp.gym.models import Category, Brand


class ProductsFilterForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'search-input',
                'placeholder': 'Search products...',
            },
        ),
        required=False,
    )

    product_category = forms.ChoiceField(
        choices=[('', 'Category')] + [(cat.id, cat.name) for cat in Category.objects.all()],
        widget=forms.Select(
            attrs={
                'id': 'product-types-input',
                'name': 'search-by-product-type',
            },
        ),
        required=False,
    )

    product_brand = forms.ChoiceField(
        choices=[('', 'Brand')] + [(brand.id, brand.name) for brand in Brand.objects.all()],
        widget=forms.Select(
            attrs={
                'id': 'product-brands-input',
                'name': 'search-by-product-brand',
            },
        ),
        required=False,
    )
