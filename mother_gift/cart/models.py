from django.db import models
from decimal import Decimal

class Product(models.Model):
    name = models.CharField(max_length=500)
    price_in_lv = models.DecimalField(max_digits=10, decimal_places=2)
    price_in_eu = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    @property
    def sum_in_lv(self):
        return self.product.price_in_lv * Decimal(self.quantity)

    @property
    def sum_in_eu(self):
        return self.product.price_in_eu * Decimal(self.quantity)