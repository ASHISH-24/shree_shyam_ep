from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=850)
    price = models.FloatField()
    description = models.TextField()
    imglink = models.CharField(max_length=2000)

class Order(models.Model):
    first_name = models.CharField(max_length=400)
    contact = models.CharField(max_length=400)
    address = models.CharField(max_length=400)
    fulfilled = models.BooleanField()
    items = models.TextField()
