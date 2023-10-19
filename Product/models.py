from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from django.utils import timezone



def product_image_upload_path(instance, filename):
    """Generate path for product image."""
    return 'uploads/product/{slug}/image.jpg'.format(slug=instance.slug)


class Product(models.Model):
   
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')

    price = models.DecimalField(max_digits=10, decimal_places=2)
    posted_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, blank=True, editable=False)

    picture = models.ImageField(upload_to=product_image_upload_path)

    availability = models.BooleanField(default=True)

    sold = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        # If the product is being created for the first time
        if not self.slug:
            # Generate a unique slug
            slug = slugify(self.name)
            unique_slug = slug
            while Product.objects.filter(slug=unique_slug).exists():
                unique_slug = "{}-{}".format(slug, get_random_string(5))
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
