from rest_framework import serializers
from .models import Product, Customer


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        exclude = ['deleted']


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        exclude = ['mobilepay_id', 'deleted']