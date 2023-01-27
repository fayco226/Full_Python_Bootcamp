from django.db import models

# Create your models here.
class Family(models.Model):
    nameA = models.CharField(max_length=150)

 
class Animal(models.Model):
    nameF = models.CharField(max_length = 150)
    legs = models.IntegerField(default=2)
    weight = models.IntegerField(default=55)
    height = models.IntegerField(default=65)
    speed = models.IntegerField(default=78)
    family_fk = models.ForeignKey(Family, on_delete=models.CASCADE)
    
    
    
    
    
