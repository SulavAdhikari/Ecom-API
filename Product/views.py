from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer

# Shows all available Product
class AvailableProductsView(generics.ListAPIView):
    queryset = Product.objects.filter(availability=True)
    serializer_class = ProductSerializer


# Shows all available product of a specified user (through user.username)
class UserAvailableProductsView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return Product.objects.filter(seller__username=username, availability=True)




# Shows all product of the current logged in user
# class CurrentUserProductsView(generics.ListAPIView):
#     serializer_class = ProductSerializer

#     def get_queryset(self):
#         return Product.objects.filter(seller=self.request.user)




# Shows all available product with price range
class PriceRangeProductsView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        min_price = self.request.query_params.get('min_price', 0)
        max_price = self.request.query_params.get('max_price', float('inf'))
        return Product.objects.filter(price__range=(min_price, max_price), availability=True)


# Shows all product based on name searched
class SearchProductsView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        return Product.objects.filter(name__icontains=query)


# Shows a product with the slug
class ProductBySlugView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


# Shows all product in date range
class DateRangeProductsView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        return Product.objects.filter(posted_date__range=(start_date, end_date))
