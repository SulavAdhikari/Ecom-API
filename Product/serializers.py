from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_seller(self, obj):
        return obj.seller.username