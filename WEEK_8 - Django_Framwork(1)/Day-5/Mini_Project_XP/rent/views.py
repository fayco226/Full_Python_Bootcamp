from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomerForm, RentalForm, VehiculeForm
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Customer, Vehicule, Rental

from faker import Faker


def customer_fill_by_faker():
    fake = Faker()
    for _ in range(30):
        customer = Customer(first_name=fake.first_name(),
                            last_name=fake.last_name(),
                            email=fake.email(),
                            phone_number=fake.phone_number(),
                            address=fake.adress(),
                            city=fake.city(),
                            country=fake.country())
        customer.save()


# Create your views here.

def vehiculelist(request, id=0):
    if id == 0:
        vehicule = Vehicule.objects.all()
        page = Paginator(vehicule, 4)
        pge = request.GET.get('page')
        cust = page.get_page(pge)
        var = 0
        return render(request, 'rent/vehiculelist.html', {'models': cust, 'len': var})
    else:
        vehicule = Vehicule.objects.filter(id=id)
        rent = Rental.objects.filter(vehicule_id=id)
        if len(rent) != 0:
            v = 1
        else:
            v = 0
        var = 1
        return render(request, 'rent/vehiculelist.html', {'models': vehicule, 'len': var, 'av': v})

def returnVehicule(request, id):
    Rental.objects.get(vehicule_id=id).delete()
    return redirect('vehiculelist')
def addVehicule(request):
    if request.method == "POST":
        form = VehiculeForm(request.POST)
        vehicule = Vehicule.objects.all()
        page = Paginator(vehicule, 4)
        pge = request.GET.get('page')
        cust = page.get_page(pge)
        if form.is_valid():
            form.save()
            messages.success(request, "Vehicule added !")
            return redirect('vehiculelist')
        else:
            return render(request, 'rent/addVehicule.html', {"form": form, 'models': cust})
    else:
        form = VehiculeForm()
        vehicule = Customer.objects.all()
        page = Paginator(vehicule, 5)
        pge = request.GET.get('page')
        cust = page.get_page(pge)

        return render(request, 'rent/addVehicule.html', {"form": form, 'models': cust})


def rentallist(request, id=0):
    if id == 0:
        rental = Rental.objects.all()
        page = Paginator(rental, 4)
        pge = request.GET.get('page')
        cust = page.get_page(pge)
        var = 0
        return render(request, 'rent/rentallist.html', {'models': cust, 'len': var})
    else:
        rental = Rental.objects.filter(id=id)
        var = 1
        return render(request, 'rent/rentallist.html', {'models': rental, 'len': var})


def addRental(request):
    if request.method == "POST":
        rental = Rental.objects.all()
        form = RentalForm(request.POST)
        page = Paginator(rental, 10)
        pge = request.GET.get('page')
        cust = page.get_page(pge)
        if form.is_valid():
            z = 0
            cc = form.cleaned_data["vehicule"]
            for i in rental:
                if i.vehicule == cc:
                    z += 1
            if z == 0:
                form.save()
                messages.success(request, "Rental added !")
                return redirect('rentallist')
            else:
                return HttpResponse("vehicle already take")
        else:
            return render(request, 'rent/addRental.html', {"form": form, 'models': cust})
    else:
        form = RentalForm()
        rental = Rental.objects.all()
        page = Paginator(rental, 5)
        pge = request.GET.get('page')
        cust = page.get_page(pge)

        return render(request, 'rent/addRental.html', {"form": form, 'models': cust})


def home0(request):
    return render(request, 'rent/home0.html')


def home(request, id=0):
    if id == 0:
        customer = Customer.objects.all()
        page = Paginator(customer, 5)
        pge = request.GET.get('page')
        cust = page.get_page(pge)
        var = len(customer)
        return render(request, 'rent/home.html', {'models': cust, 'len': var})
    else:
        customer = Customer.objects.filter(id=id)
        var = len(customer)
        return render(request, 'rent/home.html', {'models': customer, 'len': var})


def addCustomer(request):
    if request.method == "POST":
        customer = Customer.objects.all()
        form = CustomerForm(request.POST)
        page = Paginator(customer, 10)
        pge = request.GET.get('page')
        cust = page.get_page(pge)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer added !")
            return redirect('home')
        else:
            return render(request, 'rent/addCustomer.html', {"form": form, 'models': cust})
    else:
        form = CustomerForm()
        customer = Customer.objects.all()
        page = Paginator(customer, 5)
        pge = request.GET.get('page')
        cust = page.get_page(pge)

        return render(request, 'rent/addCustomer.html', {"form": form, 'models': cust})
