from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from main.models import Car, Sale


def cars_list_view(request):
    # получите список авто
    cars = Car.objects.all()
    if 'q' in request.GET:
        query = request.GET['q'].lower()
        cars = cars.filter(
            Q(model__icontains=query) |
            Q(year__icontains=query) |
            Q(color__icontains=query) |
            Q(mileage__icontains=query) |
            Q(volume__icontains=query) |
            Q(body_type__icontains=query) |
            Q(drive_unit__icontains=query) |
            Q(gearbox__icontains=query) |
            Q(fuel_type__icontains=query) |
            Q(price__icontains=query)
        )

    template_name = 'main/list.html'
    return render(request, template_name, {'cars': cars})  # передайте необходимый контекст


def car_details_view(request, car_id):
    # получите авто, если же его нет, выбросьте ошибку 404
    template_name = 'main/details.html'
    car = get_object_or_404(Car, pk=car_id)
    return render(request, template_name, {'car': car})  # передайте необходимый контекст


def sales_by_car(request, car_id):
    try:
        # получите авто и его продажи
        car = Car.objects.get(id=car_id)
        sales = Sale.objects.filter(car=car)
        template_name = 'main/sales.html'
        return render(request, template_name, {'sales': sales})  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
