from django.shortcuts import render, redirect
from catalog.forms import RegisterForm
from catalog.models import Vehicle


def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        Vehicle.objects.create(vehicle_type=request.POST['vehicle_type'],
                               brand=request.POST['brand'],
                               model=request.POST['model'],
                               version=request.POST['version'],
                               license_plate=request.POST['license_plate'],
                               mileage=request.POST['mileage'])
        return redirect('home')
    return render(request, 'register.html', {'form': form})


def home(request):
    vehicles = Vehicle.objects.all().order_by('-id')[:10]
    return render(request, 'home.html', {'vehicles': vehicles})


def edit_view(request, vi):
    if request.method == "POST":
        vehicle = Vehicle.objects.get(version=vi)
        vehicle.vehicle_type = request.POST['vehicle_type']
        vehicle.brand = request.POST['brand']
        vehicle.model = request.POST['model']
        vehicle.version = request.POST['version']
        vehicle.license_plate = request.POST['license_plate']
        vehicle.mileage = request.POST['mileage']
        vehicle.save()
        return redirect('home')

    vehicle = Vehicle.objects.get(version=vi)
    form = RegisterForm(initial={'vehicle_type': vehicle.vehicle_type,
                                 'brand': vehicle.brand,
                                 'model': vehicle.model,
                                 'version': vehicle.version,
                                 'license_plate': vehicle.license_plate,
                                 'mileage': vehicle.mileage})
    return render(request, 'edit.html', {'form': form})


def delete_view(request, vi):
    vehicle = Vehicle.objects.get(version=vi)
    vehicle.delete()
    return redirect('home')
