from django.urls import path
from .views import CreateReviewView, ProductReviewListView

urlpatterns = [
    path('create/', CreateReviewView.as_view(), name='create-review'),
    path('product/<int:product_id>/reviews/', ProductReviewListView.as_view(), name='product-reviews'),

]
