from django.db.models import Avg
from django.utils import timezone
from django.utils.dateparse import parse_date
from rest_framework import generics, status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Price, Product
from api.serializers import PriceSerializer


class PriceListView(generics.ListAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class PriceRetrieveByIdView(generics.RetrieveAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    lookup_field = 'pk'


class PriceCreateView(generics.CreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

    def perform_create(self, serializer):
        product_id = self.request.data.get('product')
        product_exists = Product.objects.filter(pk=product_id).exists()
        if not product_exists:
            raise serializers.ValidationError({'error': 'Product does not exist.'})

        date = serializer.validated_data.get('date')
        if date > timezone.now().date():
            raise serializers.ValidationError({'error': 'Price date cannot be in the future.'})

        serializer.save()


@api_view(['POST'])
def calculate_average_price(request):
    product_id = request.data.get('product_id')
    start_date_str = request.data.get('start_date')
    end_date_str = request.data.get('end_date')

    if not all([product_id, start_date_str, end_date_str]):
        return Response({'error': 'Please provide product_id, start_date, and end_date.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    start_date = parse_date(start_date_str)
    end_date = parse_date(end_date_str)

    if not all([start_date, end_date]):
        return Response({'error': 'Invalid date format. Please provide dates in YYYY-MM-DD format.'}, status=status.HTTP_400_BAD_REQUEST)

    if end_date < start_date:
        return Response({'error': 'End date cannot be before start date.'}, status=status.HTTP_400_BAD_REQUEST)

    average_price = Price.objects.filter(product=product, date__range=(start_date, end_date)).aggregate(Avg('price'))['price__avg']

    if average_price is None:
        return Response({'message': 'No prices found for the given period.'}, status=status.HTTP_200_OK)

    average_price = round(average_price, 2)

    return Response({'average_price': average_price}, status=status.HTTP_200_OK)
