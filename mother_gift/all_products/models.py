from django.contrib.auth import get_user_model
from django.db import models

from mother_gift.all_products.choices import ProductTypeChoices


# Create your models here.
UserModel = get_user_model()
class AllProducts(models.Model):

    product_image = models.ImageField(
        upload_to=""
    )

    second_product_image = models.ImageField(
        upload_to='',
        null=True,
        blank=True
    )

    product_description = models.CharField(
        max_length=200,
    )

    product_type = models.CharField(
        choices=ProductTypeChoices.choices
    )

    product_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    is_available = models.BooleanField(
        default=True
    )

    first_long_description = models.TextField()

    second_long_description = models.TextField()

    applicable_for = models.TextField()

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE
    )

class StarRating(models.Model):
    person_opinion = models.CharField(
        max_length=150,
        null=False,
        blank=False,
    )
