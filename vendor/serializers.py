from rest_framework import serializers
from .models import Vendor
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'code', 'price', 'create_at']


class VendorSerializer(serializers.HyperlinkedModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Vendor
        fields = ['id', 'name', 'cnpj', 'products', 'city', 'create_at']

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        vendor = Vendor.objects.create(**validated_data)
        for product_data in products_data:
            Product.objects.create(vendor=vendor, **product_data)
        return vendor
