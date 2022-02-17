from django.db import models

from core.models import TimeStampedModel

class User(TimeStampedModel):
    name         = models.CharField(max_length=20)
    nickname     = models.CharField(max_length=20)
    kakao_id     = models.IntegerField()
    rank         = models.CharField(max_length=20)
    point        = models.IntegerField(default=100000)

    class Meta:
        db_table = 'users'

