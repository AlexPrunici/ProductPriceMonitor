from rest_framework import serializers
from api.models import Price


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['id', 'product', 'price', 'date']
