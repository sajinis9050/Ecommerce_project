from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Offer, Home, Cart, Chat


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def index2(request):
    offers = Offer.objects.all()
    return render(request, 'index2.html', {'offers': offers})


def index3(request):
    home = Home.objects.all()
    return render(request, 'index3.html', {'home': home})


def index4(request):
    cart = Cart.objects.all()
    return render(request, 'index4.html', {'cart': cart})


def index5(request):
    chat = Chat.objects.all()
    return render(request, 'index5.html', {'chat': chat})


def new(request):
    return HttpResponse("New products")