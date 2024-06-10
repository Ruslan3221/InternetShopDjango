from django.contrib.auth.models import User
from .decorator_permission import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Cart, CartItem, Product, Order
#TODO:Сделать форму заполнения при кидание товара в корзину

@auth_and_user
def add_to_cart(request, username, product_id):
    print("add_to_cart---")
    user = request.user

    cart, created = Cart.objects.get_or_create(user=user)
    product = get_object_or_404(Product, pk=product_id)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(reverse('shop:cabinet',args=[request.user.username]))


@admin_only
def order(request):
    order = Order.objects.all()

    context = {
        'order': order
    }
    return render(request, 'order.html', context)

@admin_only

def order_detail(request,pk_order):
    order_det = get_object_or_404(Order,pk=pk_order)

    return render(request,'order_detail.html',{"order_det":order_det})


@admin_only
def order_delete(request,pk_order):
    order = get_object_or_404(Order,pk=pk_order)
    order.delete()
    return redirect('shop:order')

def secsseful(request):
    context = {
        '1':1
    }
    return render(request,'secsseful.html',context)
