from django.contrib import admin
from .models import Vendor
from .models import Product


admin.site.register(Vendor)
admin.site.register(Product)
