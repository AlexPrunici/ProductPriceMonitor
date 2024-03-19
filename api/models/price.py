from django.db import models


class Price(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.product.name} - {self.date} - ${self.price}"
