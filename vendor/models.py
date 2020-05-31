from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name