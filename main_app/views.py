from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
class Animal:  
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
  return HttpResponse('<h1>About The Animal collector</h1>')

def about(request):
  return render(request, 'about.html')  
def animals_index(request):
  return render(request, 'animals/index.html', { 'animals': animals })  