from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def phonenumber(request, number):
    person = Person.objects.filter(phone = number)
    if len(person) != 0:
        return render(request, "person/phonenumber.html", {'personnes': person})
    else:
        return HttpResponse(f"This Number {number} does not exist in database")
    
def name(request, name):
    person = Person.objects.filter(name = name)
    if len(person) != 0:
        return render(request, "person/name.html", {'personnes': person})
    else:
        return HttpResponse(f"This name {name} does not exist in database")
    
def home(request):
    personnes = Person.objects.all()
    return render(request, "person/home.html", {'personnes': personnes})


def add_person(request):
    if request.method=="POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Person added !")
            return redirect('home')
        else:
            return render(request, 'person/add_person.html', {"form":form})
    else:
        form = PersonForm()
        return render(request, 'person/add_person.html', {"form":form})