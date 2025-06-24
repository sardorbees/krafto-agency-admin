from django.urls import path
from .views import NotificationListAPIView
from .views import latest_notification_id

urlpatterns = [
    path('', NotificationListAPIView.as_view(), name='notifications-list'),
    path('admin/notifications/last-id/', latest_notification_id),
]
