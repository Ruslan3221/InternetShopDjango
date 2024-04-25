from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('shop:main')  # Перенаправьте пользователя на главную страницу
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('shop:main')  # Перенаправьте пользователя на главную страницу
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('shop:main')
