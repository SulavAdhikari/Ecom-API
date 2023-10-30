from rest_framework import generics, status
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer
from Product.models import Product

class CreateReviewView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        product_id = self.request.data.get('product')
        try:
            product = Product.objects.get(id=product_id)
            if product not in self.request.user.orders.filter(is_paid=True).values_list('products', flat=True):
                return Response({"error": "User hasn't bought this product."}, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer.save(user=self.request.user)
