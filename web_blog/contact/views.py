from django.shortcuts import render , redirect
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
def contact(request):
    return render(request , "contact/contact_us.html")
def register(request):
    if request.POST["name"] == "":
        print(request.POST)
        return render(request , "contact/contact_us.html" , {
            "error" : True
        })
    else :
        return redirect(reverse("home"))
        return render(request, "contact/contact_us.html", {
            "error": False
         })