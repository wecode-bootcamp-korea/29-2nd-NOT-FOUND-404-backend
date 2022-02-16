from django.db import models

from creators.models import Creator
from users.models import User
from core.models import TimeStampedModel

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'categories'

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name     = models.CharField(max_length=200)

    class Meta:
        db_table = 'subcategories'

class ProductStatus(models.Model):
    status = models.CharField(max_length=50)

    class Meta:
        db_table = 'product_status'

class Product(TimeStampedModel):
    title          = models.CharField(max_length=200)
    subcategory    = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    creator        = models.ForeignKey(Creator, on_delete=models.CASCADE)
    price          = models.PositiveIntegerField()
    description    = models.URLField()
    level          = models.IntegerField()
    duration       = models.IntegerField()
    subtitle       = models.CharField(max_length=200)
    available      = models.BooleanField(default=False)

    class Meta:
        db_table = 'products'

class Curriculum(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)


    class Meta:
        db_table = 'curriculums'

class ProductObject(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title   = models.CharField(max_length=200)
    content = models.CharField(max_length=500)

    class Meta:
        db_table = 'products_objectives'

class ProductLike(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_likes'