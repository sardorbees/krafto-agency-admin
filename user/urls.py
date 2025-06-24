from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('api/register/', CustomUserRegisterAPIView.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user-update/', CustomUserUpdateAPIView.as_view(), name='update_user'),
    path('api/profile/', CustomUserAPIView.as_view(), name="profile"),

    path('cart/', CartDetailAPIView.as_view(), name='cart-detail'),
    path('cart/add/', CartItemAddAPIView.as_view(), name='cart-item-add'),
    path('cart/remove/<int:product_id>/', CartItemRemoveAPIView.as_view(), name='cart-item-remove'),
    path('cart/clear/', CartClearAPIView.as_view(), name='cart-clear'),
]
