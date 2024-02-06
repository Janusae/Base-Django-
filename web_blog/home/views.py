from django.shortcuts import render , get_object_or_404 , redirect
from .models import Product
from django.urls import reverse
from django.http import HttpResponse
show = Product.objects.all()
# Create your views here.
def home(request):
    return render(request , "home/home.html" , {
        "data" : show
    })
def django_render_partial_header(request):
    return render(request , "header.html")
def django_render_partial_footer(request):
    return render(request , "footer.html")
def get(request , slug):
    check = get_object_or_404(Product , slug=slug)
    return render(request , "home/details.html" , {
        "data" : check
    })

def login(request):
    return redirect(reverse("login"))