from django.shortcuts import render
from brand.models import BrandModel
from car.models import CarModel

# Create your views here.

def index(request, brand_name = None):
    cars = CarModel.objects.all()
    brands = BrandModel.objects.all()
    
    if brand_name is not None:
        cars = CarModel.objects.filter(brand__name=brand_name)
    
    return render(request, "index.html", {"cars": cars, "brands": brands})