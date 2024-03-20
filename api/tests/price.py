from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from api.models import Product, Price
from datetime import date


class PriceTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product")
        prices_data = [
            {"price": 10.00, "date": date(2024, 1, 1)},
            {"price": 20.00, "date": date(2020, 1, 1)},
            {"price": 30.00, "date": date(2021, 1, 1)},
            {"price": 40.00, "date": date(2022, 1, 1)},
        ]
        for price_data in prices_data:
            Price.objects.create(product=self.product, **price_data)

        self.prices = Price.objects.filter(product=self.product)

    def tearDown(self):
        Product.objects.all().delete()
        Price.objects.all().delete()

    def test_get_all_prices(self):
        url = reverse("price-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_retrieve_price_by_id(self):
        price = self.prices[0]
        url = reverse("price-retrieve-by-id", kwargs={"pk": price.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["price"], "10.00")

    def test_retrieve_price_by_wrong_id(self):
        url = reverse("price-retrieve-by-id", kwargs={"pk": "0"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_price(self):
        url = reverse("price-create")
        data = {
            "product": self.product.pk,
            "price": 100.00,
            "date": str(date.today()),
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Price.objects.last().pk, response.data["id"])

        Price.objects.filter(id=response.data["id"]).delete()

    def test_cant_create_price_with_wrong_data(self):
        url = reverse("price-create")
        data = {"product": "wrong", "price": "string", "date": "date"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_calculate_average_price_valid_input(self):
        url = reverse("average-price")
        data = {
            "product_id": self.product.pk,
            "start_date": "2020-01-01",
            "end_date": "2024-02-01",
        }
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["average_price"], 25.00)

    def test_calculate_average_price_invalid_id(self):
        url = reverse("average-price")
        data = {
            "product_id": 0,
            "start_date": "2020-01-01",
            "end_date": "2024-02-01",
        }
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_calculate_average_price_invalid_date(self):
        url = reverse("average-price")
        data = {
            "product_id": self.product.pk,
            "start_date": "2023-01-01",
            "end_date": "2022-02-01",
        }
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
