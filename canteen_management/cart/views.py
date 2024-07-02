from django.shortcuts import render, redirect, get_object_or_404
from canteen.models import CanteenProduct
from .models import Cart, CartItem



def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        product = CanteenProduct.objects.get(id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user) #atttempts to fetch a cart object associated with requested user if it exists(sets creaeted = False), if not creates the object and assigns created= True
        cart_item, created = CartItem.objects.get_or_create(cart=cart, canteen_product=product) #get_or_create(querry=object)
        cart_item.item_total = cart_item.quantity * cart_item.canteen_product.price
        cart_item.save()
        if not created:
            cart_item.quantity += 1
            cart_item.item_total = cart_item.quantity * cart_item.canteen_product.price
            cart_item.save()
    return redirect('cart_view')

def remove_from_cart(request,cart_item_id):
    if request.user.is_authenticated:
        CartItem.objects.filter(id=cart_item_id).delete()
    return redirect('cart_view')


def increase_cart_item_quantity(request, cart_item_id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(CartItem, id=cart_item_id)
        cart_item.quantity += 1
        cart_item.item_total = cart_item.quantity * cart_item.canteen_product.price
        cart_item.save()
    return redirect('cart_view')

def decrease_cart_item_quantity(request, cart_item_id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(CartItem, id=cart_item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.item_total = cart_item.quantity * cart_item.canteen_product.price
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart_view')


def cart_view(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        return render(request, 'cart_templates/cart.html', {'cart' : cart})
    else:
        return redirect('users:login')
    

def checkout_view(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)
        return render(request,'payment_gateway_templates/checkout.html', {'cart':cart})
    else:
        return redirect('users:login')

