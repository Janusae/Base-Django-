from django.db import models
from django.utils.text import slugify
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30 , verbose_name="سربرگ محصول")
    name = models.CharField(max_length=30 , verbose_name="نام محصول")
    price = models.IntegerField(verbose_name="قیمت محصول")
    link_img = models.CharField(max_length=500 , verbose_name="لینک محصول")
    description = models.TextField(verbose_name="توضیحات محصول")
    is_active = models.BooleanField(default=False , verbose_name="محصول موجود است")
    slug =  models.SlugField(default="")
    def save(self , *args,**kwargs ):
        self.slug = slugify(self.title)
        super().save(*args , **kwargs)
    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
    def __str__(self):
        return f"{self.name}"