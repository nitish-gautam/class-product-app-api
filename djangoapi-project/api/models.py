from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    SKU = models.CharField(max_length = 50)
    name =models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    dateupdated = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.SKU +" " + self.name
