from django.forms import ModelForm
from .models import Customer, Rental, Vehicule
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
class RentalForm(ModelForm):
    class Meta:
        model = Rental
        fields = "__all__"
class VehiculeForm(ModelForm):
    class Meta:
        model = Vehicule
        fields = "__all__"