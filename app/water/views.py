from django.shortcuts import render, redirect

from plants.models import Plant

from .models import Water

# Create your views here.
def new_water(request, plant_id=None):
    Water.objects.create(plant=Plant.objects.get(id=plant_id))
    return redirect('/plants/')
