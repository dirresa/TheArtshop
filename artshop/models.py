from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    image = models.ImageField(upload_to='artshop/categories', default='artshop/categories/default.png')

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    image = models.ImageField(upload_to='artshop/images', default='artshop/images/default.png')
    price = models.FloatField(default=0.0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    viewed = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    subject = models.CharField(max_length=200, null=True)
    message = models.TextField(null=True)
    created = models.DateTimeField(default=timezone.now)
