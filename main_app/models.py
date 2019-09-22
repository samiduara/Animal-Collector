from django.db import models
from django.urls import reverse


# Create your models here.
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Animal(models.Model):
 name = models.CharField(max_length=100)
 breed = models.CharField(max_length=100)
 description = models.TextField(max_length=250)
 age = models.IntegerField()

def __str__(self):
   return self.name

def get_absolute_url(self):
    return reverse('detail', kwargs={'animal_id': self.id})   

def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )
  animal = models.ForeignKey(Animal, on_delete=models.CASCADE)    