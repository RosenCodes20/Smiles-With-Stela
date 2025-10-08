from django.db import models

class OrderUserModelChoices(models.TextChoices):
    IN_PROGRESS = 'В процес', 'В процес'
    DELIVERED = 'Доставено', 'Доставено'