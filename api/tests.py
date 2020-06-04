from django.test import TestCase
from rest_framework.exceptions import ErrorDetail

from .models import Vendor, Product
from .serializers import VendorSerializer


class VendorTestCase(TestCase):
    def setUp(self):
        vendor = Vendor.objects.create(name="tester vendor 01", cnpj="62.558.420/0001-45",
                                       city="Monteiro")
        Product.objects.create(name="item 01", code="ABC123456", price=12, vendor=vendor)
        Product.objects.create(name="item 02", code="ABC123456", price=19.86, vendor=vendor)

    def test_add_vendor(self):
        """Vendor was created correct"""
        vendor_test = Vendor.objects.get(name="tester vendor 01")
        self.assertEqual(vendor_test.cnpj, '62.558.420/0001-45')

    def test_add_vendor_with_same_cnpj(self):
        """Test unique cnpj"""
        with self.assertRaisesMessage(Exception, "UNIQUE constraint failed: api_vendor.cnpj"):
            self.assertIsInstance(Exception, Vendor.objects.create(name="tester vendor 01", cnpj="62.558.420/0001-45",
                                                                   city="Monteiro"))

    def test_remove_vendor_with_products(self):
        """Tester if cascaste delete is work"""
        vendor_test = Vendor.objects.get(cnpj="62.558.420/0001-45")
        vendor_test.delete()
        with self.assertRaisesMessage(Vendor.DoesNotExist, "Vendor matching query does not exist."):
            self.assertIsInstance(Vendor.DoesNotExist, Vendor.objects.get(id=vendor_test.id))

        with self.assertRaisesMessage(Product.DoesNotExist, "Product matching query does not exist."):
            self.assertIsInstance(Product.DoesNotExist, Product.objects.get(name="item 01"))

        with self.assertRaisesMessage(Product.DoesNotExist, "Product matching query does not exist."):
            self.assertIsInstance(Product.DoesNotExist, Product.objects.get(name="item 02"))


class VendorSerializerTest(TestCase):
    def setUp(self):
        self.serializer_vendor_data = {
            'products': [
                {
                    'name': 'test gugu',
                    'code': 'fas2232d3221',
                    'price': 100.5
                }
            ],
            'name': 'teste 021 LTDM.',
            'cnpj': '55.532.845/0001-10',
            'city': 'Monteiro'
        }
        self.serializer_vendor_data_not_valid_products = {
            'name': 'teste 021 LTDM.',
            'cnpj': '55.532.845/0001-10',
            'city': 'Monteiro'
        }

        self.serializer_vendor_data_not_required_fields = {
            'products': [
                {
                    'name': 'test gugu',
                    'code': 'fas2232d3221',
                },

                {
                    'id': 12,
                    'name': 'test gugu',
                    'code': 'fas2232d3221',
                    'price': 100.5
                }
            ],
            'name': 'teste 021 LTDM.',
            'cnpj': '55.532.845/0001-10',
        }

        self.serializer_vendor = VendorSerializer(data=self.serializer_vendor_data)

    def test_vendor_serializer(self):
        """Test validate data insert vendors"""
        assert self.serializer_vendor.is_valid()
        assert self.serializer_vendor.errors == {}

    def test_vendor_serializer_with_error_product(self):
        """Test validate data insert vendors without products"""
        self.serializer_vendor = VendorSerializer(data=self.serializer_vendor_data_not_valid_products)
        self.assertEqual(self.serializer_vendor.is_valid(), False)
        assert self.serializer_vendor.errors == {'products': [ErrorDetail(string='This field is required.',
                                                                          code='required')]}

    def test_vendor_serializer_without_fields(self):
        """Test validate data insert vendors without not required fields"""
        self.serializer_vendor = VendorSerializer(data=self.serializer_vendor_data_not_required_fields)
        self.assertEqual(self.serializer_vendor.is_valid(), True)
        assert self.serializer_vendor.errors == {}


