from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass


class Food(models.Model):
    name = models.CharField(max_length=100),
    calories = models.IntegerField(default=0),
    protein = models.IntegerField(default=0),
    fat = models.IntegerField(default=0),
    rel_user = models.ForeignKey(User, on_delete=models.CASCADE),
