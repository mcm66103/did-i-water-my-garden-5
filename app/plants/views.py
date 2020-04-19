from django.shortcuts import render, redirect

from plants.models import Plant
from plants.forms import PlantForm

# Create your views here.
def plant_list(request):
    context = {
        "all_plants": Plant.objects.all(),
        "plant_form": PlantForm()
    }
    return render(request, 'plant_list.html', context)

def plant_detail(request, id=None):
    context = {
        "plant": Plant.objects.get(id=id)
    }
    return render(request, 'plant_detail.html', context)

def new_plant(request):
    if request.method == 'POST':
        new_plant_form = PlantForm(data=request.POST.copy())
        if new_plant_form.is_valid():
            new_plant_form.save()
    return redirect('/plants')

def delete_plant(request, id):
    Plant.objects.get(id=id).delete()
    return redirect('/plants')
