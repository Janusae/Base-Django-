from django.urls import path
from . import views
urlpatterns = [
    path("login" , views.login , name = "get") ,
    path("create_account" , views.account , name = "create_account")
]