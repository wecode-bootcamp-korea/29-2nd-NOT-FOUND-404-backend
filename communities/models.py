from django.db import models

from core.models import TimeStampedModel
from products.models import Product, ProductObject
from reviews.models import Review
from users.models import User


class Community(TimeStampedModel):
    user          = models.ForeignKey(User, on_delete=models.CASCADE),
    product       = models.ForeignKey(Product, on_delete=models.CASCADE),
    parent_review = models.ForeignKey('self', on_delete=models.CASCADE),
    content       = models.CharField(max_length=200),

    class Meta:
        db_table = 'communities'

class Media(models.Model):
    storage_path = models.URLField()

    class Meta:
        db_table = 'media'

class CommunityMedia(models.Model):
    media     = models.ForeignKey(Media, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)

    class Meta:
        db_table = 'communities_media'

class ProductObjectMedia(models.Model):
    media          = models.ForeignKey(Media, on_delete=models.CASCADE)
    product_object = models.ForeignKey(ProductObject, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_objectives_media'

class ProductMedia(models.Model):
    media   = models.ForeignKey(Media, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_media'

class UserMedia(models.Model):
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    user  = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'users_media'

class ReviewMedia(models.Model):
    media  = models.ForeignKey(Media, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviews_media'