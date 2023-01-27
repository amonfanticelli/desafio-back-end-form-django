from django.db import models


class Form(models.Model):
    type = models.CharField(max_length=1)
    date = models.DateField(max_length=8)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=11)
    creditCard = models.CharField(max_length=12)
    time = models.TimeField(max_length=6)
    storeOwner = models.CharField(max_length=14)
    storeName = models.CharField(max_length=19)
