from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView

from .bot import *


from shop.forms import ProductForm, ProductImageForm,ProductImageFormSet
from shop.models import Product,ProductImage


from .decorator_permission import *

def main(request):
    products = Product.objects.all()
    return render(request, 'main.html', {'products': products})

def detail(request, pk):
    product = Product.objects.get(pk=pk)

    product_images = ProductImage.objects.filter(product=product)

    return render(request, 'detail.html', {'product': product, 'product_images': product_images})

@admin_only
def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        image_form = ProductImageForm(request.POST, request.FILES)
        if product_form.is_valid() and image_form.is_valid():
            product = product_form.save()
            for image in request.FILES.getlist('product_images'):
                ProductImage.objects.create(product=product, product_images=image)
            return redirect('shop:main')
    else:
        product_form = ProductForm()
        image_form = ProductImageForm()
    return render(request, 'forms/addProductForm.html', {'product_form': product_form, 'image_form': image_form})



#удаление
@admin_only
def delete_product(request,product_id):
    product = Product.objects.get(pk=product_id)

    product.delete()
    return redirect("shop:main")


#TODO:Сделать редактирование изображение
@admin_only
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product_images = ProductImage.objects.all()
    print(product_images, "formset")

    print(product.name,":product")
    if request.method == 'POST':
        product_form = ProductForm(request.POST, instance=product)
        image_formset = ProductImageFormSet(request.POST, request.FILES, instance=product)
        if product_form.is_valid() and image_formset.is_valid():
            product_form.save()
            image_formset.save()

            send_message_to_user(954677875,f"Товар {product.name} обновился!")

            return redirect('shop:main')
    else:
        product_form = ProductForm(instance=product)
        image_formset = ProductImageFormSet(instance=product)

    context = {
        'product_form': product_form,
        'image_formset': image_formset,
        "name":product.name,
        "price":product.price,
    }
    return render(request, 'product_edit.html', context)

#Подписка
@auth_and_user
def subscribe_product(request,pk,username):
    product = Product.objects.get(pk=pk)
    product.subscribe(request.user)
    return redirect(reverse("shop:cabinet", args=[request.user.username]))

@auth_and_user
def unsubscribe_product(request,pk,username):
    product = Product.objects.get(pk=pk)
    product.unsubscribe(request.user)
    return redirect(reverse("shop:cabinet", args=[request.user.username]))



#Админ панель
@admin_only
def admin_panel(request):
    context = {
        "context":1
    }

    return render(request, "./adminPanel.html",context)