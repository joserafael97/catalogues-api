from rest_framework import viewsets

from .serializers import VendorSerializer
from .models import Vendor


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all().order_by('name')
    serializer_class = VendorSerializer
