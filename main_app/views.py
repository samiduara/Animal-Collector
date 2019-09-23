from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Animal
from .forms import FeedingForm
def signup(request):
 error_message = ''
 if request.method == 'POST':
   form = UserCreationForm(request.POST)
   if form.is_valid():
     user = form.save()
     login(request, user)
     return redirect('index')
   else:
     error_message = 'Invalid credentials - try again'
 form = UserCreationForm()
 context = {'form': form, 'error_message': error_message}
 return render(request, 'registration/signup.html', context)

class AnimalCreate(CreateView):
  model = Animal
  fields = '__all__'
  success_url = '/animals/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class AnimalUpdate(UpdateView):
  model = Animal
  fields = ['breed', 'description', 'age']

class AnimalDelete(DeleteView):
  model = Animal
  success_url = '/animals/'  

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
  feeding_form = FeedingForm
  return render(request, 'animals/detail.html', {
    'animal': animal, 'feeding_form': feeding_form
  })

def add_feeding(request, animal_id):
 form = FeedingForm(request.POST)
 if form.is_valid():
   new_feeding = form.save(commit=False)
   new_feeding.animal_id = animal_id
   new_feeding.save()
 return redirect('detail', animal_id=animal_id)  