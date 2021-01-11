from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    dateupdated = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = ['id','SKU','name','qty','price','created', 'dateupdated']

class ProductCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id']
        read_only_fields = ['SKU','name','qty','price', 'created','dateupdated']
