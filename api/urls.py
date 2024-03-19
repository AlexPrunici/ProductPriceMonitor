from django.urls import path

from .views import (
    ProductListView,
    ProductRetrieveByIdView,
    ProductCreateView,
    PriceListView,
    PriceRetrieveByIdView,
    PriceCreateView,
    calculate_average_price
)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveByIdView.as_view(), name='product-retrieve-by-id'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),

    path('prices/', PriceListView.as_view(), name='price-list'),
    path('prices/<int:pk>/', PriceRetrieveByIdView.as_view(), name='price-retrieve-by-id'),
    path('prices/create/', PriceCreateView.as_view(), name='price-create'),
    path('prices/average/', calculate_average_price, name='average-price'),
]