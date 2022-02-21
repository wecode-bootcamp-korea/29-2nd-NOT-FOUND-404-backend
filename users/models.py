from enum import Enum

from django.db import models

from core.models import TimeStampedModel

class UserRankEnum(Enum):
    AMATEUR      = 1
    PROFESSIONAL = 2
    MASTER       = 3

class User(TimeStampedModel):
    name     = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    kakao_id = models.IntegerField(unique=True)
    rank     = models.ForeignKey('UserRank', on_delete=models.SET_DEFAULT, default=UserRankEnum.AMATEUR.value)
    point    = models.IntegerField(default=100000)

    class Meta:
        db_table = 'users'

class UserRank(models.Model):
    rank = models.CharField(max_length=20)

    class Meta:
        db_table = 'users_ranks'