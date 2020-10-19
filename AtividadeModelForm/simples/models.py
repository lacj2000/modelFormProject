from django.db import models

# simples
class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    quantity = models.IntegerField()
    def __str__(self):
        return self.name
