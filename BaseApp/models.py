from django.db import models
from django.utils import timezone

# Create your models here.
class FeedbackDb(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    query = models.CharField(max_length=100)
    feedback = models.CharField(max_length=400)
    time_date = models.DateTimeField(default=timezone.now)

class RecipesDb(models.Model):
    username = models.CharField(max_length=20)
    dishname = models.CharField(max_length=20)
    ingredients = models.TextField()
    recipe = models.TextField()
    time_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.dishname