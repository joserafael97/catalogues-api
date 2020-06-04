from rest_framework import viewsets
from django.http import HttpResponseNotFound
import json

from .serializers import VendorSerializer
from .serializers import ProductSerializer

from .models import Vendor
from .models import Product


class ProductViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Return a product instance.

        list:
            Return all products, ordered by most recently joined.

        create:
            Create a new product.

        delete:
            Remove an existing product associated.

        partial_update:
            Update one or more fields on an existing product.

        update:
            Update a product.
    """

    queryset = Product.objects.all().order_by('create_at')
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(
            vendor=self.kwargs["vendors_pk"])


class VendorViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Return a vendor instance.

        list:
            Return all vendors, ordered by most recently joined.

        create:
            Create a new vendor.

        delete:
            Remove an existing vendor and products associated.

        partial_update:
            Update one or more fields on an existing vendor.

        update:
            Update a vendor.
    """

    queryset = Vendor.objects.all().order_by('create_at')
    serializer_class = VendorSerializer


def error404(request, exception):
    response_data = {}
    response_data['detail'] = 'Not found.'
    return HttpResponseNotFound(json.dumps(response_data), content_type="application/json")


