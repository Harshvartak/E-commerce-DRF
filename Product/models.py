from django.db import models
from User.models import CustomUser

class Product(models.Model):
    title=models.CharField(max_length=30,unique=True)
    descrip=models.TextField(blank=True)
    image=models.ImageField(upload_to='images/')
    cost = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    published_date=models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(CustomUser, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

class Cart(models.Model):
    user = models.OneToOneField(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product , blank=True)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return "User: has items in their cart. Their total is ${}".format( self.total)
    def save(self, *args, **kwargs):
        self.total=0
        for product in self.products.all():
            self.total+=product.cost
        super(Cart, self).save(*args, **kwargs)


    def get_all_products(self):
        product=[]
        for prod in self.products:
            product.append(prod)
        return product
