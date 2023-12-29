from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    image = models.ImageField(upload_to='BannerImage/')
    url_http_link = models.URLField(max_length=500, blank=True, null=True)
    class Meta:
        
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE,blank=True, null=True,related_name='child')
    image = models.ImageField(upload_to='CategoryImage/', blank=True,  null=True)
    class Meta:
        
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    image = models.ImageField(upload_to='BrandImage/', blank=True,  null=True)
    class Meta:
        
        verbose_name_plural = 'Brand'

    def __str__(self):
        return self.name
        
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    price = models.PositiveIntegerField(max_length=30)
    discount_price = models.PositiveIntegerField(max_length=30,blank=True, null=True)
    stock = models.PositiveIntegerField(max_length=30,blank=True, null=True)
    discription = RichTextField()
    image = models.ImageField(upload_to='Product_image/')
    slug = AutoSlugField(populate_from='product_name', unique=True, blank=True, null=True)
    class Meta:
        
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.product_name


class Cart_Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.product_name
    
    def product_subtotal(self):
        if self.product.discount_price:
            return self.product.discount_price * self.quantity
        else:
            return self.product.price * self.quantity

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_product = models.ManyToManyField(Cart_Product)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for i in self.cart_product.all():
            total += i.product_subtotal()
        return total