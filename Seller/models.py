from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Seller(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='seller_profile')
    stripe_public_key = models.CharField(max_length=200, blank=True, null=True, help_text="Stripe Public Key for the seller's Stripe account.")
    stripe_secret_key = models.CharField(max_length=200, blank=True, null=True, help_text="Stripe Secret Key for the seller's Stripe account.")
    business_phone = models.CharField(max_length=15, blank=True, null=True)
    business_address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.business_name or self.user.username
