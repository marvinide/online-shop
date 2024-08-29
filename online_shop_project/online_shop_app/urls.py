from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_all_categories, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('category/<slug:slug>/', views.category_view, name='category_view'),
    path('remove_category/', views.home_view, name='remove_category'),
]
