from django.db import models
from brand.models import BrandModel
from django.contrib.auth.models import User

# Create your models here.

class CarModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='uploads/')
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class CommentModel(models.Model):
    car_model = models.ForeignKey(CarModel,on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class OrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.car_model.name}"