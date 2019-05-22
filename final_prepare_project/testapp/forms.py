from django import forms
from .models import Catalog, Shop

class CatalogForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = '__all__'


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'
        #exclude = ['catalog']