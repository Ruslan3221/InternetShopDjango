import os

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
def upload_to(instance, filename):
    # Если instance не сохранен в базе данных или не существует, возвращаем дефолтный путь
    print(f'[{instance}] - {filename}')
    if not instance or not instance.pk:
        return f"detail/image/{filename}"

    # Получаем расширение файла
    filename_base, filename_ext = os.path.splitext(filename)

    # Получаем объект ProductImage, связанный с данным товаром
    product_image = ProductImage.objects.filter(product=instance).first()

    # Определяем номер следующего изображения
    next_photo_number = 1 if not product_image else ProductImage.objects.filter(product=instance).count() + 1

    # Возвращаем путь сохранения файла
    return f"{instance.name}/{instance.name}_{next_photo_number}{filename_ext}"




class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    #image = models.ImageField(upload_to=upload_to, blank=True)
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    product_images = models.ImageField(upload_to='detail')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Cart(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)