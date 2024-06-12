from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from .models import CanteenProduct

@method_decorator(login_required, name='dispatch')
class CanteenMenuView(ListView):
    model = CanteenProduct
    template_name = 'store_templates/canteen_menu.html'
    context_object_name = 'canteen_products'

    def get_queryset(self):
        return CanteenProduct.objects.filter(is_available=True)



