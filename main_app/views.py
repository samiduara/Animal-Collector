from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Animal
# Create your views here.
class AnimalCreate(CreateView):
  model = Animal
  fields = '__all__'
  success_url = '/animals/'

class AnimalUpdate(UpdateView):
  model = Animal
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class AnimalDelete(DeleteView):
  model = Animal
  success_url = '/cats/'  

def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

def home(request):
  return render(request, 'about.html')

def about(request):
  return render(request, 'about.html')  

def animals_index(request):
  animals = Animal.objects.all()
  return render(request, 'animals/index.html', { 'animals': animals })  

def animals_detail(request, animal_id):
  animal = Animal.objects.get(id=animal_id)
  return render(request, 'animals/detail.html', { 'animal': animal })  