from django import forms
from django.utils.translation import gettext_lazy as _, get_language

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
        widget=forms.Select(
            attrs={
                'id': 'product-category-input',
            },
        ),
        required=False,
    )

    brand = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'id': 'product-brand-input',
            },
        ),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        current_language = get_language()

        if current_language == 'bg':
            self.fields['category'].choices = [('', _('Категория'))] + [(cat.id, cat.name_bg) for cat in Category.objects.all()]
            self.fields['brand'].choices = [('', _('Марка'))] + [(brand.id, brand.name_bg) for brand in Brand.objects.all()]
        else:
            self.fields['category'].choices = [('', _('Категория'))] + [(cat.id, cat.name_en) for cat in Category.objects.all()]
            self.fields['brand'].choices = [('', _('Марка'))] + [(brand.id, brand.name_en) for brand in Brand.objects.all()]
