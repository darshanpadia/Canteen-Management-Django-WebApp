
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

class CanteenMenuView(ListView):
    model = Product
    template_name = 'store_templates/canteen_menu.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(is_available=True)



