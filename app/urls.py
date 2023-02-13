from django.urls import path 
from . import views 
 
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('contact/', views.contact, name="contact"),
    path('cart/', views.cart, name="cart"),
    path('news/', views.news, name="news"),
    path('shop/', views.shop, name="shop"),
    path('books/', views.books, name="books"),
    path('stationary/', views.stationary, name="stationary"),
    path('single-product/', views.single_product, name="single_product"),
]
