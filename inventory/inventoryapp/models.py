# Create your models here.
from django.db import models

class Inventory(models.Model):  # model class
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def _str_(self):
        return self.name