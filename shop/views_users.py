from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView
from shop.models import User
from .decorator_permission import *


@admin_only
def users(request):
    users = User.objects.all()
    useri = []
    you = request.user.username
    print(you,"-----you-------")

    id = 0

    for user in users:
        id +=1
        userr = {
            "id":id,
            "name":str(user),
            "personal": user.is_superuser
        }

        useri.append(userr)



    context = {
        "all":useri,
        "you": you

    }

    print(f"{context}------")

    return render(request, './users.html', context)