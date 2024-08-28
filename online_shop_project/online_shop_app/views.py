# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import RegisterForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            name = form.cleaned_data.get("name")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(email=email, name=name, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    error_message = None
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error_message = "Invalid email or password!"
    return render(request, 'accounts/login.html', {'error': error_message})

@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
    
    return render(request, 'accounts/logout.html')
    
def home_view(request):
    return render(request, 'online_shop_app/home.html')
