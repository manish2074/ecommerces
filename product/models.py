from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Product(models.Model):

    CONDITION_TYPE = (
        ("New","New"),
        ("Used","Used")

    )

    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User , on_delete= models.CASCADE)
    description = models.TextField(max_length=500)
    condition = models.CharField(max_length=100,choices=CONDITION_TYPE)
    category = models.ForeignKey('Category' , on_delete= models.SET_NULL,null= True)
    brand = models.ForeignKey('Brand' , on_delete= models.SET_NULL,null= True)
    price = models.DecimalField(max_digits=10,decimal_places=5)
    created = models.DateTimeField(default=timezone.now)
    

    
    def __str__(self):
        return self.name

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name='Product Image'
        verbose_name_plural='Product Images'

class Category(models.Model):
    ##for product category
    category_name = models.CharField(max_length=50) 
    image = models.ImageField(upload_to='category/', blank=True , null=True) 
    
    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.category_name



class Brand(models.Model):
    ##for product brand
    brand = models.CharField(max_length=50) 
    
    
    class Meta:
        verbose_name='brand'
        verbose_name_plural='brands'

    def __str__(self):
        return self.brand

