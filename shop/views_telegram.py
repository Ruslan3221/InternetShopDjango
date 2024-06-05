from django.shortcuts import render, redirect
from .forms import TelegramidForm

from .models import Telegramid

def update_telegram_profile(request):
    telegram_profile, created = Telegramid.objects.get_or_create(user=request.user)
    profile_exists = telegram_profile.chat_id is not None

    if request.method == 'POST':
        if not profile_exists:
            form = TelegramidForm(request.POST, instance=telegram_profile)
            if form.is_valid():
                form.save()
                return redirect('shop:main')  # Замените 'profile' на имя нужного URL
        else:
            return redirect('shop:main')  # Замените 'profile' на имя нужного URL
    else:
        form = TelegramidForm(instance=telegram_profile) if not profile_exists else None

    return render(request, 'forms/update_telegram_profile.html', {
        'form': form,
        'profile_exists': profile_exists
    })
