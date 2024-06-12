from django.db import models 
from users.models import CustomUser
from canteen.models import CanteenProduct

# Create your models here.


class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    canteen_product = models.ForeignKey(CanteenProduct, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.PositiveIntegerField(default=0)
