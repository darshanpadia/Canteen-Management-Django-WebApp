from django.shortcuts import render, redirect
from canteen.models import CanteenProduct
from .models import Cart, CartItem


def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        product = CanteenProduct.objects.get(id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user) #atttempts to fetch a cart object associated with requested user if it exists(sets creaeted = False), if not creates the object and assigns created= True
        cart_item, created = CartItem.objects.get_or_create(cart=cart, canteen_product=product) #get_or_create(querry=object)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
    return redirect('cart_view')

def remove_from_cart(request,cart_item_id):
    if request.user.is_authenticated:
        CartItem.objects.filter(id=cart_item_id).delete()
    return redirect('cart_view')

def cart_view(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        return render(request, 'cart_templates/cart.html', {'cart' : cart})
    else:
        return redirect('users:login')