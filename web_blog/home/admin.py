from django.contrib import admin
from . import models
# Register your models here.
class ChangeAdmin(admin.ModelAdmin):
    list_display = ["name" , "is_active"]
    prepopulated_fields = {
        "slug" : ["title"]
    }
admin.site.register(models.Product , ChangeAdmin)