from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .decorator_permission import *
from .models import Cart, CartItem, Product


#Корзина и кабинет
class Cabinet:
    def __init__(self, request,username):
        self.username = username
        self.request = request
        self.user = User.objects.get(username=self.username)
        self.cart = get_object_or_404(Cart, user=self.user)
        self.context = {}
        self.products_in_cart = []

    #вид корзины
    def cart_items(self):
        print(f"cart_items === {self.cart.items.all()} = {self.cart}")
        for item in self.cart.items.all():

            self.count_products = len(self.products_in_cart)+1

            self.product = item.product

            self.quantity = item.quantity

            self.price = item.product.price

            self.total_price = int(self.price) * int(self.quantity)

            self.first_image = self.product.images.first()

            self.image_first_url = self.first_image.product_images.url if self.first_image else ""


            product_context = {
                'id_cart': item.id,
                'name': self.product.name,
                'price': self.price,
                'quantity': self.quantity,
                'image': self.first_image,
                'total_price': self.total_price,
                'number': self.count_products,
            }

            self.products_in_cart.append(product_context)
        return self.products_in_cart

    def cabinet_start(self):
        products_in_cart = self.cart_items()

        self.context = {
            'products_in_cart': products_in_cart,
            'user': self.user,
            'cart': self.cart,
        }

        print(f"{self.context['products_in_cart']}===")
        return render(self.request, 'cabinet.html', self.context)

    #Удаление из корзины
    def delete_from_cart(self, request, cart_id):
        #request = self.request
        self.cart = get_object_or_404(CartItem, pk=cart_id)
        self.cart.delete()
        return redirect(reverse("shop:cabinet", args=[self.username]))



@auth_and_user
def cabinet_views(request, username):
    #global cabinet_class

    cabinet_class = Cabinet(request, username)
    return cabinet_class.cabinet_start()


#Удаляет из корзины
@auth_and_user
def delete_from_cabinet_cart(request, username, cart_id):
    print(f"==={cart_id}===")

    cabinet_class = Cabinet(request, username)
    return cabinet_class.delete_from_cart(request, cart_id)

