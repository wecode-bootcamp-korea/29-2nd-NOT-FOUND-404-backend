from django.db  import models

from core.models    import TimeStampedModel
from products.models import Product
from users.models   import User

class Review(TimeStampedModel):
    product       = models.ForeignKey(Product, on_delete=models.CASCADE)
    user          = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_review        = models.ForeignKey('self', on_delete=models.CASCADE)
    content       = models.CharField(max_length=500)
    ratings       = models.IntegerField()

    class Meta:
        db_table = 'reviews'

class ReviewLike(models.Model):
    user   = models.ForeignKey(User, on_delete=models.CASCADE)
    reivew = models.ForeignKey(Review, on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviews_likes'