from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
 

class Customer(models.Model):
    name = models.CharField(max_length=140)
    balance = models.IntegerField()
    deleted = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    mobilepay_id = models.CharField(max_length=140, blank=True, null=True)


class Transaction(models.Model):
    timestamp = models.DateTimeField()
    product = models.ForeignKey(Product, null=True, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.PROTECT)