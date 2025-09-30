from django.db import models

# Create your models here.

class Product(models.Model):
    title=models.CharField(max_length=120)
    price=models.FloatField()
    discount_price=models.FloatField()
    category=models.CharField(max_length=120)
    
    description=models.TextField()
    image=models.CharField(max_length=500)
    
    
    
    def __str__(self):
        return self.title
    
    
class Order(models.Model):
    items=models.CharField(max_length=5000)
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    Address=models.CharField(max_length=500)
    City=models.CharField(max_length=120)
    state=models.CharField(max_length=120)
    zipcode=models.CharField(max_length=20)
    total=models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.name
    