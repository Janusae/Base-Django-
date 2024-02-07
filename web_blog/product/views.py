from django.shortcuts import render
from django.http import HttpResponse
from .models import models
# Create your views here.
def produc(request):
    return render(request , "product/product.html")