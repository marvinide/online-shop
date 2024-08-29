from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('category/<slug:slug>/', views.category_view, name='category_view'),
    path('product/<slug:slug>/', views.product_detail_view, name='product_detail'),
    path('add_to_cart/<slug:slug>/', views.add_to_cart_view, name='add_to_cart'),
    path('remove_category/', views.home_view, name='remove_category'),
]
