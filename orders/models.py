from django.db import models

from core.models import TimeStampedModel
from users.models import User
from products.models import Product

class Order(TimeStampedModel):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'

