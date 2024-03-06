from django.db import models

# Create your models here.

class Product(models.Model):
    product_image = models.ImageField(upload_to="product_images/", default = 'product_images/blank-product.png')
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name