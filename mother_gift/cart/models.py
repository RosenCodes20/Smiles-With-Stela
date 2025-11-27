from django.contrib.auth import get_user_model
from django.db import models
from decimal import Decimal

from mother_gift.cart.choices import OrderUserModelChoices

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
    first_name = models.CharField(
        max_length=150
    )

    last_name = models.CharField(
        max_length=150
    )

    address_email = models.EmailField()

    town_name = models.CharField(
        max_length=100
    )

    speedy_address = models.CharField(
        max_length=200
    )

    user_finish_cart = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE
    )

class OrderUserModel(models.Model):
    product_description_order_user = models.CharField(
        max_length=300
    )

    date = models.DateField()

    status = models.CharField(
        max_length=100,
        choices=OrderUserModelChoices.choices
    )

    user_order = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE
    )