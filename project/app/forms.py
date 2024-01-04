from django import forms
from django.core.exceptions import ValidationError
from django_filters import FilterSet
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'description',
            'category',
            'price',
            'quantity',
        ]

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("description")
        if description is not None and len(description) < 20:
            raise ValidationError({
                "description": "Описание не может быть менее 20 символов."
            })
        product_name = cleaned_data.get("product_name")
        if product_name == description:
            raise ValidationError(
                "Описание не должно быть идентичным названию."
            )

        return cleaned_data

