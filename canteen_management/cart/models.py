from django.db import models 
from users.models import CustomUser
from canteen.models import CanteenProduct

# Create your models here.


class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def get_total(self):
        return sum(item.item_total for item in self.cartitem_set.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    canteen_product = models.ForeignKey(CanteenProduct, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.item_total = self.quantity * self.canteen_product.price
        super().save(*args,**kwargs)
