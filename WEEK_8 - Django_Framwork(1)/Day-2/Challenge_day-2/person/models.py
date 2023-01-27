from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Person(models.Model):
    name = models.CharField( max_length=50)
    email = models.CharField(max_length=50)
    phone = PhoneNumberField()
    adresse = models.CharField(max_length=50)
       

    def __str__(self):
        return self.name


    