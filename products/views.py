from django.shortcuts import render
from django.http import HttpResponse
from .models import Products , Offer


def index(request):
    products = Products.objects.all()
    return render(request, 'index.html', {'products': products})


def secondIndex(request):
    return HttpResponse("new product of hamza")
