from django.shortcuts import render

# Create your views here.

people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

def home(request):
      
  context = {
        "data": people,
    }
  return render(request, "people/home.html", context)

def by_age(request):
    
    people1 = sorted(people, key = lambda d: d['age'])
    
    context = {
      "data":people1
    }
    return render(request, "people/by_age.html", context)

def by_id(request, x):
    people2 = []
    for i in people:
        if i['id'] == x:
          people2.append(i)
    context = {
      "data":people2
    }
    return render(request, "people/by_id.html", context)
    