from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

@method_decorator(login_required, name='dispatch')
class CanteenMenuView(ListView):
    model = Product
    template_name = 'store_templates/canteen_menu.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(is_available=True)



