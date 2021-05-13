from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Customer
from .serializers import ProductSerializer, CustomerSerializer


def index(request):
    """Serves Vue frontend"""
    return render(request, template_name="index.html")


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(deleted=False)
    serializer_class = ProductSerializer


class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.filter(deleted=False)
    serializer_class = CustomerSerializer