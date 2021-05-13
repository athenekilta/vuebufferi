from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {(self.price/100):.2f}€ {self.quantity} kpl"
 

class Customer(models.Model):
    name = models.CharField(max_length=140)
    balance = models.IntegerField()
    deleted = models.BooleanField(default=False)
    mobilepay_id = models.CharField(max_length=140, blank=True, null=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    timestamp = models.DateTimeField()
    product = models.ForeignKey(Product, null=True, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.PROTECT)