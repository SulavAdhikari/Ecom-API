from django.urls import path
from Seller.views import (ProductUploadView, 
                          ProductEditView, 
                          ProductDeleteView, 
                          MakeUnavailableView, 
                          SellerProductListView, 
                          MakeAvailableView, 
                          SellerCreateView,
                          SellerDeleteView,
                          SellerRetrieveUpdateView)


urlpatterns = [
    path('seller_dashboard/upload/', ProductUploadView.as_view(), name='product-upload'),
    path('seller_dashboard/edit/<slug:slug>/', ProductEditView.as_view(), name='product-edit'),
    path('seller_dashboard/delete/<slug:slug>/', ProductDeleteView.as_view(), name='product-delete'),
    path('seller_dashboard/make-unavailable/<slug:slug>/', MakeUnavailableView.as_view(), name='make-unavailable'),
    path('seller_dashboard/make-available/<slug:slug>/', MakeAvailableView.as_view(), name='make-available'),
    path('seller_dashboard/list/', SellerProductListView.as_view(), name='seller-product-list'),
    path('seller_dashboard/create/', SellerCreateView.as_view(), name='seller-create'),
    path('seller_dashboard/<int:id>/', SellerRetrieveUpdateView.as_view(), name='seller-retrieve-update'),
    path('seller_dashboard/<int:id>/delete/', SellerDeleteView.as_view(), name='seller-delete'),
]


