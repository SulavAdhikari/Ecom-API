from rest_framework import generics, status
from rest_framework.response import Response

import redis, stripe, json

from Product.models import Product
from Seller.models import Seller
from .models import Order, OrderItem, Payment
from .serializers import OrderSerializer, PaymentSerializer

r = redis.Redis(host='localhost', port=6379, db=0)

class AddToCartView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        product_slug = request.data.get('product_slug')
        quantity = request.data.get('quantity', 1)
        
        # Validate product exists
        try:
            product = Product.objects.get(slug=product_slug)
        except Product.DoesNotExist:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Add to Redis cart
        cart_key = f"cart_{request.user.id}"
        cart = r.get(cart_key)
        if cart:
            cart = json.loads(cart)
        else:
            cart = {}

        if product_slug in cart:
            cart[product_slug] += quantity
        else:
            cart[product_slug] = quantity

        r.set(cart_key, json.dumps(cart))
        return Response({"message": "Product added to cart."}, status=status.HTTP_201_CREATED)

class CheckoutView(generics.CreateAPIView):
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        cart_key = f"cart_{request.user.id}"
        cart = r.get(cart_key)
        if not cart:
            return Response({"error": "Cart is empty."}, status=status.HTTP_400_BAD_REQUEST)

        cart = json.loads(cart)
        
        # Create Order
        order = Order.objects.create(buyer=request.user)

        # Create OrderItems and remove items from cart
        for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id)
            OrderItem.objects.create(order=order, product=product, quantity=quantity)

        r.delete(cart_key)
        return Response({"message": "Order successfully created."}, status=status.HTTP_201_CREATED)

class PaymentView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

    def post(self, request, *args, **kwargs):
        order_id = request.data.get('order_id')
        amount = request.data.get('amount')
        
        # Validate order exists and is not already paid
        try:
            order = Order.objects.get(id=order_id)
            if order.is_paid:
                return Response({"error": "Order already paid."}, status=status.HTTP_400_BAD_REQUEST)
        except Order.DoesNotExist:
            return Response({"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            seller = Seller.objects.get(user=order.seller.user)
            stripe.api_key = seller.stripe_secret_key
        except Seller.DoesNotExist:
            return Response({"error": "Seller not found."}, status=status.HTTP_404_NOT_FOUND)

        # Create Stripe payment intent
        try:
            intent = stripe.PaymentIntent.create(
                amount=int(order.total_price() * 100),  # Stripe requires amount in cents
                currency='usd',
                payment_method_types=['card'],
                description=f'Order {order.id}',
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        
        # Return client secret to frontend to proceed with payment
        return Response({"client_secret": intent.client_secret}, status=status.HTTP_201_CREATED)
