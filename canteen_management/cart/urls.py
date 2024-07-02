from django.urls import path
from .views import add_to_cart, remove_from_cart, increase_cart_item_quantity, decrease_cart_item_quantity, cart_view, checkout_view

urlpatterns = [
    path('', cart_view, name='cart_view'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_item_id>', remove_from_cart, name='remove_from_cart'),
    path('increase/<int:cart_item_id>/', increase_cart_item_quantity, name='increase_quantity'),
    path('decrease/<int:cart_item_id>/', decrease_cart_item_quantity, name='decrease_quantity'),
    path('checkout', checkout_view, name='checkout_view')
]