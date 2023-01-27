from copy import deepcopy
from django.shortcuts import render

# Create your views here.
data = {
    "animals": [
        {
            "id" :1,
            "name": "Dog",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2
        },
        {
            "id": 2,
            "name": "Domestic Cat",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1
        },
        {
            "id": 3,
            "name": "Panther",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1 
        },
        {
            "id": 4,
            "name": "mouse",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2 
        },
        {
            "id": 5,
            "name": "Sheep",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 3 
        },
        {
            "id": 6,
            "name": "cow",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 3 
        },
        {
            "id": 7,
            "name": "pig",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 4 
        },
        {
            "id": 8,
            "name": "chicken",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 4 
        },
        {
            "id": 9,
            "name": "donkey",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 5 
        },
        {
            "id": 10,
            "name": "horse",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 5 
        },
        {
            "id": 11,
            "name": "cat",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 6 
        },
        {
            "id": 12,
            "name": "rabit",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 6
        },
        {
            "id": 13,
            "name": "duck",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 7 
        },
        {
            "id": 14,
            "name": "dauphin",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 7
        },
        {
            "id": 14,
            "name": "Turtle",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 8 
        },
        {
            "id": 15,
            "name": "Panther",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1 
        },
        {
            "id": 16,
            "name": "Shark",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 3 
        },
        {
            "id": 17,
            "name": "Octepus",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 8
        },
        {
            "id": 18,
            "name": "Giraffe",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2 
        }
    ],
    "families": [
        {
            "id": 1,
            "name": "Felidae"
        },
        {
            "id": 2,
            "name": "Caninae"
        },
        {
            "id":3,
            "name":"mamal"
        },
        {
            "id":4,
            "name":"mammifère"
        },
        {
            "id":5,
            "name":"reptile"
        },
        {
            "id":6,
            "name":"insecte"
        },
        {
            "id": 7,
            "name":"arachnide"
        },
        {
            "id": 8,
            "name":"amphibie"
        }
        
        
    ]
}

data1 = deepcopy(data)


def home(request):
    context ={
        "data": data,
        }
    return render(request, "info/home.html", context)

def family(request, x):
    list_family_animal = []
    for value in data1["animals"]:
        if value["family"] == x:
            list_family_animal.append(value)
    for val in data1["families"]:
        if val["id"] == x:
            for va in list_family_animal:
                va["family_name"] = val["name"]
    context = {
        "list" : list_family_animal,
    }
    return render(request, "info/family.html", context)

def animals(request, y):
    list_animal = []
    for value in data1["animals"]:
        if value["id"]==y:
            list_animal.append(value)
    for val in data1["families"]:
        if val["id"] == y:
            for va in list_animal:
                va["family_name"] = val["name"] 
    context = {"list":list_animal}
    return render(request, "info/animal.html", context)
    
    