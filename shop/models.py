import decimal
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

    def __str__(self):
        return self.name

    def subscribe(self,user):
        Subscriber.objects.get_or_create(user=user,product=self)


    def unsubscribe(self,user):
        Subscriber.objects.filter(user=user,product=self).delete()

    def notify(self):
        subscribers = Subscriber.objects.filter(user=self)

        for sub in subscribers:
            Message.objects.create(title="!!!",text="Обновление!",user=sub.user)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    product_images = models.ImageField(upload_to='detail')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

#model for podpisoti
class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('user', 'product'),)


class Cart(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def create_order(self):
        order = Order.objects.create(user=self.user, total_price= 0.00)
        total_price = decimal.Decimal(0.00)
        for item in self.items.all():
            order_item = OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
            print("сдесь ошибка create_order",type(order_item.quantity),type(order_item.price))

            price = decimal.Decimal(order_item.price)
            quantity = decimal.Decimal(order_item.quantity)

            print(type(total_price))

            total_price += price*quantity

        order.total_price = total_price
        order.save()
        self.items.all().delete()
        return order


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Order(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)

    def __str__(self):
        return f' Заказ-{self.id}.От {self.user}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity}-{self.product.name}"




class Message(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
