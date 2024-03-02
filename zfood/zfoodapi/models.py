from django.db import models
from django.utils import timezone


# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    occupation = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    delegation = models.CharField(max_length=50)
    photo = models.FileField(upload_to='zfood/static/user_upload')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Store(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    image = models.ImageField(upload_to='zfood/static/store_upload')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Association(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='zfood/static/association_upload')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Command(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

class bouquet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    command = models.ForeignKey(Command, on_delete=models.CASCADE)



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='zfood/static/product_upload')
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    expiration_date = models.DateTimeField(default=timezone.now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bouquet = models.ForeignKey(bouquet, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    association = models.ForeignKey(Association, on_delete=models.CASCADE)






