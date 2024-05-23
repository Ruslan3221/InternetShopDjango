from django import forms

from shop.models import Product, ProductImage,User
from multiupload.fields import MultiFileField


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductImageForm(forms.Form):
    #images = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5)
    class Meta:
        model = ProductImage
        fields = ['product_images']


class SignUpFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username.lower()