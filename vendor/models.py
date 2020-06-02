from django.db import models
from localflavor.br.models import BRCNPJField
from django.core.validators import MinValueValidator


class Vendor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False)
    cnpj = BRCNPJField(unique=True, blank=False)
    city = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    code = models.CharField(max_length=255, blank=False)
    price = models.FloatField(verbose_name=u'The price cannot be less than zero', validators=[MinValueValidator(0.0)])
    create_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name