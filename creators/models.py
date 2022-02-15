from django.db import models

from users.models import User

class Creator(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    name        = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    class Meta:
        db_table = 'creators'
