from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    deleted = models.BooleanField(default=False)


class Transaction(models.Model):
    timestamp = models.DateTimeField()
    product = models.ForeignKey(Product, null=True, on_delete=models.PROTECT)
    # TODO: ForeignKey to Customer and possibly MP_ID
