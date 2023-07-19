from django.db import models

# Create your models here.

class Dish_data(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    items = models.TextField(default=None)
    lat_long = models.TextField(default=None)
    full_details = models.TextField(default=None)