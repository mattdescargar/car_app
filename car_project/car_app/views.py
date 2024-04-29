from django.shortcuts import render, get_object_or_404
from .models import Car
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.http import JsonResponse

@csrf_exempt
def update_positions(request):
    if request.method == 'POST':
        positions = request.POST.getlist('positions[]')
        cars = [Car(id=car_id, position=index) for index, car_id in enumerate(positions, start=1)]

        with transaction.atomic():
            Car.objects.bulk_update(cars, ['position'])

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

def list_cars(request):
    cars = Car.objects.all().order_by('position')
    return render(request, 'car_app/list_cars.html', {'cars': cars})

@csrf_exempt
def move_car(request, car_id, new_position):
    car = get_object_or_404(Car, id=car_id)
    car.position = int(new_position)
    car.save()
    return JsonResponse({'success': True})
def query_cars(request, color):
    cars = Car.objects.filter(color=color).order_by('position')
    return render(request, 'car_app/list_cars.html', {'cars': cars})
