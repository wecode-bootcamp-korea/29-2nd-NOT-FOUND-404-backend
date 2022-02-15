from django.db import models

from core.models import TimeStampedModel

class User(TimeStampedModel):
    name         = models.CharField(max_length=20)
    nickname     = models.CharField(max_length=20)
    email        = models.EmailField(max_length=100, unique=True)
    kakao_id     = models.IntegerField()
    password     = models.CharField(max_length=200)
    rank         = models.CharField(max_length=20)
    point        = models.IntegerField(default=100000)
    phone_number = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'users'

