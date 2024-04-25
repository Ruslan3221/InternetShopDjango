from django import forms

from shop.models import Product, ProductImage
from multiupload.fields import MultiFileField

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductImageForm(forms.Form):
    images = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5)