from django.contrib.auth import get_user_model
from django.db import models
from decimal import Decimal

from mother_gift.all_products.models import AllProducts

UserModel = get_user_model()

class Cart(models.Model):
    product_image_cart = models.ImageField(
        upload_to=""
    )

    product_description_cart = models.CharField(
        max_length=200,
    )

    product_price_cart = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    user_cart = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE
    )

class Addresses(models.Model):
    town_name = models.CharField(
        max_length=100
    )

    speedy_address = models.CharField(
        max_length=200
    )