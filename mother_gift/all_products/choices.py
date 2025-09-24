from django.db import models

class ProductTypeChoices(models.TextChoices):
    SOAPS = "Сапуни", "Сапуни"
    DECORATIONS = "Украси", "Украси"
    GIFT_SETS = "Подаръчни комплекти", "Подаръчни комплекти"