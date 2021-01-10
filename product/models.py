from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Product(models.Model):

    name = models.CharField(max_length=50)
    heading_txt = models.TextField()
    description = models.TextField()
    price = models.CharField(max_length=15)
    pic = models.TextField()
    stock = models.TextField()
    quantity = models.TextField()
   

    def __str__(self):
        return self.name
    
