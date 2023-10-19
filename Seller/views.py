from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from User.authentication import CustomJWTAuthentication
from Product.models import Product
from .serializers import ProductUploadSerializer

class ProductUploadView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductUploadSerializer
    authentication_classes = [CustomJWTAuthentication]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user, availability=True)

class ProductEditView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductUploadSerializer
    authentication_classes = [CustomJWTAuthentication]
    lookup_field = 'slug'
    parser_classes = [MultiPartParser, FormParser]

class ProductDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductUploadSerializer
    authentication_classes = [CustomJWTAuthentication]
    lookup_field = 'slug'

class MakeUnavailableView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductUploadSerializer
    authentication_classes = [CustomJWTAuthentication]
    lookup_field = 'slug'

    def update(self, request, *args, **kwargs):
        product = self.get_object()
        product.availability = False
        product.save()
        return Response({"message": "Product marked as unavailable"}, status=status.HTTP_200_OK)


class MakeAvailableView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductUploadSerializer
    authentication_classes = [CustomJWTAuthentication]
    lookup_field = 'slug'

    def update(self, request, *args, **kwargs):
        product = self.get_object()
        product.availability = True
        product.save()
        return Response({"message": "Product marked as available"}, status=status.HTTP_200_OK)


class SellerProductListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductUploadSerializer
    authentication_classes = [CustomJWTAuthentication]

    def get_queryset(self):
        return Product.objects.filter(seller=self.request.user)


# setup for seller dashboard

from .models import Seller
from .serializers import SellerSerializer

class SellerCreateView(generics.CreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

class SellerRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    lookup_field = 'id'

class SellerDeleteView(generics.DestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    lookup_field = 'id'
