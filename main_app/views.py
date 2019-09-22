from django.shortcuts import render
from .models import Animal
# Create your views here.

def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

animals = [
  Animal('Lion', 'mufasa', 'little demon', 3),
  Animal('Tiger', 'brown', 'crazy', 0),
  Animal('Hyena', 'black tripod', '3 legged hyena', 4)
]    

def home(request):
  return render(request, 'about.html')

def about(request):
  return render(request, 'about.html')  

def animals_index(request):
  animals = Animal.objects.all()
  return render(request, 'animals/index.html', { 'animals': animals })  