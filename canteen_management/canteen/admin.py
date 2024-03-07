from django.contrib import admin
from .models import CanteenProduct
# Register your models here.

class CanteenProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name", "price")
    ordering = ("name",)

admin.site.register(CanteenProduct, CanteenProductAdmin)
