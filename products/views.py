from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Offer, Home


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def index2(request):
    offers = Offer.objects.all()
    return render(request, 'index2.html', {'offers': offers})


def index3(request):
    home = Home.objects.all()
    return render(request, 'index3.html', {'home': home})


def new(request):
    return HttpResponse("New products")