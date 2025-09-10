from django.db import models

class ProductTypeChoices(models.TextChoices):
    SOAPS = "Сапуни", "Soaps"
    DECORATIONS = "Украси", "Decorations"
    GIFT_SETS = "Подаръчни комплекти", "Gift sets"