from django import forms

from shop.models import Product, ProductImage,User,Telegramid
from multiupload.fields import MultiFileField


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductImageForm(forms.ModelForm):
    #images = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5)
    class Meta:
        model = ProductImage
        fields = ['product_images']



ProductImageFormSet = forms.inlineformset_factory(
    Product,
    ProductImage,
    form=ProductImageForm,
    extra=1,
    can_delete=True,
    max_num=10,
)


class TelegramidForm(forms.ModelForm):
    class Meta:
        model = Telegramid
        fields = ['chat_id']


class SignUpFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username.lower()

