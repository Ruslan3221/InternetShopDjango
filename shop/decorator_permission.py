from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse


#Декоратор для ограничения доступа ТОЛЬКО ДЛЯ ТЕХ У КОГО ЕСТЬ АККАУНТ
def auth_and_user(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("shop:login")
        url_username = kwargs.get('username')

        if url_username != request.user.username:
            return redirect("shop:main")
        return view_func(request, *args, **kwargs)
    return wrapper


def auth_and_user2(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("shop:login")
        url_username = kwargs.get('username')
        if url_username != request.user.username:
            print("This(-_-)")
            print(url_username)
            return redirect("shop:main")
        return view_func(request, *args, **kwargs)
    return wrapper


#Только для админов
def admin_only(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect("shop:main")
        return view_func(request, *args, **kwargs)
    return wrapper
