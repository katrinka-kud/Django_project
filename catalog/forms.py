from django import forms
from django.forms import BooleanField

from catalog.models import Product, Version


class StyleFormMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа',
                       'дешево', 'бесплатно', 'обман', 'полиция', 'радар')

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'category', 'image')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        for name in self.forbidden_words:
            if name in cleaned_data:
                raise forms.ValidationError(f'В наименовании товара есть запрещенное слово "{name}"')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for description in self.forbidden_words:
            if description in cleaned_data:
                raise forms.ValidationError(f'В описании товара есть запрещенное слово "{description}"')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
