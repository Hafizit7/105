from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('product/details/<slug>', product_details, name='product_details'),
    path('product-search', product_search,name='product_search'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-cart/<slug>/', remove_cart, name='remove_cart'),
    path('cart-summary/', cart_summary, name='cart_summary'),
    path('cart-increment/<slug>/', card_increment, name='card_increment'),
    path('cart-decrement/<slug>/', card_decrement, name='card_decrement'),
]