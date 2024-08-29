from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Category, Product, ProductCategory, User
from .forms import RegisterForm
from django.http import HttpResponse

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
    return redirect('category_view', slug='all')

def category_view(request, slug):
    if slug == 'all':
        # Wenn der Slug 'all' ist, zeige alle Produkte
        products = Product.objects.all()
        selected_category = None
    else:
        # Wenn der Slug eine gültige Kategorie ist, zeige Produkte der ausgewählten Kategorie
        category = get_object_or_404(Category, slug=slug)
        product_categories = ProductCategory.objects.filter(category=category)
        products = [pc.product for pc in product_categories]
        selected_category = category

    categories = Category.objects.all()
    return render(request, 'online_shop_app/home.html', {
        'products': products,
        'categories': categories,
        'selected_category': selected_category  # Track the selected category
    })

def redirect_to_all_categories(request):
    return redirect('category_view', slug='all')

def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'online_shop_app/product_detail.html', {'product': product})

def add_to_cart_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    quantity = int(request.POST.get('quantity', 1))
    
    # Logik zum Hinzufügen zum Warenkorb (hier nur ein Beispiel)
    # cart = request.session.get('cart', {})
    # if product.id in cart:
    #     cart[product.id] += quantity
    # else:
    #     cart[product.id] = quantity
    # request.session['cart'] = cart
    
    return redirect('product_detail', slug=slug)
