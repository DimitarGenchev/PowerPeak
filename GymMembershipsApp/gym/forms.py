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

    category = forms.ChoiceField(
        choices=[('', 'Category')] + [(cat.id, cat.name) for cat in Category.objects.all()],
        widget=forms.Select(
            attrs={
                'id': 'product-category-input',
            },
        ),
        required=False,
    )

    brand = forms.ChoiceField(
        choices=[('', 'Brand')] + [(brand.id, brand.name) for brand in Brand.objects.all()],
        widget=forms.Select(
            attrs={
                'id': 'product-brand-input',
            },
        ),
        required=False,
    )
