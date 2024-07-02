# from django.shortcuts import render,redirect
# from cart.models import Cart

# def checkout_view(request):
#     if request.user.is_authenticated:
#         cart = Cart.objects.get(user=request.user)
#         return render(request,'payment_gateway_templates/checkout.html', {'cart':cart})
#     else:
#         return redirect('users:login')
