from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Offer


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def index2(request):
    offers = Offer.objects.all()
    return render(request, 'index2.html', {'offers': offers})


def new(request):
    return HttpResponse("New products")