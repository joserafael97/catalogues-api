from django.contrib import admin

from .models import Product
from .models import Vendor

admin.site.register(Vendor)
admin.site.register(Product)
