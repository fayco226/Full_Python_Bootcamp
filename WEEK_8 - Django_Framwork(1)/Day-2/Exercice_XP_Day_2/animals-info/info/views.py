from django.shortcuts import render
from .models import Animal, Family
# Create your views here.






def home(request):
    data = Animal.objects.all()
    context ={
        "data": data,
        }
    return render(request, "info/home.html", context)

def family(request, x):
    data2 = Family.objects.get(id = x)
    data = Animal.objects.filter(family_fk_id = x)
    family_name = data2.nameA
    
    context = {
        "list" : data,
        "name": family_name
    }
    return render(request, "info/family.html", context)

def animals(request, y):
    data = Animal.objects.get(id=y)
    x = data.family_fk_id
    data2 = Family.objects.get(id = x)
    family_name = data2.nameA
    
    context = {
        "data":data,
        "name": family_name
        }
    return render(request, "info/animal.html", context)
    
