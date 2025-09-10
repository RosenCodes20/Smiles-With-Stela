from django.db import models

from mother_gift.all_products.choices import ProductTypeChoices


# Create your models here.

class AllProducts(models.Model):

    image = models.ImageField()

    product_description = models.CharField(
        max_length=200,
    )

    product_type = models.CharField(
        choices=ProductTypeChoices.choices
    )