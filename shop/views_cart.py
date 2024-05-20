from django.contrib.auth.models import User
from .decorator_permission import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Cart, CartItem, Product
#TODO:Сделать форму заполнения при кидание товара в

@auth_and_user
def add_to_cart(request, product_id):
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    product = get_object_or_404(Product, pk=product_id)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(reverse('shop:cabinet',args=[request.user.username]))

