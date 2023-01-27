from django.contrib import admin
from .models import Rental, RentalRate, Vehicule, VehiculeSize, VehiculeType, Customer
# Register your models here.
admin.site.register(Rental)
admin.site.register(RentalRate)
admin.site.register(Vehicule)
admin.site.register(VehiculeSize)
admin.site.register(VehiculeType)
admin.site.register(Customer)