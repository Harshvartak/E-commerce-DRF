from rest_framework import serializers

from .models import Cart,Product

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields= ['user','total','updated','products','quantity']



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['title','descrip','image','cost','published_date','publisher']
