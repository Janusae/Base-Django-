from django.db import models

# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=30 , verbose_name="نام")
    email = models.EmailField(max_length=30 , verbose_name="ایمیل")
    subject =models.CharField(max_length=30 , verbose_name="موضوع")
    company = models.CharField(max_length=30 , verbose_name="کمپانی")
    message = models.TextField(verbose_name="پیام")
