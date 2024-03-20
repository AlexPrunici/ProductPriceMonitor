from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from api.models import Product


class ProductTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.products = [
            Product.objects.create(name=f"product_{i}") for i in range(1, 4)
        ]

    def tearDown(self):
        Product.objects.all().delete()

    def test_get_all_products(self):
        url = reverse("product-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(self.products))

    def test_get_product_by_id(self):
        product = self.products[0]
        url = reverse("product-retrieve-by-id", kwargs={"pk": product.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], product.name)

    def test_get_product_by_wrong_id(self):
        url = reverse("product-retrieve-by-id", kwargs={"pk": "0"})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_product(self):
        url = reverse("product-create")
        data = {"name": "test_create_product"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 4)
        self.assertEqual(Product.objects.last().name, "test_create_product")

        created_product = Product.objects.get(name="test_create_product")
        created_product.delete()

    def test_cant_create_product_with_same_name(self):
        url = reverse("product-create")
        data = {"name": "test_cant_create_product_with_same_name"}
        response_1 = self.client.post(url, data, format="json")
        response_2 = self.client.post(url, data, format="json")

        self.assertEqual(response_1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cant_create_product_with_no_name(self):
        url = reverse("product-create")
        data = {"name": ""}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
