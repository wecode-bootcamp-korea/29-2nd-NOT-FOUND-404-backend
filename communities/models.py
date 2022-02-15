from django.db import models

from users.models import User
from products.models import Product
from core.models import TimeStampedModel

class Community(TimeStampedModel):
    user      = models.ForeignKey(User, on_delete=models.CASCADE),
    product   = models.ForeignKey(Product, on_delete=models.CASCADE),
    parent_review = models.ForeignKey('self', on_delete=models.CASCADE),
    content   = models.CharField(max_length=200),

    class Meta:
        db_table = 'communities'

