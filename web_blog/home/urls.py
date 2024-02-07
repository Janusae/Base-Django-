from django.urls import path
from . import views
urlpatterns = [
    path("" , views.home , name = "home"),
    path("login" , views.login , name = "log"),
    path("contact_us" , views.contact , name = "contact_uses"),
    path("about" , views.about , name = "about"),
    path("product" , views.product , name = "product_get"),
    path("<slug>" , views.get , name = "get")
]