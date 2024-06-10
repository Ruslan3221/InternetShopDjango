from .decorator_permission import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import TelegramidForm

from .models import Telegramid


def edit_you_chatId(request,username):
    chatId = get_object_or_404(Telegramid, user__username=username)

    if request.method == "POST":
        form = TelegramidForm(request.POST,instance=chatId)
        if form.is_valid():
            form.save()
            return redirect("shop:main")

    else:
        form = TelegramidForm(instance=chatId)

    context = {
        'form':form,
        'id': chatId.chat_id
    }
    return render(request,"forms/edit_chatId.html",context)


