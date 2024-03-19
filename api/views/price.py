from rest_framework import viewsets
from api.models import Price
from api.serializers import PriceSerializer


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
