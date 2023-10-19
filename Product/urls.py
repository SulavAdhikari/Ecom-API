from django.urls import path
from .views import (
    AvailableProductsView,
    UserAvailableProductsView,
    #CurrentUserProductsView,
    PriceRangeProductsView,
    SearchProductsView,
    ProductBySlugView,
    DateRangeProductsView
)

urlpatterns = [
    path('products/available/', AvailableProductsView.as_view(), name='available-products'),
    path('products/user/<str:username>/', UserAvailableProductsView.as_view(), name='user-available-products'),
    #path('products/me/', CurrentUserProductsView.as_view(), name='my-products'),
    path('products/price-range/', PriceRangeProductsView.as_view(), name='price-range-products'),
    path('products/search/', SearchProductsView.as_view(), name='search-products'),
    path('products/<slug:slug>/', ProductBySlugView.as_view(), name='product-by-slug'),
    path('products/date-range/', DateRangeProductsView.as_view(), name='date-range-products'),
]
