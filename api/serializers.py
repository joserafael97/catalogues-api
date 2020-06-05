"""Module to serializers data in rest API"""
from rest_framework import serializers

from .models import Product
from .models import Vendor


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'code', 'price', 'create_at']


class VendorSerializer(serializers.HyperlinkedModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Vendor
        fields = ['id', 'name', 'cnpj', 'products', 'city', 'create_at']

    def create(self, validated_data):
        """Create Vendor with associated products.

           Superscript default function to Save Vendor and
           products with relationship.

           Return Vendor and products saved.
        """
        products_data = validated_data.pop('products')
        vendor = Vendor.objects.create(**validated_data)
        for product_data in products_data:
            Product.objects.create(vendor=vendor, **product_data)
        return vendor

    def update(self, instance, validated_data):
        """Update Vendor with associated products.

           Superscript default function to Update Vendor and
           products with relationship.

           Return Vendor and products updated.
        """
        products = validated_data.pop('products')
        product_items_dict = dict((i.id, i) for i in instance.products.all())
        instance.city = validated_data['city']
        instance.name = validated_data['name']
        instance.cnpj = validated_data['cnpj']

        for product_data in products:
            if 'id' in product_data:
                product_item = product_items_dict.pop(product_data['id'])
                product_item.name = product_data['name']
                product_item.code = product_data['code']
                product_item.price = product_data['price']
                product_item.save()
            else:
                Product.objects.create(vendor=instance, **product_data)

        if len(product_items_dict) > 0:
            for product in product_items_dict.values():
                product.delete()

        instance.save()
        return instance
