from django.urls import path
from .views import CanteenMenuView


urlpatterns = [
    path('menu/', CanteenMenuView.as_view(), name='canteen_menu'),
]