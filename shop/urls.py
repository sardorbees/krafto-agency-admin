from django.urls import path

from shop.views import *

urlpatterns = [
    path('category-list/', CategoryListAPIView.as_view(), name='category-list'),
    path('size-list/', SizeListAPIView.as_view(), name='size-list'),
    path('product-list/', ProductListAPIView.as_view(), name='product-list'),
    path('add-feedback/<int:product_id>/', FeedbackCreateAPIView.as_view(), name='create-feedback'),
    path('add-favorite/<int:product_id>/', FavoriteProductCreateAPIView.as_view(), name='add-favorite'),
    path('favorites/', FavoriteProductsListAPIView.as_view(), name='list-favorite-products'),
    path('favorites/<int:pk>/', FavoriteProductDeleteAPIView.as_view(), name='delete-favorite-product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail')
]