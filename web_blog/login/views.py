from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
def login(request):
    return render(request , "login/login.html")

def account(request):
    return redirect(reverse("account"))