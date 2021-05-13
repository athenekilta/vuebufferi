from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


def index(request):
    """Serves Vue frontend"""
    return render(request, template_name="index.html")


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(deleted=False)
    serializer_class = ProductSerializer
