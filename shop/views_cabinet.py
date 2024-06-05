from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .decorator_permission import *
from django.http import JsonResponse
from .models import Cart, CartItem, Product,Message,Subscriber,Order,OrderItem,Telegramid
import logging

logger = logging.getLogger(__name__)


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

    def views_sub(self):
        subscribe = Subscriber.objects.filter(user=self.user)
        return subscribe


    def message(self):
        self.message = Message.objects.all().filter(user=self.user)
        return self.message


    #Метод запуска
    def cabinet_start(self):
        products_in_cart = self.cart_items()

        message = self.message()

        subscribe = self.views_sub()

        self.context = {
            'products_in_cart': products_in_cart,
            'user': self.user,
            'message': message,
            'cart': self.cart,
            'subscribe':subscribe
        }

        return render(self.request, 'cabinet.html', self.context)

    #Удаление из корзины
    def delete_from_cart(self, request, cart_id):
        self.cart = get_object_or_404(CartItem, pk=cart_id)
        self.cart.delete()
        return redirect(reverse("shop:cabinet", args=[self.username]))

    def create_Order(self, username):
        logger.debug(f"Creating order for username: {username}")
        print("ok")
        user = get_object_or_404(User, username=username)
        cart = get_object_or_404(Cart, user=user)
        cart.create_order()
        return redirect(reverse("shop:cabinet", args=[username]))

    def get_all_chat_id(self):
        chat = Telegramid.objects.all()

        listt = [{'chat': obj.chat_id} for obj in chat]

        return JsonResponse(listt, safe=False)



@auth_and_user
def cabinet_views(request, username):
    cabinet_class = Cabinet(request, username)
    return cabinet_class.cabinet_start()


#Удаляет из корзины
@auth_and_user
def delete_from_cabinet_cart(request, username, cart_id):
    cabinet_class = Cabinet(request, username)
    return cabinet_class.delete_from_cart(request, cart_id)

@auth_and_user
def create_order_card(request,username):
    print("Create_order_card")
    cabinet = Cabinet(request,username)
    return cabinet.create_Order(username)


def all_chat(request,username):
    cabinet = Cabinet(request,username)
    return cabinet.get_all_chat_id()


