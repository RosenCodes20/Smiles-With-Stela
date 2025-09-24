from django.contrib.auth import get_user_model
from django.db import models

from mother_gift.all_products.choices import ProductTypeChoices


# Create your models here.
UserModel = get_user_model()
class AllProducts(models.Model):

    product_image = models.ImageField(
        upload_to="media/"
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

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE
    )